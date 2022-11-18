from flask_wtf import FlaskForm
from wtforms import StringField, validators, SubmitField

class ContactForm(Form):
    name = StringField('Your name', [
        validators.Length(min=4, message=_("Could you give us a little more to work on?" )),
        validators.Length(max=120, message_=("A bit much, don\'t you think?")),
        ])
    email = StringField('Your email', [
        validators.Length(min=6, message=_("Little short for an email address, no??")),
        validators.Length(max=120, message_=("A bit much, don\'t you think?")),
        validators.Email(message=_("That doesn\'t look like a valid email address.")),
        ])
    subject = StringField('How can we help?', [
        validators.Length(max=2900, message_=("There's a lot here so I recommend we move this to email. Leave a short message and we'll reach out.")),
        validators.Length(min=4, message=_("Could you give us a little more to go on" )),
    ])
    submit = SubmitField("Send")