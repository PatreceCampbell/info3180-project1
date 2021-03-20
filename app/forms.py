from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, IntegerField, SelectField, TextAreaField, FileField, DecimalField
from wtforms.validators import DataRequired, Email, Optional

class PropForm(FlaskForm):
    title = StringField('Property Title', validators=[DataRequired()])
    bedrooms = IntegerField("No. of Rooms", validators=[DataRequired()])
    bathrooms = DecimalField("No. of Bathrooms", validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired()])
    price = IntegerField('Price', validators=[DataRequired()])
    option = SelectField('Property Type', choices = [('House'), ('Apartment')], validators=[Optional()])
    description = TextAreaField('Description', validators=[DataRequired()])
    photo = FileField('Photo', validators=[FileRequired(), FileAllowed(['jpg', 'png', 'Photos only!'])])