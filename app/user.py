from flask import (
    Blueprint, 
    flash, 
    g, 
    render_template, 
    request, 
    url_for, 
    session, 
    redirect
)
import functools

from models.modelUser import User
from utils.db import db

from werkzeug.security import check_password_hash, generate_password_hash
from werkzeug.utils import redirect 

userBp = Blueprint('user', __name__, url_prefix='/user')

# Register in the application
@userBp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        error = None

        user = User.query.filter_by(username=username).first()

        if user is None:
            user = User(username, email, generate_password_hash(password))
            db.session.add(user)
            db.session.commit()

            return redirect(url_for('user.login'))

        else:
            error = "Please, enter another user."
            
            flash(error)

    return render_template('user/register.html')


# User login
@userBp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = str(request.form['username'])
        password = request.form['password']

        error = None

        user = User.query.filter_by(username=username).first()

        # Check if the entered user exists.
        if user is None:
            error = "Wrong Username or Password."

        elif not check_password_hash(user.password, password):
            error = "Wrong Username or Password."
        
        elif error is None:

            session.clear()

            session["username"] = user.username
            session["id"] = user.userid
            session["logged_in"] = True
            # g.user = user

            return redirect(url_for('todo.listToDo'))
        
        flash(error)

    return render_template('user/login.html')

# Check if the user is logged in
@userBp.before_app_request
def load_logged_in_user():
    user_id = session.get('id')
    if user_id is None:
        g.user = None
    else:
        g.user = User.query.get_or_404(user_id)


# Check if user is needed to access routes
def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('user.login'))
        return view(**kwargs)
    return wrapped_view

# Logout user
@userBp.route('/logout')
def logout():
    session.clear()
    g.user = None
    return redirect(url_for('index'))
