from flask import Flask
from .config import DevConfig
from flask_bootstrap import Bootstrap



#Initialization
app = Flask(__name__,instance_relative_config=True)

#Setting up new configuration
app.config.from_object(DevConfig)
app.config.from_pyfile('config.py')

#Initialize the Bootstrap extension
bootstrap = Bootstrap(app)


from app import views
from app import errors