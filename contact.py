from flask import request, flash
from flask_wtf import FlaskForm
from wtforms import TextField, IntegerField, TextAreaField, SubmitField, RadioField, SelectField
from wtforms import validators, ValidationError

class ContactForm(FlaskForm):
   message = TextAreaField("message")
   submit = SubmitField("send")