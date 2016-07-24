#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import sys

import smtplib
import email
import os
import sys

from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.message import MIMEMessage

class PostMail:
    __smtp = { 'yandex' : 'smtp.yandex.ru:465', 'gmail' : 'smtp.gmail.com:587', 'mail' : 'smtp.mail.ru:588'  }
    __email = MIMEMultipart()
    __subject = u"Показания приборов учёта"
    __parts = list()
    
    def __init__(self,post="yandex", login="user", password="12345678", sender="user@mail.com", recipient="user@mail.com" , msg=""):
        self.post = post
        self.login = login
        self.password = password
        self.sender = sender
        self.recipient = recipient
        self.msg = msg
        
    def connect_yandex(self):
        self.__smtp = smtplib.SMTP_SSL( self.__smtp.get(self.post) )
        self.__smtp.login( self.login, self.password )
    
    def connect_gmail(self):
        self.__smtp = smtplib.SMTP( self.__smtp.get(self.post) )
        self.__smtp.ehlo()
        self.__smtp.starttls()
        self.__smtp.login(self.login, self.password)
    
    def connect_mail(self):
        print("SMTP : mail" )        
    
    def __dispatch(self):
        method_name = 'connect_' + str(self.post)
        method = getattr(self, method_name)
        return method()
        
    def setMsg(self, msg):
        self.msg = msg
    
    def genMsg(self, template, keys, values):
        if template is None:
            print('The template is not correct')
        if keys is None:
            print('The keys is not correct')
        if values is None:
            print('The values is not correct')
        try:
            data = dict(zip(keys,values))
            print("Keys:{}, values:{}".format(keys,values))
            self.msg = template.format(**data)
            return self.msg
        except Exception as exc:
            print( "PostMail.genMSg() failed; {}".format(str(exc)) ) # give a error message
            return False
        
    def __createMessage(self):
        self.__email['From'] = self.sender
        self.__email['To'] = self.recipient
        self.__email['Subject'] = self.__subject
        self.__email.attach(MIMEText(self.msg, 'html',_charset='utf-8'))
        for part in self.__parts:
            self.__email.attach(part)
        
    def attachFile(self,filepath):
        try:
            part = MIMEBase('application', "octet-stream")
            basename = os.path.basename(filepath)
            try:
                part.set_payload(open(filepath,"rb").read() )
            finally:
                email.encoders.encode_base64(part)
                part.add_header('Content-Disposition', 'attachment; filename="%s"' % basename)
                self.__parts.append(part)
        except Exception as exc:    
            print( "attachFile({}) failed; {}".format(filepath,str(exc)) )

    def Test(self):
        print( self.__smtp.get(self.post) )
        
    def sendMail(self):
        try:
            self.__createMessage()
            self.__dispatch()
            try:
                print("log: From : {}  To : {}  \nBody: {}".format( self.sender, self.recipient, self.__email) )
                self.__smtp.sendmail(self.sender, self.recipient, self.__email.as_string())
            finally:
                self.__smtp.quit()
                return True
        except Exception as exc:
            print( "mail({}) failed; {}".format(self.post,str(exc)) ) # give a error message
            return False
