from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options

bootstrap = Bootstrap()


def create_app(config_name):
    app = Flask(__name__)
#app = Flask(__name__,instance_relative_config = True)


#We pass in instance_relative_config which allow us to connect to the instance/folder when the app instance is created.
# app.config.from_pyfile('config.py') connects to the config.py file and all its contents are appended to the app.config
#Setting up configuration
    # create the app configurations
    app.config.from_object(config_options[config_name])

    # Initializing flask extensions
    bootstrap.init_app(app)

    # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # setting config
    from .requests import configure_request
    configure_request(app)

    return app
