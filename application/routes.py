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
    return f'Added a new task - "{title}".'

@app.route('/read')
def read():
    all_tasks = Tasks.query.all()
    task_list = ''
    for task in all_tasks:
        if task.status == True:
            task_status = 'Completed'
        elif task.status == False:
            task_status = 'To be completed'
        task_list += task.title.title() + ' - ' + str(task.description) + ' - ' + task_status + '<br>'
    return task_list

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
        print(update_task.status)
        db.session.commit()
    return f'Modified "{update}" of task "{title.title()}" to "{value}".'

@app.route('/delete/<title>')
def delete(title):
    delete_task = Tasks.query.filter_by(title=title).first()
    db.session.delete(delete_task)
    db.session.commit()
    return f'Deleted task "{title.title()}".'
