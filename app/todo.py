from flask import (
    Blueprint, 
    flash, 
    render_template, 
    request, 
    url_for, 
    session, 
    redirect
)
from models.modelTodo import Todo
from utils.db import db

from time import strftime,gmtime
from user import login_required


toDoBp = Blueprint('todo', __name__, url_prefix='/todo')

# List all "To Do's"
@toDoBp.route('/listToDo', methods=['GET', 'POST'])
def listToDo():
    date = strftime("%Y-%m-%d", gmtime())
    
    todos = Todo.query.filter_by(created_by=session["id"]).all()

    return render_template('todo/tasks.html', todos=todos, date=date)

# Create "To Do"
@toDoBp.route('/createToDo', methods=['GET', 'POST'])
def createToDo():
    date = strftime("%Y-%m-%d", gmtime())

    if request.method == "POST":
        description = request.form['description']

        if description == "":
            return redirect(url_for('todo.listToDo'))

        user_id = session["id"]

        # set the date and time
        created_at = strftime("%Y-%m-%d %H:%M:%S", gmtime())

        todo = Todo(description, user_id, created_at, False)
        db.session.add(todo)
        db.session.commit()

        return redirect(url_for('todo.listToDo'))

    return render_template('todo/create.html', date=date)

# Update "to do"
@toDoBp.route('/<int:id>/updateToDo', methods=['GET', 'POST'])
@login_required
def updateToDo(id):
    
    todo = Todo.query.filter_by(taskId=id).first()

    if request.method == 'POST':

        error = None
        
        description = request.form['description']

        # Completed check box
        completed = True if request.form.get('completed') == 'on' else False

        if not description:
            error = "Description is required."

        elif error is not None:
            flash(error)

        else:
            # You can update description or/and the completed check box.
            todo.description = description
            todo.completed = completed
            db.session.commit()

            return redirect(url_for('todo.listToDo'))

    return render_template('todo/update.html', todo=todo)

# Delete "To Do"
@toDoBp.route('/<int:id>/deleteToDo', methods=['GET', 'POST'])
@login_required
def deleteToDo(id):
    todo = Todo.query.filter_by(taskId=id).first()
    db.session.delete(todo)
    db.session.commit()

    return redirect(url_for('todo.listToDo'))
