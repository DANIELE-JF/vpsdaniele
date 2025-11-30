from flask import Flask
from app.extensions import db, login_manager, migrate
from configs import Config

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    # Initialize extensions
    db.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app, db)
    
    # Register blueprints
    from app.routes.auth_bp import auth_bp
    from app.routes.main_bp import main_bp
    from app.routes.users import users_bp
    
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(main_bp)
    app.register_blueprint(users_bp, url_prefix='/users')
    
    return app

