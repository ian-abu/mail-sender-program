# mail-sending-program 0.1.2

a program that makes it easy to send emails with python

# install
```cmd
pip install mail-sending-program
```

# uninstall 

```cmd
pip uninstall mail-sending-program
```


# examples:

## 1 sending html to one person:
```python
import gmail_sender as g 
g.send_html_gmail_to_one(email_name,password_for_gmail , to, subject, content_html)

```
## 2 sending regular gmail to a person:
```python 
import gmail_sender as g 
g.send_gmail_to_one(email_name,password_for_gmail , to, subject, content)

```

## 3 send html gmail to many people:
```python 
import gmail_sender as g 
send_html_gmail_to_people_in_list(email_name,password_for_gmail , to(list), subject, content_html)
```

## 4 send regular gmail to many people:
```python 
import gmail_sender as g 
g.send_gmail_to_people_in_list(email_name,password_for_gmail , to(list), subject, content)
```
## 5 send random letters with caps lock to someone:
```python 
import gmail_sender as g 
g.send_random_message_no_word_meaning_caps_lock(email_name,password_for_gmail , to, subject, how many letters)
```
## 6 send random lower case letters someone:
```python
import gmail_sender as g 
g.send_random_message_no_word_meaning_lower_case(email_name,password_for_gmail , to, subject, how many letters)
```

# updates

## 0.1.3

you will be able to:

1. send gmails to **multipule** people with random letters 

2. send gmail to people with a random meaning

<h1>update coming in 20.6.2021<h1>

# to my gethub click [here](https://github.com/Pydevoleper/mail-sender-program)
