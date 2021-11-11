from flask import Blueprint, render_template, request, jsonify
from flask_login import login_required
from ..api.routes import getMyCars
from ..forms import CarAddForm
from flask_login import login_user, logout_user, current_user, login_required
from car_inventory.models import db, User, Car, car_schema, cars_schema

"""
    Note that in the below code,
    some arguments are specified when creating Blueprint objects.
    The first argument, 'site' is the Blueprint's name.
    which flask uses for routing.

    The second argument, __name__, is the Blueprint's import name,
    which flask uses to locate the Blueprint's resources
"""

site = Blueprint('site', __name__, template_folder='site_templates')

@site.route('/')
def home():
    return render_template('index.html')

@site.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    form = CarAddForm()
    cars = getMyCars(current_user)
    try:
        if request.method == 'POST' and form.validate_on_submit():
            make = form.make.data
            model = form.model.data
            year = form.year.data
            topSpeed = form.topSpeed.data
            value = form.value.data
            mileage = form.mileage.data
            user_token = current_user.token
            car = Car(make, model, year, topSpeed, value, mileage, user_token)
            db.session.add(car)
            db.session.commit()
            return render_template('profile.html', cars=cars, form = form)
    except:
        raise Exception('Invalid Form Data: Please Check your form.')
    return render_template('profile.html', cars=cars, form = form)