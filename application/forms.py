from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired


class TaskForm(FlaskForm):
    task = StringField("Task", validators=[DataRequired()])
    status = SelectField(
        "Status", choices=[("incompleted", "Incompleted"), ("completed", "Completed")]
    )
    submit = SubmitField("Add Task")


class UpdateTaskForm(FlaskForm):
    status = SelectField(
        "Status", choices=[("incompleted", "Incompleted"), ("completed", "Completed")]
    )
    update = SubmitField("Update Task")
