from datetime import datetime, timezone

from flask import render_template, url_for

from app.extensions import db
from app.main import bp
from app.models import (
    Atividade,
    Aula,
    Aviso,
    Disciplina,
    DisciplinaTurma,
    Recurso,
    RecursoVinculo,
    Semana,
    Turma,
)


def _get_oferta_or_404(disciplina_slug, turma_slug):
    disciplina = Disciplina.query.filter_by(slug=disciplina_slug).first_or_404()
    turma = Turma.query.filter_by(slug=turma_slug).first_or_404()
    oferta = DisciplinaTurma.query.filter_by(
        disciplina_id=disciplina.id, turma_id=turma.id
    ).first_or_404()
    return disciplina, turma, oferta


def _oferta_breadcrumb(disciplina, turma, extra=None):
    """Trilha de breadcrumb comum a toda página de uma oferta (disciplina +
    turma). Quando `extra` é informado, o nível da turma vira um link para a
    home da oferta em vez de ser o último item da trilha."""
    turma_url = (
        url_for("main.oferta_dashboard", disciplina_slug=disciplina.slug, turma_slug=turma.slug)
        if extra
        else None
    )
    items = [
        ("Disciplinas", url_for("main.disciplinas")),
        (
            disciplina.nome,
            url_for("main.disciplina_detail", disciplina_slug=disciplina.slug),
        ),
        (turma.apelido, turma_url),
    ]
    if extra:
        items.extend(extra)
    return items


@bp.route("/")
def index():
    disciplinas = (
        Disciplina.query.filter_by(ativa=True).order_by(Disciplina.nome).all()
    )
    agora = datetime.now(timezone.utc)

    proximos_prazos = (
        Atividade.query.join(
            DisciplinaTurma, Atividade.disciplina_turma_id == DisciplinaTurma.id
        )
        .join(Disciplina, DisciplinaTurma.disciplina_id == Disciplina.id)
        .filter(
            Disciplina.ativa.is_(True),
            Atividade.data_publicacao <= agora,
            db.or_(Atividade.prazo.is_(None), Atividade.prazo >= agora),
        )
        .order_by(Atividade.prazo.asc().nulls_last())
        .limit(8)
        .all()
    )
    avisos_recentes = (
        Aviso.query.join(Disciplina, Aviso.disciplina_id == Disciplina.id)
        .filter(Disciplina.ativa.is_(True), Aviso.data_publicacao <= agora)
        .order_by(Aviso.data_publicacao.desc())
        .limit(8)
        .all()
    )

    return render_template(
        "index.html",
        disciplinas=disciplinas,
        proximos_prazos=proximos_prazos,
        avisos_recentes=avisos_recentes,
        nav_active="inicio",
    )


@bp.route("/disciplinas/")
def disciplinas():
    todas = Disciplina.query.order_by(Disciplina.nome).all()
    return render_template(
        "disciplinas.html", disciplinas=todas, nav_active="disciplinas"
    )


@bp.route("/disciplinas/<disciplina_slug>/")
def disciplina_detail(disciplina_slug):
    disciplina = Disciplina.query.filter_by(slug=disciplina_slug).first_or_404()
    ofertas = sorted(
        disciplina.turma_vinculos,
        key=lambda vinculo: (vinculo.turma.ano, vinculo.turma.semestre),
        reverse=True,
    )
    periodo_atual = (ofertas[0].turma.ano, ofertas[0].turma.semestre) if ofertas else None
    ofertas_atuais = [
        v for v in ofertas if (v.turma.ano, v.turma.semestre) == periodo_atual
    ]
    ofertas_anteriores = [
        v for v in ofertas if (v.turma.ano, v.turma.semestre) != periodo_atual
    ]
    return render_template(
        "disciplina_detail.html",
        disciplina=disciplina,
        ofertas_atuais=ofertas_atuais,
        ofertas_anteriores=ofertas_anteriores,
        nav_active="disciplinas",
    )


@bp.route("/disciplinas/<disciplina_slug>/<turma_slug>/")
def oferta_dashboard(disciplina_slug, turma_slug):
    disciplina, turma, oferta = _get_oferta_or_404(disciplina_slug, turma_slug)
    agora = datetime.now(timezone.utc)

    semana_atual = (
        Semana.query.filter_by(disciplina_turma_id=oferta.id)
        .order_by(Semana.numero.desc())
        .first()
    )
    proximos_prazos = (
        Atividade.query.filter(
            Atividade.disciplina_turma_id == oferta.id,
            Atividade.data_publicacao <= agora,
            db.or_(Atividade.prazo.is_(None), Atividade.prazo >= agora),
        )
        .order_by(Atividade.prazo.asc().nulls_last())
        .limit(5)
        .all()
    )
    avisos = (
        Aviso.query.filter(
            Aviso.disciplina_id == disciplina.id,
            db.or_(Aviso.turma_id.is_(None), Aviso.turma_id == turma.id),
            Aviso.data_publicacao <= agora,
        )
        .order_by(Aviso.data_publicacao.desc())
        .limit(5)
        .all()
    )

    return render_template(
        "oferta_dashboard.html",
        disciplina=disciplina,
        turma=turma,
        oferta=oferta,
        semana_atual=semana_atual,
        proximos_prazos=proximos_prazos,
        avisos=avisos,
        agora=agora,
        nav_active="disciplinas",
        course_nav_active="inicio",
        breadcrumb_items=_oferta_breadcrumb(disciplina, turma),
    )


@bp.route("/disciplinas/<disciplina_slug>/<turma_slug>/cronograma/")
def oferta_cronograma(disciplina_slug, turma_slug):
    disciplina, turma, oferta = _get_oferta_or_404(disciplina_slug, turma_slug)
    semanas = (
        Semana.query.filter_by(disciplina_turma_id=oferta.id)
        .order_by(Semana.numero)
        .all()
    )
    return render_template(
        "oferta_cronograma.html",
        disciplina=disciplina,
        turma=turma,
        oferta=oferta,
        semanas=semanas,
        nav_active="disciplinas",
        course_nav_active="cronograma",
        compact_header=True,
        breadcrumb_items=_oferta_breadcrumb(disciplina, turma, extra=[("Cronograma", None)]),
    )


@bp.route("/disciplinas/<disciplina_slug>/<turma_slug>/semanas/<int:numero>/")
def oferta_semana(disciplina_slug, turma_slug, numero):
    disciplina, turma, oferta = _get_oferta_or_404(disciplina_slug, turma_slug)
    semana = Semana.query.filter_by(
        disciplina_turma_id=oferta.id, numero=numero
    ).first_or_404()
    atividades = (
        Atividade.query.join(Aula, Atividade.aula_id == Aula.id)
        .filter(Aula.semana_id == semana.id)
        .order_by(Atividade.categoria, Atividade.numero)
        .all()
    )
    return render_template(
        "oferta_semana.html",
        disciplina=disciplina,
        turma=turma,
        oferta=oferta,
        semana=semana,
        atividades=atividades,
        nav_active="disciplinas",
        course_nav_active="cronograma",
        compact_header=True,
        breadcrumb_items=_oferta_breadcrumb(
            disciplina,
            turma,
            extra=[
                (
                    "Cronograma",
                    url_for(
                        "main.oferta_cronograma",
                        disciplina_slug=disciplina.slug,
                        turma_slug=turma.slug,
                    ),
                ),
                (f"Semana {semana.numero}", None),
            ],
        ),
    )


@bp.route("/disciplinas/<disciplina_slug>/<turma_slug>/atividades/")
def oferta_atividades(disciplina_slug, turma_slug):
    disciplina, turma, oferta = _get_oferta_or_404(disciplina_slug, turma_slug)
    agora = datetime.now(timezone.utc)
    atividades = (
        Atividade.query.filter(
            Atividade.disciplina_turma_id == oferta.id,
            Atividade.data_publicacao <= agora,
        )
        .order_by(Atividade.data_publicacao.desc())
        .all()
    )
    return render_template(
        "oferta_atividades.html",
        disciplina=disciplina,
        turma=turma,
        oferta=oferta,
        atividades=atividades,
        agora=agora,
        nav_active="disciplinas",
        course_nav_active="atividades",
        compact_header=True,
        breadcrumb_items=_oferta_breadcrumb(disciplina, turma, extra=[("Atividades", None)]),
    )


@bp.route("/disciplinas/<disciplina_slug>/<turma_slug>/avisos/")
def oferta_avisos(disciplina_slug, turma_slug):
    disciplina, turma, oferta = _get_oferta_or_404(disciplina_slug, turma_slug)
    agora = datetime.now(timezone.utc)
    avisos = (
        Aviso.query.filter(
            Aviso.disciplina_id == disciplina.id,
            db.or_(Aviso.turma_id.is_(None), Aviso.turma_id == turma.id),
            Aviso.data_publicacao <= agora,
        )
        .order_by(Aviso.data_publicacao.desc())
        .all()
    )
    return render_template(
        "oferta_avisos.html",
        disciplina=disciplina,
        turma=turma,
        oferta=oferta,
        avisos=avisos,
        nav_active="disciplinas",
        course_nav_active="avisos",
        compact_header=True,
        breadcrumb_items=_oferta_breadcrumb(disciplina, turma, extra=[("Avisos", None)]),
    )


@bp.route("/disciplinas/<disciplina_slug>/<turma_slug>/recursos/")
def oferta_recursos(disciplina_slug, turma_slug):
    disciplina, turma, oferta = _get_oferta_or_404(disciplina_slug, turma_slug)
    vinculos = (
        RecursoVinculo.query.filter(
            RecursoVinculo.disciplina_id == disciplina.id,
            db.or_(
                RecursoVinculo.turma_id.is_(None), RecursoVinculo.turma_id == turma.id
            ),
        )
        .join(Recurso)
        .order_by(Recurso.titulo)
        .all()
    )
    vinculos_especificos = [v for v in vinculos if not v.recurso.geral]
    vinculos_gerais = [v for v in vinculos if v.recurso.geral]
    return render_template(
        "oferta_recursos.html",
        disciplina=disciplina,
        turma=turma,
        oferta=oferta,
        vinculos_especificos=vinculos_especificos,
        vinculos_gerais=vinculos_gerais,
        nav_active="disciplinas",
        course_nav_active="recursos",
        compact_header=True,
        breadcrumb_items=_oferta_breadcrumb(disciplina, turma, extra=[("Recursos", None)]),
    )


@bp.route("/calendario/")
def calendario():
    return render_template(
        "stub.html", titulo="Calendário", nav_active="calendario"
    )


@bp.route("/recursos/")
def recursos_globais():
    recursos = (
        Recurso.query.filter_by(geral=True).order_by(Recurso.titulo).all()
    )
    return render_template(
        "recursos_globais.html", recursos=recursos, nav_active="recursos"
    )


@bp.route("/recursos/<slug>/")
def recurso_detail(slug):
    recurso = Recurso.query.filter_by(slug=slug).first_or_404()
    return render_template(
        "recurso_detail.html", recurso=recurso, nav_active="recursos"
    )


@bp.route("/arquivo/")
def arquivo():
    return render_template("stub.html", titulo="Arquivo", nav_active="arquivo")


@bp.route("/sobre/")
def sobre():
    return render_template("stub.html", titulo="Sobre", nav_active="sobre")
