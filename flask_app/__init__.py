from flask import Flask, send_from_directory
import os


app = Flask(__name__)

@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)


app.secret_key = "shhhhhh"