from flask import Flask, render_template, url_for, flash, redirect
from forms import SignUpForm, LogInForm
import os

# os.system('pyductivity.py')

app = Flask(__name__)

app.config['SECRET_KEY'] = 'd5f022697fb22f41fb41d0d4873bedbbd5a6e6489d3e9f581552c9eefdeae7a5'

if __name__ == '__main__':
    app.run(debug=True)


@app.route('/')
def landing():
    return render_template('landing.html')


@app.route('/input')
def input():
    return render_template('input.html')


# @app.route('/category_input')
# def category_input():
#     return render_template('landing.html')
#
#
# @app.route('/activity_input')
# def activity_input():
#     return render_template('landing.html')
#
#
# @app.route('/logged_in_landing')
# def logged_in_landing():
#     return render_template('landing.html')
#
#
# @app.route('/result')
# def result():
#     return render_template('landing.html')
#
#
# @app.route('/my_data')
# def my_data():
#     return render_template('landing.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignUpForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'Success!')
        return redirect(url_for('landing'))
    return render_template('signup.html', title='Sign Up', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LogInForm()
    if form.validate_on_submit():
        # flash(f'Account created for {form.username.data}!', 'Success!')
        return redirect(url_for('landing'))
    else:
        flash('Log in unsuccessful, please check username and password')
    return render_template('login.html', title='Log In', form=form)
