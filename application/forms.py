from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import InputRequired, NumberRange

class Farmform(FlaskForm):
    name = StringField("What is your name?", validators=[InputRequired()]) 
    farm = StringField("What is the name of your farm?", validators=[InputRequired()])
    age = StringField("How old are you?", validators=[InputRequired()])
    equipment = StringField("What equipments are you selling or renting? Separate with a comma, thank you.", validators=[InputRequired()])
    equipmenttype = StringField("What type of equipment are these? Separate with a comma, thank you.", validators=[InputRequired()])
    vegetables = StringField("What vegetables do you sell? Separate with a comma, thank you.", validators=[InputRequired()])
    vegenum = IntegerField("How many of these vegetables are you selling? Separate with a comma, thank you.", validators=[InputRequired()])
    fruits = StringField("What fruits do you sell? Separate with a comma, thank you.", validators=[InputRequired()])
    fruitnum = IntegerField("How many of these vegetables are you selling? Separate with a comma, thank you.", validators=[InputRequired()])
    submit = SubmitField("Submit")