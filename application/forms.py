from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired

class TaskForm(FlaskForm):
    task = StringField('Task', validators=[DataRequired()])
    description = StringField('Description')
    status = SelectField('Status', choices=[('incompleted', 'Incompleted'), ('completed', 'Completed')])
    submit = SubmitField('Add task')

class UpdateForm(FlaskForm):
    task = StringField('Task', validators=[DataRequired()])
    description = StringField('Description')
    status = SelectField('Status', choices=[('incompleted', 'Incompleted'), ('completed', 'Completed')])
    update = SubmitField('Update task')