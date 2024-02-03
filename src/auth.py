from flask import Blueprint, render_template, url_for

auth = Blueprint('auth', __name__)

@auth.route('/signup')
def signup():
    return render_template('signup.html')

@auth.route('/login')
def login():
    return " This page for log in users"

@auth.route('/logout')
def logout():
    return " This page for log out users"