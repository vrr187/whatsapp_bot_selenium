from selenium import webdriver
import time
import datetime
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import pandas as pd
import numpy as np


########################## FUNCTIONS #################################

def reach_root_chat(fixed_contact):

    search_box = driver.find_element_by_xpath('//div[contains(@class, "copyable-text selectable-text")]')
    wait(total_seconds=3, random_factor=0.1)
    
    search_box.click()
    wait(total_seconds=2, random_factor=0.1)

    search_box.send_keys(fixed_contact)
    wait(total_seconds=10, random_factor=0.1)

    search_box.send_keys(Keys.ENTER)
    wait(total_seconds=10, random_factor=0.1)

def content_selector(msgs):

    # pega o botao de menu da pagina da conversa
    conversation_menu_button = driver.find_element_by_xpath("//div[@data-testid='conversation-menu-button']")
    wait(total_seconds=1, random_factor=0.1)

    # clica nele
    conversation_menu_button.click()
    wait(total_seconds=5, random_factor=0.1)

    # pega o botao de selecionar mensagens
    select_msg_button = driver.find_element_by_xpath("//div[@aria-label='Select messages']")
    wait(total_seconds=1, random_factor=0.1)

    # clica nele
    select_msg_button.click()
    wait(total_seconds=5, random_factor=0.1)   

    # pega todos os botoes de envio da midia que o chat ta agora
    selectable_midia_list = driver.find_elements_by_xpath("//div[@data-testid='visual-checkbox']")
    wait(total_seconds=1, random_factor=0.1)

    # fazer um loop que seleciona as midias

    selected_boxes = 0

    for i in list(np.arange(-msgs, 0, 1, dtype=int)):
        
        selectable_midia_list[i].click()
        wait(total_seconds=5, random_factor=0.1)

        selected_boxes = selected_boxes + 1
        # add delay e foi

    if selected_boxes != msgs:

        print('MESAGENS SELECTOR ERROR')
        wait(total_seconds=0.5, random_factor=0.1)
        RAISE_ERROR

def forward_mensage():

    forward_button = driver.find_element_by_css_selector("span[data-testid='forward']")
    wait(total_seconds=0.5, random_factor=0.1)

    forward_button.click()
    wait(total_seconds=5, random_factor=0.1)

def get_next_user(df):
    """ filtra o df pra deixar so pros caras que devem receber
    """

    df = df[df['reachable'] != 0] # nao pode nao ser achavel
    df = df[df['delivered'] == -1] # nao pode ter tido tentivas de enviar msg a ele
    
    # orderna por rank priority
    df = df.sort_values('rank_priority').reset_index(drop=True)
    
    # pega o primeiro nome do df
    name = str(df['Display Name'][0])
    
    return name

def reach_contact(name):

    """tenta localizar um contato, pelo sim ou pelo nao, ele retorna seus status
    """

    # localiza search box
    search_box = driver.find_element_by_xpath("//div[@data-testid='chat-list-search']")
    wait(total_seconds=1, random_factor=0.1)
    
    # clica nela
    search_box.click()
    wait(total_seconds=2, random_factor=0.1)

    # seleciona todo o texto
    search_box.send_keys(Keys.CONTROL, 'a')
    wait(total_seconds=2, random_factor=0.1)
    
    # apaga tudo
    search_box.send_keys(Keys.BACKSPACE)
    wait(total_seconds=1, random_factor=0.1)

    # digita o nome
    search_box.send_keys(name)
    wait(total_seconds=2, random_factor=0.1)

    # verifica se o usuario e achavel
    try:
        
        # se ele nao der erro aqui, ele nao e achavel
        failed_search = driver.find_element_by_xpath("//div[@data-testid='search-no-chats-or-contacts']")
        wait(total_seconds=1, random_factor=0.1)

        reachable_status = 0
        delivered_status = 0     

    except:

        # se ele tiver achado, vai apertar enter, selecionando o primeiro contato da lista que apareceu
        search_box.send_keys(Keys.ENTER)
        wait(total_seconds=2, random_factor=0.1)

        reachable_status = 1
        delivered_status = 1

    return reachable_status, delivered_status

def update_df(df, name, reachable, delivered):

    df.loc[df['original_name'] == name, ['reachable']] = reachable
    df.loc[df['original_name'] == name, ['delivered']] = delivered
    df.loc[df['original_name'] == name, ['updated_at']] = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')

    return df

def upload_df(df, path):
    """Recebe um df, salva no path que recebeu, e retorna o mesmo df - desnecessario mas ok
    """

    # save
    df.to_csv(path, index=False)
    
    # load
    df = pd.read_csv(path)

    return df


    

    return reachable_status, delivered_status

def send_mesage():

    send_button = driver.find_element_by_css_selector("span[data-testid='send']")
    wait(total_seconds=2, random_factor=0.1)

    send_button.click()

def wait(total_seconds, random_factor):

    upper_limit = total_seconds + (total_seconds*random_factor)
    lower_limit = abs(total_seconds - (total_seconds*random_factor))

    time_to_wait = np.random.uniform(low=lower_limit, high=upper_limit)

    time.sleep(time_to_wait)


########################## SETTINGS ###################################

# instala o driver e abre o chrome pra autenticacao
print('Installing driver')
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://web.whatsapp.com/')
wait(total_seconds=300, random_factor=0.1)

# sent_file path
path = 'data/sent/01_contatos_1_2.csv'

# first_time load df
df = pd.read_csv(path)

# define max users
max_users = 2000

# define quantidade de mensagens a serem encaminhadas
msgs = 3

# nome do chat de onde as msgs devem sair
fixed_contact = 'ALFA1' ##'eu mesmo' #'ALFA1'


########################## RUNNING #####################################

total_runs = max_users/5
current_run = 0

print('Starting main loop...')
wait(total_seconds=1, random_factor=0.1)

while (current_run < total_runs):

    # vai ao contato cujo a msg a ser enviada se encontra
    print('Running reach_root_chat...')
    wait(total_seconds=1, random_factor=0.1)
    reach_root_chat(fixed_contact)

    # selecao de conteudo
    print('Running content_selector...')
    wait(total_seconds=1, random_factor=0.1)
    content_selector(msgs)

    # envia mensagens
    print('Running forward_mensage...')
    wait(total_seconds=1, random_factor=0.1)
    forward_mensage()


    print('Starting batch loop', current_run)
    wait(total_seconds=1, random_factor=0.1)
    contacts_batch = 0

    while (contacts_batch<5):
        
        # pegar um usuario
        print('Running get_next_user...')
        name = get_next_user(df)
        wait(total_seconds=1, random_factor=0.1)

        # tenta achar ele e retorna se conseguiu
        print('Running reach_contact...')
        reachable_status, delivered_status = reach_contact(name)
        wait(total_seconds=1, random_factor=0.1)

        # atializa o df
        print('Running update_df...')
        df = update_df(df, name, reachable_status, delivered_status)
        wait(total_seconds=1, random_factor=0.1)

        # upa a atualizacao
        print('Running upload_df...')
        df = upload_df(df, path)
        wait(total_seconds=2, random_factor=0.1)

        # adiciona 1 caso sucesso e 0 se falha
        contacts_batch = contacts_batch + reachable_status
        wait(total_seconds=1, random_factor=0.1)

    if (contacts_batch == 5):

        # envia msg
        send_mesage()
        wait(total_seconds=3, random_factor=0.1)

        print('Batch', current_run, 'sent.')


    # o while garante que o codigo so avanca se ele tiver 5 success

    # pra cada batch, esse while garante que o script so e interrompido se rodar x vezes
    current_run = current_run + 1






