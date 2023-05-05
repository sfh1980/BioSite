from flask_app import app
from flask import render_template, redirect, request, flash, session




@app.route('/games_homepage')
def games_homepage():
    return render_template('python_games.html')

@app.route('/guess_the_number')
def guess_the_number():
    return render_template('guess_the_number.html')