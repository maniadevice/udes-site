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

@main_app.route('/contact')
def contact():
    return render_template('contact.html')

@main_app.route('/ramadan-2019')
def ramadan_2019():
    return render_template('/ramadan-2019.html')

@main_app.route('/bakrid-2019')
def bakrid_2019():
    return render_template('/bakrid-2019.html')

@main_app.route('/water-pump-2019')
def water_pump_2019():
    return render_template('/water-pump-2019.html')

@main_app.route('/masjid-2019')
def masjid_2019():
    return render_template('/mosque-2019.html')

@main_app.route('/accreditation')
def accreditation():
    return render_template('accreditation.html')