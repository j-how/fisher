from wtforms import Form, StringField, IntegerField
from wtforms.validators import Length, NumberRange, DataRequired


class SearchForm(Form):
    p = StringField(validators=[DataRequired(message='内容不能为空'), Length(min=1, max=30, message='长度必须大于1')])
    page = IntegerField(validators=[NumberRange(min=1, max=30)], default=1)
