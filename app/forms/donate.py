from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class DonateColorNicknameForm(FlaskForm):
    nickname = StringField("Ваш никнейм в игре", validators=[DataRequired()])
    color = StringField(default="#FFFFFF", validators=[DataRequired()])
    submit = SubmitField("Готово")
