# this handles CURD

from flask import Blueprint, render_template, url_for

main = Blueprint('main', __name__)

# home page
@main.route('/')
def index():
    return render_template('index.html')

# profile page
@main.route('/profile')
def profile():
    return render_template('profile.html')