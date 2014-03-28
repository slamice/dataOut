#!/usr/bin/env python
import re
import sys
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def create_addresses(from_addr,to_addr,cc=[],bcc=[]):
    msg = MIMEMultipart()
    msg['From'] = from_addr
    msg['To'] = to_addr
    if cc:
        msg['CC'] = cc
    if bcc:
        msg['BCC'] = bcc
    return msg.as_string()

def check_email_valid(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+",email) != None

def add_subject_to_email(msg,subject):
    try:
        msg['Subject'] = subject
        return msg
    except Exception,e:
        print str(e)

# only plain text
def add_text_to_email(msg,text):
    try:
        msg.attach(MIMEText(text, 'plain'))
        return msg
    except Exception,e:
        print str(e)

def add_html_to_email(msg,html):
    try:
        msg.attach(MIMETEXT(html,'html'))
        return msg
    except Exception,e:
        print str(e)

def send_mail(to_addr,cc,bcc,msg,username,password,host,port):
    try:
        s = smtplib.SMTP_SSL(host, port)
        s.ehlo()
        s.login(username,password)
        s.sendmail(username,[to_addr,cc,bcc],msg.as_string())
        s.quit()
    except Exception,e:
        print str(e)






