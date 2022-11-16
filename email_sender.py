import smtplib
import os
from email.mime.text import MIMEText
from dotenv import load_dotenv


load_dotenv()

def send_email():
    sender = 'mv.rogozov@ya.ru'
    password = os.getenv('EMAIL_PASSWORD')
    send_to = 'mv.rogozov@ya.ru'
    template_file = 'template.html'

    server = smtplib.SMTP('smtp.yandex.ru', 587)
    server.ehlo()
    server.starttls()
    print(password)
    try:
        with open(template_file) as file:
            template = file.read()
    except IOError:
        return 'Error during opening template file.'

    try:
        server.login(sender, password)
        msg = MIMEText(template, 'html')
        msg['Subject'] = 'subject text'
        server.sendmail(sender, send_to, msg.as_string())
        return 'Email sent'
    except Exception as e:
        return 'Error, during sending message.\n{}'.format(e)
    

def main():
    print(send_email())


if __name__ == '__main__':
    main()
