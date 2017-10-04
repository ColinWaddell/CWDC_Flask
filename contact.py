from flask import request, flash
from flask_wtf import FlaskForm
from wtforms import TextField, IntegerField, TextAreaField, SubmitField, RadioField, SelectField
from wtforms import validators, ValidationError

from key import G_USER, G_PASS

class ContactForm(FlaskForm):
   message = TextAreaField("message")
   submit = SubmitField("send")

def send_email(user, pwd, recipient, subject, body):
    import smtplib

    gmail_user = user
    gmail_pwd = pwd
    FROM = user
    TO = recipient if type(recipient) is list else [recipient]
    SUBJECT = subject
    TEXT = body

    # Prepare actual message
    message = """From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
  # try:
    # SMTP_SSL Example
    server_ssl = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server_ssl.ehlo()
    server_ssl.login(gmail_user, gmail_pwd)
    server_ssl.sendmail(FROM, TO, message)
    server_ssl.close()
    print ('successfully sent the mail')
  # except:
  #     print ("failed to send mail")

def SendMessage(message):
  send_email(G_USER, G_PASS, G_USER, "Website Contact Form", message)