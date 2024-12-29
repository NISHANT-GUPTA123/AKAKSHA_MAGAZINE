# __init__.py
from flask import Flask
from flask_login import LoginManager
from config import Config
from database import init_app

login_manager = LoginManager()

def create_app(config_class=Config):
    app = Flask(__name__, static_url_path='/static')
    app.config.from_object(config_class)
    
    # Initialize extensions
    init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'
    
    # Register blueprints here (if using)
    
    return app