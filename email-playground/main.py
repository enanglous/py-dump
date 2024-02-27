import smtplib
from email.message import EmailMessage
from LOGININFO import user, password

email = EmailMessage()
email['from'] = 'baser'
email['to'] = 'wildghost613@gmail.com'  # :sob:
email['subject'] = 'You won 1,000,000 dollars!'

email.set_content('I don\'t know how to code')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(user, password)
    smtp.send_message(email)
    print('all good boss!')
