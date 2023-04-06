# This project is a WhatsApp bot thats aims to automatic send messages to a list of contacts.

## Funcionality
The bot utilizes the WhatsApp web interface to mimic human behavior. The bot makes use of Selenium, a web browser automation tool, to interact with HTML web page objects and make decisions based on a predetermined script. Codes are written in python.

## How it works:
1. Manually import your contact list as a csv to the repository.
2. Have a cellphone with WhatsApp installed and ready to authenticate the application sign in on web interface by QR code.
3. Create a WhatsApp group with any name and pin it to the top of your conversation tab (you can be alone in this group).
4. Write the name of the created group right after `group_name` in the repository's file `user_parameters.yaml`.
5. In the group, send the messages you want to be forwarded. On this first release, it can only be text or image. The order of the messages is important, so the messages will be forwarded in the exaclty same order you put them on your WhatsApp group.
6. Again inside the file `user_parameters.yaml`, type the amount of messages you want to foward right after `historic_to_send`.<br>
  __Example for steps 5 and 6__: if you want to mass send 4 messages, you post them in your group in the exact order you want it to be forwarded. Then you go to the user_parameters.yaml and type the amount of messages your batch contains, in this case: 4. The bot will select the last 4 messages in the referenced group and forward it to the contact list.
7. Run `python script.py`;
8. Authorize WhatsApp web interface to log in through QR code.

<br><br><br><br><br>
ToDos:
- video of funcionality
- add google chrome web driver instructions, credits and content
- create yaml files
- replace selenium functions for it to wait specific events
