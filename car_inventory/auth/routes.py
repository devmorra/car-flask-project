from flask import Blueprint, render_template

"""
    Note that in the below code,
    some arguments are specified when creating Blueprint objects.
    The first argument, 'site' is the Blueprint's name.
    which flask uses for routing.

    The second argument, __name__, is the Blueprint's import name,
    which flask uses to locate the Blueprint's resources
"""

auth = Blueprint('auth', __name__, template_folder='auth_templates')

@auth.route('/signin', methods=['GET', 'POST'])
def signin():
    return render_template('signin.html')

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    return render_template('signup.html')
