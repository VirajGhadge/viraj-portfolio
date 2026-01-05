# flask_app/__init__.py - PRODUCTION READY

import os
from flask import Flask
from dotenv import load_dotenv

# Load environment variables from .env OR platform env vars
load_dotenv()

def create_app():
    app = Flask(__name__)

    # NO FALLBACK - REQUIRE SECRET_KEY from environment
    secret_key = os.getenv('SECRET_KEY')
    if not secret_key:
        raise RuntimeError('SECRET_KEY environment variable is required for production!')
    
    app.config['SECRET_KEY'] = secret_key
    app.config['DEBUG'] = os.getenv('FLASK_DEBUG', 'False').lower() == 'true'
    
    # Register blueprints
    from flask_app.routes import main_bp
    app.register_blueprint(main_bp)

    return app
