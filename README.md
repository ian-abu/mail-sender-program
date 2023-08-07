# mail-sending-program 1.5
<p align="center">
  <img alt="PyPI" src="https://img.shields.io/pypi/v/mail-sending-program">
  <img alt="GitHub" src="https://img.shields.io/github/license/ian-abu/mail-sender-program">
  <img alt="GitHub Workflow Status (with event)" src="https://img.shields.io/github/actions/workflow/status/ian-abu/mail-sender-program/.github%2Fworkflows%2Fcodeql-analysis.yml">
  <a href="https://pepy.tech/project/quote"><img alt="Downloads" src="https://pepy.tech/badge/mail-sending-program"></a>
</p>
a program that makes it really easy to send emails and read emails with python

#

# sections
* [install](#install)  
* [update](#update)  
* [uninstall](#uninstall)  
* [sending a html email to one person](#1-sending-a-html-email-to-one-person)  
* [sending regular gmail to a person](#2-sending-plain-text-gmail-to-a-person)  
* [sending a html email to one person](#3-send-html-gmail-to-many-people)  
* [send plain text email to many people](#4-send-plain-text-gmail-to-many-people)
* [send random caps-lock letters to someone](#5-send-random-letters-with-caps-lock-to-someone)
* [send random caps-lock letters to many people](#6-random-letters-with-caps-lock-to-many-people)
* [send random lower letters to someone](#7-send-random-lower-case-letters-someone)
* [send random lower letters to many people](#8-send-random-lower-case-letters-to-many-people)
* [read your email](#9-read-email)
* [read your email](#9-read-email)
* [send plain text email with attachment](#10-send-gmail-with-attachment)
* [send html email with attachment](#11-send-gmail-with-attachment)
* [inputs in a function](#inputs-in-a-function)
* [updates](#updates)
* [latest update](#latest-update)

# install
```cmd
pip install mail-sending-program
```
#
# update

```cmd
pip install --upgrade mail-sending-program
```
#
# uninstall 

```cmd
pip uninstall mail-sending-program
```
#
# examples:

## 1 sending a html email to one person:
```python
import gmail_sender as g 
g.send_html_gmail_to_one(email_name,password_for_gmail , to, subject, content_html, write)
# or if you want to use a template use 
g.send_html_gmail_to_one(email_name,password_for_gmail , to, subject, load_template(filename), write)
```

## 2 sending plain text gmail to a person:
```python 
import gmail_sender as g 
g.send_gmail_to_one(email_name,password_for_gmail , to, subject, content)

```

## 3 send html gmail to many people:
```python 
import gmail_sender as g 
send_html_gmail_to_people_in_list(email_name,password_for_gmail , to(list), subject, content_html)
# or if you want to use a template use 
g.send_html_gmail_to_one(email_name,password_for_gmail , to, subject, load_template(filename), write)
```

## 4 send plain text gmail to many people:
```python 
import gmail_sender as g 
g.send_gmail_to_people_in_list(email_name,password_for_gmail , to(list), subject, content)
```
## 5 send random letters with caps lock to someone:
```python 
import gmail_sender as g 
g.send_random_message_no_word_meaning_caps_lock(email_name,password_for_gmail , to, subject, letters)
```

## 6 random letters with caps lock to many people:
```python
import gmail_sender as g 

g.send_random_message_no_word_meaning_caps_lock_to_many(email_name, password_for_gmail  ,to list, subject ,lettrs):

```
## 7 send random lower case letters someone:
```python
import gmail_sender as g 
g.send_random_message_no_word_meaning_lower_case(email_name,password_for_gmail , to, subject, letters)
```
## 8 send random lower case letters to many people:
```python 
import gmail_sender as g 
g.send_random_message_no_word_meaning_lower_case(email_name, password_for_gmail  ,to list, subject ,lettrs)
```
## 9 read email:
```python
import gmail_sender as g 
email = g.read_email(email_name, password_for_gmail, org)
print(email)
```

## 10 send gmail with attachment:

```python
import gmail_sender as g
g.send_attachment_with_regular_body(email_name, password_for_gmail, to, subject, content, path_to_file, write)
```
## 11 send gmail with attachment:

```python
import gmail_sender as g
g.send_attachment_with_html_body(email_name, password_for_gmail, to, subject, content_html, path_to_file, write)
# or if you want to use a template use 
g.send_html_gmail_to_one(email_name,password_for_gmail , to, subject, load_template(filename), write)
```
# 

# inputs in a function

| input name | explanation |
|---|---|
| email name | your email name |
| password_for_gmail| your email password|
| to | to wich email address you want to send the email|
| to(list)| a list of people to send to|
| subject| emails subject|
| content| emails content|
| letters| how many letters do you want in the email|
| content_html| emails html content|
| load_template(filename)| load a html template and instead of filename use your html template|
| path_to_file| path yto the file you want to attach|
| write| if you want to write your email in a file called gmail.txt set as yes if not dont fill it|

#

# updates

there is nothing planned if you are interested in a feature contact me with issues

# latest update

## 1.5
1. make an auto sending bot to send email at any time you want to whoever you want

2. adding ways to make a template file other than html

3. bug fixes
#

# to my github click [here](https://github.com/ian-abu/mail-sender-program)

# to the pypi page click [here](https://pypi.org/project/mail-sending-program/)

# if there are any bugs please report
