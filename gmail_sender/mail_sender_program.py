import smtplib
from email.message import EmailMessage
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time
from datetime import datetime
def send_gmail_to_people_in_list(email_name,password_for_gmail , to, subject, content):
    email_address = email_name
    msg = EmailMessage()
    msg['subject '] = subject
    msg['from'] = email_address
    msg['to'] = ', '.join(to)
    msg.set_content(content)
    msg.set_content(content)
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login( email_address, password_for_gmail)
        smtp.send_message(msg)
    

def send_html_gmail_to_people_in_list(email_name,password_for_gmail , to, subject, content_html):
    content = MIMEText(content_html, "html")
    email_address = email_name
    msg = EmailMessage()
    msg['subject '] = subject
    msg['from'] = email_address
    msg['to'] = ', '.join(to)
    msg.set_content(content)
    msg.set_content(content)
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login( email_address, password_for_gmail)
        smtp.send_message(msg)
        

def send_gmail_to_one(email_name,password_for_gmail , to, subject, content):
    email_address = email_name
    msg = EmailMessage()
    msg['subject '] = subject
    msg['from'] = email_address
    msg['to'] = to
    msg.set_content(content)
    msg.set_content(content)
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login( email_address, password_for_gmail)
        smtp.send_message(msg)
       

def send_html_gmail_to_one(email_name,password_for_gmail , to, subject, content_html):
    content = MIMEText(content_html, "html")
    email_address = email_name
    msg = EmailMessage()
    msg['subject '] = subject
    msg['from'] = email_address
    msg['to'] = to
    msg.set_content(content)
    msg.set_content(content)
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login( email_address, password_for_gmail)
        smtp.send_message(msg)
        
