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

    from app.main.course_colors import course_color
    app.jinja_env.globals["course_color"] = course_color

    from app.main.display import (
        categoria_label,
        data_curta,
        dia_semana_label,
        numero_padded,
        professor_responsavel,
    )
    app.jinja_env.globals["dia_semana_label"] = dia_semana_label
    app.jinja_env.globals["data_curta"] = data_curta
    app.jinja_env.globals["categoria_label"] = categoria_label
    app.jinja_env.globals["numero_padded"] = numero_padded
    app.jinja_env.globals["professor_responsavel"] = professor_responsavel

    return app
