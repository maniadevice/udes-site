from flask import current_app, Blueprint, render_template, redirect, url_for, request, session

main_app = Blueprint('main_app', __name__, template_folder='templates')

@main_app.route('/')
def home():
    return render_template('home.html')


@main_app.route('/history')
def history():
    return render_template('history.html')


@main_app.route('/donate')
def donate():
    return render_template('donate.html')


@main_app.route('/project-aims')
def aims():
    return render_template('project-aims.html')