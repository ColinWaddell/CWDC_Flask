''' Contact forms and email scripts '''

from subprocess import Popen, PIPE
from email.mime.text import MIMEText
from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField


class ContactForm(FlaskForm):
    ''' Very basic contact form '''
    message = TextAreaField("message", default="Please include your contact details.")
    submit = SubmitField("send")


def send_message(message, email_from, email_to, subject):
    ''' send an email via sendmail '''
    msg = MIMEText(message)
    msg["From"] = email_from
    msg["To"] = email_to
    msg["Subject"] = subject
    email = Popen([
        "/usr/sbin/sendmail",
        "-t", "-oi", "-f",
        "mrcolin@colinwaddell.com"],
        stdin=PIPE
    )
    email.communicate(msg.as_bytes())
