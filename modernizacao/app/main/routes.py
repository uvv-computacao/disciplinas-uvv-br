from flask import render_template

from app.main import bp
from app.models import Disciplina


@bp.route("/")
def index():
    disciplinas = Disciplina.query.order_by(Disciplina.nome).all()
    return render_template("index.html", disciplinas=disciplinas)
