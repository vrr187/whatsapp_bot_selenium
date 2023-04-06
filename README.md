# This project is a WhatsApp bot created with Python using the library Selenium as its main develop tool.

## Funcionality
The bot simulates human behavior using WhatsApp web interface. It uses Selenium to interact with the HTML web page objects and take decisions guided by a script. The main goal consists in sending a message, or a pack messages to a limited list of users.


## How it works:
1. Manually import your contact list as a csv to the repository;
2. Have a cellphone with whatsapp installed and ready to authenticate WhatsApp web login by QR code;
3. Create a WhatsApp group with any name and fix it in your conversation (you can be alone in this group);
4. Write the name of the created group right after 'group_name' in the repository's file user_parameters.yaml;
5. In the group, send the messages you want to be mass forwarded. It can be any kind: text, image, video, audio. The order of the messages is important, so the messages will be forwarded in the exaclty same order you put it on your WhatsApp group;
6. Again inside the file user_parameters.yaml, type the amount of messages you want to foward right after 'historic_to_send'.
Example for steps 5 and 6: if you want to mass send 4 messages, you post them in your group in the exact order you want it to be forwarded. Then you go to the user_parameters.yaml and type the amount of messages your batch contains, in this case: 4. The bot will select the last 4 messages in the referenced group and forward it to the contact list.
7. Run python script.py;
8. Authorize WhatsApp web interface to log in through QR code.
