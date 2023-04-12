from flask_app import app
from flask import render_template, redirect, request, flash, session

@app.route('/games_homepage')
def games_homepage():
    return render_template('python_games.html')