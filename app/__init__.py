from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options


bootstrap = Bootstrap()

def create_app(config_name):
    #Initialization
    app = Flask(__name__)

    # Creating app configurations
    app.config.from_object(config_options[config_name])

    #Initialize the flask extension
    bootstrap.init_app(app)

    # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    #Setting up config
    from .request import configure_request
    configure_request(app) 

    return app