from flask import render_template
from app import app

@app.errorhandler(404)
def four_zero_four(error):
    '''
    A function to render a custom 404 error page
    '''
    return render_template('fourZeroFour.html'),404