from application import app, db
from application.models import Tasks

@app.route('/')
def home():
    return '<h1>Welcome to the To-do-app homepage!</h1>'

@app.route('/add/<title>')
def add(title):
    new_task = Tasks(title=title)
    db.session.add(new_task)
    db.session.commit()
    return f'Added a new task - {title}.'

@app.route('/read')
def read():
    all_tasks = Tasks.query.all()
    task_list = ''
    for task in all_tasks:
        task_list += task.title + ' - ' + task.description + '<br>'
    return task_list

@app.route('/update/<title>:<description>')
def update(title, description):
    update_task = Tasks.query.filter_by(title=title).first()
    update_task.description = description
    db.session.commit()
    return f'Added description to task {title}.'

@app.route('/delete/<title>')
def delete(title):
    delete_task = Tasks.query.filter_by(title=title).first()
    db.session.delete(delete_task)
    db.session.commit()
    return f'Deleted task {title}.'
