from flask import Flask

from app.extensions import db, migrate
from config import Config


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)

    from app import models  # noqa: F401 — garante que os models sejam registrados

    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    from app.cli import seed_command
    app.cli.add_command(seed_command)

    return app
