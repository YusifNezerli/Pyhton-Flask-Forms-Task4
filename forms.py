from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import DataRequired, Length , Email


class ContactForm(FlaskForm):
    full_name = StringField(label='Full name', validators=[DataRequired(), Length(min=2, max=20)])
    email = EmailField(label='Your email address: ', validators=[DataRequired(), Email()])
    phone = IntegerField(label='Your phone', validators=[DataRequired()])
    comment = StringField(label='Your comment', validators=[DataRequired()])

class RecMovieFrom(FlaskForm):
    movie_name = StringField(label='Movie name: ', validators=[DataRequired(), Length(min=2, max=20)])
    producer = StringField(label='Producer: ', validators=[DataRequired()])
    year= IntegerField(label='Year: ', validators=[DataRequired()])
    your_point = IntegerField(label='Your point: ', validators=[DataRequired()])
