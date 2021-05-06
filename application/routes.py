from application import app, db
from application.models import Tasks
from flask import render_template, flash, redirect, url_for, request
from application.forms import TaskForm, UpdateForm

@app.route('/')
def home():
    all_tasks = Tasks.query.all()
    completed_list = []
    incompleted_list = []

    for task in all_tasks:
        if task.status == 'incompleted':
            if task.description == '':
                task.description = 'No Description'
                incompleted_list.append(str(task.date_created)[:11] + ' --- ' + task.title.title() + ' --- ' + task.description)
        else:
            if task.description == '':
                task.description = 'No Description'
                completed_list.append(str(task.date_created)[:11] + ' --- ' + task.title.title() + ' --- ' + task.description)

    if len(completed_list) == 0:
        completed_list.append('No completed tasks.')

    if len(incompleted_list) == 0:
        incompleted_list.append('No incompleted tasks.')

    return render_template('index.html', title='Homepage', incompleted_list=incompleted_list, completed_list=completed_list)

@app.route('/add', methods=['GET', 'POST'])
def add():
    form = TaskForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            new_task = Tasks(title=form.task.data, description=form.description.data, status=form.status.data)
            db.session.add(new_task)
            db.session.commit()
            flash(f'Added new task "{form.task.data}".')
            return redirect(url_for('home'))
    return render_template('add_task.html', title='Add Task', form=form)

@app.route('/update', methods=['GET', 'POST'])
def update_task():
    form = UpdateForm()
    all_tasks = Tasks.query.all()

    for task in all_tasks:
        form.task.choices.append((task.id, f'{task.title}'))

    if request.method == 'POST':
        selected_task_id = form.task.data
        update_task = Tasks.query.filter_by(id=selected_task).first()
        if form.validate_on_submit():
            if form.description.data != '':
                update_task.description = form.description.data
            
            if form.status.data != update_task.status:
                update_task.status = form.status.data

            db.session.commit()
            return redirect(url_for('home'))
            flash(f'Updated task "{form.task.data}"')

    return render_template('update_task.html', title='Update Task', form=form, all_tasks=all_tasks)

@app.route('/delete/<title>')
def delete(title):
    delete_task = Tasks.query.filter_by(title=title).first()
    db.session.delete(delete_task)
    db.session.commit()
    return f'Deleted task "{title.title()}".'
