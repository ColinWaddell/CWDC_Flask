from flask import request, flash
from flask_wtf import FlaskForm
from wtforms import TextField, IntegerField, TextAreaField, SubmitField, RadioField, SelectField
from wtforms import validators, ValidationError

from email.mime.text import MIMEText
from subprocess import Popen, PIPE

class ContactForm(FlaskForm):
   message = TextAreaField("message")
   submit = SubmitField("send")

def SendMessage(message):
    msg = MIMEText(message)
    msg["From"] = "mrcolin+server@gmail.com"
    msg["To"] = "mrcolin+server@gmail.com"
    msg["Subject"] = "WEBSITE CONTACT FORM"
    p = Popen(["/usr/sbin/sendmail", "-t", "-oi", "-f", "mrcolin@colinwaddell.com"], stdin=PIPE)
    p.communicate(msg.as_bytes())
