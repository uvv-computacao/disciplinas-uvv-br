from datetime import datetime, time, timedelta, timezone

import click
from flask.cli import with_appcontext

from app.extensions import db
from app.models import (
    Atividade,
    AtividadeHistorico,
    Aula,
    Aviso,
    Disciplina,
    DisciplinaTurma,
    Horario,
    Monitor,
    Monitoria,
    Professor,
    ProfessorEmail,
    ProfessorTelefone,
    Recurso,
    RecursoVinculo,
    Regencia,
    Semana,
    Turma,
)


@click.command("seed")
@with_appcontext
def seed_command():
    """Popula o banco com dados de exemplo para desenvolvimento."""
    turmas_exemplo = [
        dict(slug="20251-cc6m", nome="Turma CC6M - 2025/1", apelido="CC6M",
             ano=2025, semestre=1, codigo="cc6m"),
        dict(slug="20251-cc5n", nome="Turma CC5N - 2025/1", apelido="CC5N",
             ano=2025, semestre=1, codigo="cc5n"),
        dict(slug="20251-cc5m", nome="Turma CC5M - 2025/1", apelido="CC5M",
             ano=2025, semestre=1, codigo="cc5m"),
    ]

    turmas_por_slug = {}
    for dados in turmas_exemplo:
        turma = Turma.query.filter_by(slug=dados["slug"]).first()
        if turma is None:
            turma = Turma(**dados)
            db.session.add(turma)
            db.session.flush()
        turmas_por_slug[turma.slug] = turma

    disciplinas_exemplo = [
        ("Estrutura de Dados II", "ED2", "ed2", ["20251-cc6m"]),
        ("Arquitetura de Computadores I", "ArqComp1", "arqcomp1", ["20251-cc6m"]),
        ("Banco de Dados I", "BD1", "bd1", ["20251-cc5n"]),
        ("Banco de Dados II", "BD2", "bd2", ["20251-cc5m", "20251-cc6m"]),
    ]

    disciplinas_por_slug = {}
    for nome, apelido, slug, slugs_turmas in disciplinas_exemplo:
        disciplina = Disciplina.query.filter_by(slug=slug).first()
        if disciplina is None:
            disciplina = Disciplina(nome=nome, apelido=apelido, slug=slug)
            db.session.add(disciplina)

        for slug_turma in slugs_turmas:
            turma = turmas_por_slug[slug_turma]
            if turma not in disciplina.turmas:
                disciplina.turmas.append(turma)

        disciplinas_por_slug[slug] = disciplina

    db.session.flush()

    professores_exemplo = [
        dict(
            slug="abrantes",
            apelido="Abrantes",
            biografia="Professor de Estrutura de Dados e Arquitetura de Computadores.",
            emails=["abrantes@uvv.br"],
            telefones=["(27) 99999-0001"],
        ),
        dict(
            slug="julio",
            apelido="Julio",
            biografia=None,
            emails=["julio@uvv.br"],
            telefones=[],
        ),
    ]

    professores_por_slug = {}
    for dados in professores_exemplo:
        professor = Professor.query.filter_by(slug=dados["slug"]).first()
        if professor is None:
            professor = Professor(
                slug=dados["slug"], apelido=dados["apelido"], biografia=dados["biografia"]
            )
            db.session.add(professor)
            db.session.flush()

            for email in dados["emails"]:
                professor.emails.append(ProfessorEmail(email=email))
            for telefone in dados["telefones"]:
                professor.telefones.append(ProfessorTelefone(telefone=telefone))

        professores_por_slug[professor.slug] = professor

    db.session.flush()

    def oferta(slug_disciplina, slug_turma):
        turma = turmas_por_slug[slug_turma]
        return DisciplinaTurma.query.filter_by(
            disciplina_id=disciplinas_por_slug[slug_disciplina].id, turma_id=turma.id
        ).first()

    regencias_exemplo = [
        ("ed2", "20251-cc6m", "abrantes", True),
        ("arqcomp1", "20251-cc6m", "abrantes", True),
        ("arqcomp1", "20251-cc6m", "julio", False),
        ("bd1", "20251-cc5n", "julio", True),
        ("bd2", "20251-cc5m", "julio", True),
        ("bd2", "20251-cc6m", "julio", True),
    ]

    for slug_disciplina, slug_turma, slug_professor, principal in regencias_exemplo:
        disciplina_turma = oferta(slug_disciplina, slug_turma)
        professor = professores_por_slug[slug_professor]
        existe = Regencia.query.filter_by(
            disciplina_turma_id=disciplina_turma.id, professor_id=professor.id
        ).first()
        if existe is None:
            db.session.add(
                Regencia(
                    disciplina_turma_id=disciplina_turma.id,
                    professor_id=professor.id,
                    principal=principal,
                )
            )

    monitores_exemplo = [
        dict(slug="rayssa", nome="Rayssa"),
        dict(slug="susilea", nome="Susilea"),
    ]

    monitores_por_slug = {}
    for dados in monitores_exemplo:
        monitor = Monitor.query.filter_by(slug=dados["slug"]).first()
        if monitor is None:
            monitor = Monitor(**dados)
            db.session.add(monitor)
            db.session.flush()
        monitores_por_slug[monitor.slug] = monitor

    monitorias_exemplo = [
        ("ed2", "20251-cc6m", "rayssa"),
        ("arqcomp1", "20251-cc6m", "rayssa"),
        ("ed2", "20251-cc6m", "susilea"),
        ("bd1", "20251-cc5n", "susilea"),
    ]

    for slug_disciplina, slug_turma, slug_monitor in monitorias_exemplo:
        disciplina_turma = oferta(slug_disciplina, slug_turma)
        monitor = monitores_por_slug[slug_monitor]
        existe = Monitoria.query.filter_by(
            disciplina_turma_id=disciplina_turma.id, monitor_id=monitor.id
        ).first()
        if existe is None:
            db.session.add(
                Monitoria(
                    disciplina_turma_id=disciplina_turma.id, monitor_id=monitor.id
                )
            )

    db.session.flush()

    julio = professores_por_slug["julio"]
    bd2 = disciplinas_por_slug["bd2"]
    turma_cc5m = turmas_por_slug["20251-cc5m"]
    turma_cc6m = turmas_por_slug["20251-cc6m"]
    agora = datetime.now(timezone.utc)

    avisos_exemplo = [
        # Específico da CC5M — só essa turma vê.
        dict(
            disciplina_id=bd2.id, turma_id=turma_cc5m.id, professor_id=julio.id,
            titulo="Avisos da 1ª Semana - CC5M",
            conteudo="Turma CC5M: comecem pela leitura do capítulo 1, seção 1.2.",
            data_publicacao=agora,
        ),
        # Específico da CC6M — conteúdo diferente, só essa turma vê.
        dict(
            disciplina_id=bd2.id, turma_id=turma_cc6m.id, professor_id=julio.id,
            titulo="Avisos da 1ª Semana - CC6M",
            conteudo="Turma CC6M: revisem o conteúdo de BD1 antes da próxima aula.",
            data_publicacao=agora,
        ),
        # Geral da disciplina (turma_id nulo) — vale para CC5M e CC6M ao mesmo tempo.
        dict(
            disciplina_id=bd2.id, turma_id=None, professor_id=julio.id,
            titulo="Prova final remarcada",
            conteudo="A prova final de BD2 foi remarcada para a última semana do semestre, valendo para todas as turmas.",
            data_publicacao=agora,
        ),
        # Agendado para o futuro — não deve aparecer como publicado ainda.
        dict(
            disciplina_id=bd2.id, turma_id=None, professor_id=julio.id,
            titulo="Aviso agendado de teste",
            conteudo="Este aviso é um exemplo de agendamento: só deve valer a partir da data de publicação.",
            data_publicacao=agora + timedelta(days=7),
        ),
    ]

    for dados in avisos_exemplo:
        existe = Aviso.query.filter_by(
            disciplina_id=dados["disciplina_id"],
            turma_id=dados["turma_id"],
            titulo=dados["titulo"],
        ).first()
        if existe is None:
            db.session.add(Aviso(**dados))

    horarios_exemplo = [
        # ED2/CC6M: 2 dias de aula teórica na semana (exemplo do enunciado).
        ("ed2", "20251-cc6m", "aula", "teorica", "terca", "19:10", "20:50", "(local a definir)"),
        ("ed2", "20251-cc6m", "aula", "teorica", "sexta", "07:15", "08:55", "(local a definir)"),
        # ED2/CC6M: 1 sessão de monitoria na semana.
        ("ed2", "20251-cc6m", "monitoria", None, "quarta", "14:00", "16:00", "Laboratório 1"),
        # ArqComp1/CC6M: 1 dia de aula teórica + 1 dia de aula de laboratório.
        ("arqcomp1", "20251-cc6m", "aula", "teorica", "segunda", "09:15", "10:55", None),
        ("arqcomp1", "20251-cc6m", "aula", "laboratorio", "sabado", "08:00", "09:40", "Laboratório 2"),
    ]

    def hora(texto):
        h, m = texto.split(":")
        return time(int(h), int(m))

    for slug_disciplina, slug_turma, categoria, tipo, dia, inicio, fim, local in horarios_exemplo:
        disciplina_turma = oferta(slug_disciplina, slug_turma)
        hora_inicio = hora(inicio)
        existe = Horario.query.filter_by(
            disciplina_turma_id=disciplina_turma.id,
            categoria=categoria,
            dia_semana=dia,
            hora_inicio=hora_inicio,
        ).first()
        if existe is None:
            db.session.add(
                Horario(
                    disciplina_turma_id=disciplina_turma.id,
                    categoria=categoria,
                    tipo=tipo,
                    dia_semana=dia,
                    hora_inicio=hora_inicio,
                    hora_fim=hora(fim),
                    local=local,
                )
            )

    recursos_exemplo = [
        dict(
            slug="slides-aula1-ed2-cc6m",
            titulo="Slides da Aula 1 - CC6M",
            descricao="Slides usados na aula introdutória, específicos da turma CC6M.",
            tipo="arquivo",
            caminho_arquivo="recursos/ed2/slides-aula1-cc6m.pdf",
            nome_arquivo="slides-aula1-cc6m.pdf",
            professor_slug="abrantes",
            geral=False,
            vinculos=[("ed2", "20251-cc6m")],
        ),
        dict(
            slug="livro-texto-bd1",
            titulo="Livro-texto (referência) - BD1",
            descricao="Livro-texto adotado, vale para todas as turmas de BD1.",
            tipo="link",
            url="https://example.org/livro-bd1",
            professor_slug="julio",
            geral=False,
            vinculos=[("bd1", None)],
        ),
        # Geral E vinculado: aparece tanto no catálogo /recursos/ quanto nas
        # páginas das disciplinas onde foi destacado.
        dict(
            slug="tutorial-git",
            titulo="Tutorial de Git",
            descricao="Tutorial geral, usado em várias disciplinas e turmas.",
            tipo="link",
            url="https://example.org/tutorial-git",
            professor_slug="abrantes",
            geral=True,
            vinculos=[("ed2", None), ("arqcomp1", None), ("bd2", "20251-cc6m")],
        ),
        # Geral SEM nenhum vínculo: não pertence a nenhuma disciplina
        # específica, só aparece no catálogo geral do site.
        dict(
            slug="calendario-academico-uvv",
            titulo="Calendário Acadêmico UVV",
            descricao="Calendário oficial da universidade, com feriados e datas de matrícula.",
            tipo="link",
            url="https://example.org/calendario-academico",
            professor_slug="abrantes",
            geral=True,
            vinculos=[],
        ),
        # Vinculado a várias disciplinas mas explicitamente NÃO geral: só
        # quem cursa essas disciplinas específicas precisa dele.
        dict(
            slug="tutorial-gdb-valgrind",
            titulo="Tutorial de GDB e Valgrind",
            descricao="Como depurar e detectar vazamentos de memória em programas C.",
            tipo="link",
            url="https://example.org/tutorial-gdb-valgrind",
            professor_slug="abrantes",
            geral=False,
            vinculos=[("ed2", None), ("arqcomp1", None)],
        ),
    ]

    for dados in recursos_exemplo:
        professor = professores_por_slug[dados["professor_slug"]]
        recurso = Recurso.query.filter_by(slug=dados["slug"]).first()
        if recurso is None:
            recurso = Recurso(
                professor_id=professor.id,
                slug=dados["slug"],
                titulo=dados["titulo"],
                descricao=dados["descricao"],
                tipo=dados["tipo"],
                caminho_arquivo=dados.get("caminho_arquivo"),
                nome_arquivo=dados.get("nome_arquivo"),
                url=dados.get("url"),
                geral=dados["geral"],
            )
            db.session.add(recurso)
            db.session.flush()

            for slug_disciplina, slug_turma in dados["vinculos"]:
                disciplina = disciplinas_por_slug[slug_disciplina]
                turma = turmas_por_slug[slug_turma] if slug_turma else None
                db.session.add(
                    RecursoVinculo(
                        recurso_id=recurso.id,
                        disciplina_id=disciplina.id,
                        turma_id=turma.id if turma else None,
                    )
                )

    arqcomp1_cc6m = oferta("arqcomp1", "20251-cc6m")

    semana1 = Semana.query.filter_by(
        disciplina_turma_id=arqcomp1_cc6m.id, numero=3
    ).first()
    if semana1 is None:
        semana1 = Semana(
            disciplina_turma_id=arqcomp1_cc6m.id,
            numero=3,
            titulo="Álgebra Booleana",
            objetivos="Ao final desta semana o estudante deverá ser capaz de simplificar "
            "expressões booleanas e projetar circuitos combinacionais simples.",
            antes_das_aulas="- Leitura 3.1\n- Vídeo 3.1\n- Exercício preparatório",
            depois_da_semana="Você deverá estar preparado para: portas → expressões → "
            "simplificação → circuitos combinacionais.",
        )
        db.session.add(semana1)
        db.session.flush()

    aula5 = Aula.query.filter_by(
        disciplina_turma_id=arqcomp1_cc6m.id, numero=5
    ).first()
    if aula5 is None:
        aula5 = Aula(
            semana_id=semana1.id,
            disciplina_turma_id=arqcomp1_cc6m.id,
            numero=5,
            titulo="Álgebra Booleana",
            objetivos="Operadores lógicos, propriedades e tabelas-verdade.",
            conteudo="Introdução às operações AND, OR, NOT e suas propriedades algébricas.",
            material="- Notas\n- Slides\n- Exemplos\n- Código",
        )
        db.session.add(aula5)

    aula6 = Aula.query.filter_by(
        disciplina_turma_id=arqcomp1_cc6m.id, numero=6
    ).first()
    if aula6 is None:
        aula6 = Aula(
            semana_id=semana1.id,
            disciplina_turma_id=arqcomp1_cc6m.id,
            numero=6,
            titulo="Simplificação de Expressões",
            objetivos="Aplicar as propriedades booleanas para simplificar expressões.",
            conteudo="Mapas de Karnaugh e simplificação algébrica.",
            material="- Notas\n- Slides\n- Exercícios",
        )
        db.session.add(aula6)

    db.session.flush()

    pset02 = Atividade.query.filter_by(
        disciplina_turma_id=arqcomp1_cc6m.id, categoria="pset", numero=2
    ).first()
    if pset02 is None:
        pset02 = Atividade(
            disciplina_turma_id=arqcomp1_cc6m.id,
            aula_id=aula6.id,
            categoria="pset",
            numero=2,
            titulo="Representação da Informação",
            data_publicacao=agora,
            prazo=agora + timedelta(days=10),
            objetivos="Praticar simplificação de expressões booleanas e projeto de "
            "circuitos combinacionais.",
            pre_requisitos="- Aula 05\n- Aula 06\n- seção 2.1 do livro",
            especificacao="Simplifique as expressões booleanas fornecidas e projete o "
            "circuito combinacional correspondente para cada uma.",
            o_que_entregar="Relatório em PDF com as simplificações e os diagramas de circuito.",
            como_entregar="Envio pelo formulário da disciplina.",
            criterios_avaliacao="Correção das simplificações (60%) e clareza dos "
            "diagramas (40%).",
        )
        db.session.add(pset02)
        db.session.flush()
        db.session.add(
            AtividadeHistorico(atividade_id=pset02.id, descricao="Publicado")
        )

    laboratorio04 = Atividade.query.filter_by(
        disciplina_turma_id=arqcomp1_cc6m.id, categoria="lab", numero=4
    ).first()
    if laboratorio04 is None:
        laboratorio04 = Atividade(
            disciplina_turma_id=arqcomp1_cc6m.id,
            aula_id=aula6.id,
            categoria="lab",
            numero=4,
            titulo="Circuitos Combinacionais",
            data_publicacao=agora,
            prazo=agora + timedelta(days=14),
            objetivos="Montar e testar um circuito combinacional simples em protoboard.",
            especificacao="Antes do laboratório: leitura da seção de portas lógicas TTL.\n"
            "Materiais: 74HC00, 74HC04, protoboard, fonte, multímetro.",
            como_executar="Siga o roteiro de montagem entregue em aula.",
            o_que_entregar="Relatório com os resultados esperados e obtidos.",
        )
        db.session.add(laboratorio04)

    db.session.commit()
    click.echo("Banco populado com dados de exemplo.")
