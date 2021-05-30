# mail-sender-program
a program that sends gmail in 2 lines of code 

## examples:

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
import gmmail_sender as g 
g.send_gmail_to_people_in_list(email_name,password_for_gmail , to(list), subject, content)
```

# it is that simple
