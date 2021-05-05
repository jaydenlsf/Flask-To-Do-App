from application import app, db
from application.models import Tasks
from flask import render_template, flash, redirect
from application.forms import TaskForm, UpdateForm

@app.route('/')
def home():
    return render_template('index.html', title='Homepage')

@app.route('/add', methods=['GET', 'POST'])
def add():
    form = TaskForm()
    if form.validate_on_submit():
        flash(f'Added new task "{form.task.data}".')
        new_task = Tasks(title=form.task.data, description=form.description.data, status=form.status.data)
        print(form.status.data)
        db.session.add(new_task)
        db.session.commit()
        return redirect('/')
    return render_template('add_task.html', title='Add Task', form=form)

@app.route('/all')
def read():
    all_tasks = Tasks.query.all()
    task_list = []
    for task in all_tasks:
        if task.description == '':
            task.description = 'No Description'
        task_list.append(task.title.title() + ' --- ' + task.description + ' --- ' + task.status.title())
    return render_template('tasks.html', title='View tasks', task_list=task_list)

@app.route('/update/<title>:<update>:<value>')
def update_task(title, update, value):
    update_task = Tasks.query.filter_by(title=title).first()
    if update == 'description':
        update_task.description = value
        db.session.commit()
    elif update == 'status':
        if value.lower() == 'true':
            update_task.status = True
        elif value.lower() == 'false':
            update_task.status = False
        else:
            return 'Unable to update status.'
        db.session.commit()
    else:
        return 'Invalid entry.'
    return f'Modified "{update}" of task "{title.title()}" to "{value}".'

@app.route('/delete/<title>')
def delete(title):
    delete_task = Tasks.query.filter_by(title=title).first()
    db.session.delete(delete_task)
    db.session.commit()
    return f'Deleted task "{title.title()}".'
