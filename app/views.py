from flask import render_template
from app import app

@app.route('/')
def index():
    '''
    Function that returns the index page & its data
    '''
    return render_template('index.html')