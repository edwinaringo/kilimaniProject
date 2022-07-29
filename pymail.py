import os
import smtplib
from email.message import EmailMessage

email_id = 'biancaedwin44@gmail.com'
email_pass = 'spvoticszkmycxjj'

recipient_list = ['tedaringo628@gmail.com', 'edwinaringo32@gmail.com']

msg = EmailMessage()
msg['Subject'] = 'Land Change Notice'
msg['From'] = email_id
msg['To'] = recipient_list
msg.set_content('This is to inform you that the following piece of land is changing its use. Click on the link below for more informaion. In case of any complaints, please fill the form found withing the link. Thank you for your cooperation.')

for each_file in os.listdir():
    if each_file == 'pymail.py':
        continue
    with open(each_file, 'rb') as f:
        file_data = f.read()
        file_name = f.name
        msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(email_id, email_pass)
    smtp.send_message(msg)