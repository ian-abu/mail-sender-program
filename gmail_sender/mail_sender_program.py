from os import write
import smtplib
from email.message import EmailMessage
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from time import strftime
import random
import email
import ssl
import traceback 
import imaplib
from email.mime.base import MIMEBase
from email import encoders
from datetime import datetime
def load_template(name):
    f = open(name)
    html = f.read()
    return html
def write_to_file(content):
    ntime = strftime('%H:%M:%S %p')
    f = open("gmail.txt", "a")
    f.write("======================================\n")
    f.write("sent at " + ntime + "\n")
    f.write(content + "\n")
    f.write("======================================\n")
def send_gmail_to_people_in_list(email_name,password_for_gmail , to, subject, content, write=None):
    if write == "":
        write = "no"
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
        if write == "yes":
            write_to_file(content)
def send_html_gmail_to_people_in_list(email_name,password_for_gmail , to, subject, content_html, write=None):
    if write == "":
        write = "no"
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
        if write == "yes":
            write_to_file(content_html)


def send_gmail_to_one(email_name,password_for_gmail , to, subject, content, write=None):
    if write == "":
        write = "no"
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
        if write == "yes":
            write_to_file(content)


def send_html_gmail_to_one(email_name,password_for_gmail , to, subject, content_html, write=None):
    if write == "":
        write = "no"
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
        if write == "yes":
            write_to_file(content_html)

def send_attachment_with_regular_body(email_name, password_for_gmail, to, subject, content, path_to_file, write=None):
    if write == "":
        write = "no"
    message = MIMEMultipart()
    message["From"] = email_name
    message["To"] = to
    message["Subject"] = subject
    message.attach(MIMEText(content, "plain"))

    filename = path_to_file

    with open(filename, "rb") as attachment:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())


    encoders.encode_base64(part)

    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {filename}",
    )

    message.attach(part)
    text = message.as_string()

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(email_name, password_for_gmail)
        server.sendmail(email_name, to, text)
        if write == "yes":
            write_to_file(content)
def send_attachment_with_html_body(email_name, password_for_gmail, to, subject, content_html, path_to_file, write=None):
    if write == "":
        write = "no"
    message = MIMEMultipart()
    message["From"] = email_name
    message["To"] = to
    message["Subject"] = subject
    message.attach(MIMEText(content_html, "html"))

    filename = path_to_file 

    with open(filename, "rb") as attachment:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())


    encoders.encode_base64(part)

    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {filename}",
    )

    message.attach(part)
    text = message.as_string()

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(email_name, password_for_gmail)
        server.sendmail(email_name, to, text)
        if write == "yes":
            write_to_file(content_html)
def send_random_message_no_word_meaning_caps_lock(email_name, password_for_gmail  ,to, subject ,lettrs, write=None):
    if write == "":
        write = "no"
    lettrs = int(lettrs)
    list1 = [
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "K",
        "L",
        "M",
        "N",
        "O",
        "P",
        "Q",
        "R",
        "S",
        "T",
        "U",
        "V",
        "W",
        "X",
        "Y",
        "Z"
    ]
    content = ""
    for i in range(lettrs):
        content1 = random.choice(list1)
        content = content + content1
    
    send_gmail_to_one(email_name, password_for_gmail,to, subject, content)
    if write == "yes":
        write_to_file(content)
def send_random_message_no_word_meaning_lower_case(email_name, password_for_gmail  ,to, subject ,lettrs, write=None):
    if write == "":
        write = "no"
    lettrs = int(lettrs)
    content = ""
    list1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for i in range(lettrs):
        content1 = random.choice(list1)
        content = content + content1
    
    send_gmail_to_one(email_name, password_for_gmail,to, subject, content)
    if write == "yes":
        write_to_file(content)
def send_random_message_no_word_meaning_caps_lock_to_many(email_name, password_for_gmail  ,to, subject ,lettrs, write=None):
    if write == "":
        write = "no"
    lettrs = int(lettrs)
    list1 = [
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "K",
        "L",
        "M",
        "N",
        "O",
        "P",
        "Q",
        "R",
        "S",
        "T",
        "U",
        "V",
        "W",
        "X",
        "Y",
        "Z"
    ]
    content = ""
    for i in range(lettrs):
        content1 = random.choice(list1)
        content = content + content1
    
    send_gmail_to_people_in_list(email_name, password_for_gmail,to, subject, content)
    if write == "yes":
        write_to_file(content)
def send_random_message_no_word_meaning_lower_case(email_name, password_for_gmail  ,to, subject ,lettrs, write=None):
    if write == "":
        write = "no"
    lettrs = int(lettrs)
    content = ""
    list1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for i in range(lettrs):
        content1 = random.choice(list1)
        content = content + content1
    
    send_gmail_to_people_in_list(email_name, password_for_gmail,to, subject, content)
    if write == "yes":
        write_to_file(content)

def send_gmail_with_meaning(email_name, password_for_gmail,to, write=None):
    if write == "":
        write = "no"
    listg = [
        "hello, good morning",
        "what a good morning",
        "i had good breakfast",
        "good morning!",
        "do you like cornflakes?"
    ]
    lista = [
        "good, afternoon",
        "good day",
        "have a good day", 
        "stay safe", 
        "today is amazing"
    ]
    listr = [
        "are you having dinner?",
        "dinner was amazing loved it ",
        "good night"
    ]
    lists = [
        "hello", 
        "hallo", 
        "hi", 
        "how are you"
    ]
    now = datetime.now()

    current_time = now.strftime("%H")

    if current_time == "12" or "12" > current_time and current_time  > "0":
        content = random.choice(listg)

    if current_time != "12" or "12" < current_time and current_time < "20":
        content = random.choice(lista)
    
    else:
        content = random.choice(listr)
    
    subject = random.choice(lists)
    send_gmail_to_one(email_name, password_for_gmail, to, subject, content)
    if write == "yes":
        write_to_file(content)
def send_gmail_with_meaning_to_many(email_name, password_for_gmail,to, write=None):
    if write == "":
        write = "no"
    listg = [
        "hello, good morning",
        "what a good morning",
        "i had good breakfast",
        "good morning!",
        "do you like cornflakes?"
    ]
    lista = [
        "good, afternoon",
        "good day",
        "have a good day", 
        "stay safe", 
        "today is amazing"
    ]
    listr = [
        "are you having dinner?",
        "dinner was amazing loved it ",
        "good night"
    ]
    lists = [
        "hello", 
        "hallo", 
        "hi", 
        "how are you"
    ]
    now = datetime.now()

    current_time = now.strftime("%H")

    if current_time == "12" or "12" > current_time and current_time  > "0":
        content = random.choice(listg)

    if current_time != "12" or "12" < current_time and current_time < "20":
        content = random.choice(lista)
    
    else:
        content = random.choice(listr)
    
    subject = random.choice(lists)
    send_gmail_to_people_in_list(email_name, password_for_gmail, to, subject, content)
    if write == "yes":
        write_to_file(content)
def read_email(email_name, password_for_gmail):
    try:
        FROM_EMAIL = email_name
        FROM_PWD = password_for_gmail
        SMTP_SERVER = "imap.gmail.com" 
        SMTP_PORT = 993
        mail = imaplib.IMAP4_SSL(SMTP_SERVER)
        mail.login(FROM_EMAIL,FROM_PWD)
        mail.select('inbox')

        data = mail.search(None, 'ALL')
        mail_ids = data[1]
        id_list = mail_ids[0].split()   
        first_email_id = int(id_list[0])
        latest_email_id = int(id_list[-1])

        for i in range(latest_email_id,first_email_id, -1):
            data = mail.fetch(str(i), '(RFC822)' )
            for response_part in data:
                arr = response_part[0]
                if isinstance(arr, tuple):
                    msg = email.message_from_string(str(arr[1],'utf-8'))
                    email_subject = msg['subject']
                    email_from = msg['from']
                    if email_subject != None:
                        print('From : ' + str(email_from) + '\n')
                        print('Subject : ' + str(email_subject) + '\n')
                    else: 
                        break

    except Exception as e:
        traceback.print_exc() 
        print(str(e))
