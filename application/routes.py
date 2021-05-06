from application import app, db
from application.models import Tasks
from flask import render_template, redirect, request, url_for
from application.forms import TaskForm, UpdateTaskForm


@app.route("/", methods=["GET"])
def home():
    all_tasks = Tasks.query.all()
    incompleted_tasks = []
    completed_tasks = []

    for task in all_tasks:
        if task.status == "incompleted":
            incompleted_tasks.append(task)
        else:
            completed_tasks.append(task)

    return render_template(
        "index.html",
        title="Homepage",
        all_tasks=all_tasks,
        incompleted_tasks=incompleted_tasks,
        completed_tasks=completed_tasks,
    )


@app.route("/add", methods=["GET", "POST"])
def add():
    form = TaskForm()

    if request.method == "POST":
        if form.validate_on_submit():
            new_task = Tasks(task=form.task.data, status=form.status.data)
            db.session.add(new_task)
            db.session.commit()
            return redirect(url_for("home"))
    return render_template("add.html", title="Add Task", form=form)


@app.route("/update/<int:id>", methods=["GET", "POST"])
def update(id):
    form = UpdateTaskForm()

    if request.method == "POST":
        update_task = Tasks.query.filter_by(id=id).first()
        if form.validate_on_submit():
            update_task.status = form.status.data
            db.session.commit()
            return redirect(url_for("home"))
    return render_template(
        "update.html", title="Update Task", form=form, update_task=update_task
    )


@app.route("/completed/<int:id>", methods=["POST"])
def completed(id):
    task = Tasks.query.filter_by(id=id).first()
    task.status = "completed"
    db.session.commit()
    return redirect(url_for("home"))


@app.route("/incompleted/<int:id>", methods=["POST"])
def incompleted(id):
    task = Tasks.query.filter_by(id=id).first()
    task.status = "incompleted"
    db.session.commit()
    return redirect(url_for("home"))


@app.route("/delete/<int:id>", methods=["GET", "POST"])
def delete(id):
    delete_task = Tasks.query.filter_by(id=id).first()
    db.session.delete(delete_task)
    db.session.commit()
    return redirect(url_for("home"))
