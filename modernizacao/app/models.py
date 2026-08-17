from datetime import datetime, timezone

from sqlalchemy.ext.associationproxy import association_proxy

from app.extensions import db


class Disciplina(db.Model):
    __tablename__ = "disciplinas"
    __table_args__ = (
        db.CheckConstraint(
            "(ativa AND data_desativacao IS NULL) OR "
            "(NOT ativa AND data_desativacao IS NOT NULL)",
            name="ck_disciplina_ativa_data_desativacao",
        ),
        db.CheckConstraint(
            "(caminho_syllabus IS NULL AND nome_arquivo_syllabus IS NULL) OR "
            "(caminho_syllabus IS NOT NULL AND nome_arquivo_syllabus IS NOT NULL)",
            name="ck_disciplina_syllabus_campos_coerentes",
        ),
    )

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(120), nullable=False)
    apelido = db.Column(db.String(60), nullable=False)
    slug = db.Column(db.String(60), unique=True, nullable=False)
    ativa = db.Column(db.Boolean, nullable=False, default=True, server_default="true")
    data_desativacao = db.Column(db.Date, nullable=True)
    caminho_syllabus = db.Column(db.String(500), nullable=True)
    nome_arquivo_syllabus = db.Column(db.String(255), nullable=True)

    turma_vinculos = db.relationship(
        "DisciplinaTurma", back_populates="disciplina", cascade="all, delete-orphan"
    )
    turmas = association_proxy(
        "turma_vinculos", "turma", creator=lambda turma: DisciplinaTurma(turma=turma)
    )
    avisos = db.relationship(
        "Aviso", back_populates="disciplina", cascade="all, delete-orphan"
    )
    recurso_vinculos = db.relationship(
        "RecursoVinculo", back_populates="disciplina", cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"<Disciplina {self.slug}>"


class Turma(db.Model):
    __tablename__ = "turmas"
    __table_args__ = (db.UniqueConstraint("ano", "semestre", "codigo"),)

    id = db.Column(db.Integer, primary_key=True)
    slug = db.Column(db.String(60), unique=True, nullable=False)
    nome = db.Column(db.String(120), nullable=False)
    apelido = db.Column(db.String(60), nullable=False)
    ano = db.Column(db.Integer, nullable=False)
    semestre = db.Column(db.Integer, nullable=False)
    codigo = db.Column(db.String(30), nullable=False)

    disciplina_vinculos = db.relationship(
        "DisciplinaTurma", back_populates="turma", cascade="all, delete-orphan"
    )
    disciplinas = association_proxy(
        "disciplina_vinculos",
        "disciplina",
        creator=lambda disciplina: DisciplinaTurma(disciplina=disciplina),
    )
    avisos = db.relationship(
        "Aviso", back_populates="turma", cascade="all, delete-orphan"
    )
    recurso_vinculos = db.relationship(
        "RecursoVinculo", back_populates="turma", cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"<Turma {self.slug}>"


class DisciplinaTurma(db.Model):
    """Vínculo entre uma disciplina e uma turma que a cursa — é a esta
    combinação específica que professores (via Regencia) e monitores (via
    Monitoria) são atribuídos."""

    __tablename__ = "disciplina_turma"
    __table_args__ = (db.UniqueConstraint("disciplina_id", "turma_id"),)

    id = db.Column(db.Integer, primary_key=True)
    disciplina_id = db.Column(
        db.Integer, db.ForeignKey("disciplinas.id"), nullable=False
    )
    turma_id = db.Column(db.Integer, db.ForeignKey("turmas.id"), nullable=False)

    disciplina = db.relationship("Disciplina", back_populates="turma_vinculos")
    turma = db.relationship("Turma", back_populates="disciplina_vinculos")
    regencias = db.relationship(
        "Regencia", back_populates="disciplina_turma", cascade="all, delete-orphan"
    )
    monitorias = db.relationship(
        "Monitoria", back_populates="disciplina_turma", cascade="all, delete-orphan"
    )
    horarios = db.relationship(
        "Horario", back_populates="disciplina_turma", cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"<DisciplinaTurma disciplina_id={self.disciplina_id} turma_id={self.turma_id}>"


class Professor(db.Model):
    __tablename__ = "professores"

    id = db.Column(db.Integer, primary_key=True)
    slug = db.Column(db.String(60), unique=True, nullable=False)
    apelido = db.Column(db.String(60), nullable=False)
    biografia = db.Column(db.Text, nullable=True)
    foto = db.Column(db.String(255), nullable=True)

    emails = db.relationship(
        "ProfessorEmail", back_populates="professor", cascade="all, delete-orphan"
    )
    telefones = db.relationship(
        "ProfessorTelefone", back_populates="professor", cascade="all, delete-orphan"
    )
    regencias = db.relationship(
        "Regencia", back_populates="professor", cascade="all, delete-orphan"
    )
    avisos = db.relationship(
        "Aviso", back_populates="professor", cascade="all, delete-orphan"
    )
    recursos = db.relationship(
        "Recurso", back_populates="professor", cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"<Professor {self.slug}>"


class ProfessorEmail(db.Model):
    __tablename__ = "professor_emails"
    __table_args__ = (db.UniqueConstraint("professor_id", "email"),)

    id = db.Column(db.Integer, primary_key=True)
    professor_id = db.Column(
        db.Integer, db.ForeignKey("professores.id"), nullable=False
    )
    email = db.Column(db.String(255), nullable=False)

    professor = db.relationship("Professor", back_populates="emails")

    def __repr__(self):
        return f"<ProfessorEmail {self.email}>"


class ProfessorTelefone(db.Model):
    __tablename__ = "professor_telefones"
    __table_args__ = (db.UniqueConstraint("professor_id", "telefone"),)

    id = db.Column(db.Integer, primary_key=True)
    professor_id = db.Column(
        db.Integer, db.ForeignKey("professores.id"), nullable=False
    )
    telefone = db.Column(db.String(30), nullable=False)

    professor = db.relationship("Professor", back_populates="telefones")

    def __repr__(self):
        return f"<ProfessorTelefone {self.telefone}>"


class Regencia(db.Model):
    """Atribuição de um professor a uma DisciplinaTurma específica, com
    indicação de papel: professor principal ou auxiliar."""

    __tablename__ = "regencias"
    __table_args__ = (
        db.UniqueConstraint("disciplina_turma_id", "professor_id"),
        db.Index(
            "ix_regencia_um_principal_por_oferta",
            "disciplina_turma_id",
            unique=True,
            postgresql_where=db.text("principal"),
        ),
    )

    id = db.Column(db.Integer, primary_key=True)
    disciplina_turma_id = db.Column(
        db.Integer, db.ForeignKey("disciplina_turma.id"), nullable=False
    )
    professor_id = db.Column(
        db.Integer, db.ForeignKey("professores.id"), nullable=False
    )
    principal = db.Column(
        db.Boolean, nullable=False, default=False, server_default="false"
    )

    disciplina_turma = db.relationship("DisciplinaTurma", back_populates="regencias")
    professor = db.relationship("Professor", back_populates="regencias")

    def __repr__(self):
        papel = "principal" if self.principal else "auxiliar"
        return f"<Regencia professor_id={self.professor_id} ({papel})>"


class Monitor(db.Model):
    __tablename__ = "monitores"

    id = db.Column(db.Integer, primary_key=True)
    slug = db.Column(db.String(60), unique=True, nullable=False)
    nome = db.Column(db.String(120), nullable=False)
    foto = db.Column(db.String(255), nullable=True)

    monitorias = db.relationship(
        "Monitoria", back_populates="monitor", cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"<Monitor {self.slug}>"


class Monitoria(db.Model):
    """Atribuição de um monitor a uma DisciplinaTurma específica."""

    __tablename__ = "monitorias"
    __table_args__ = (db.UniqueConstraint("disciplina_turma_id", "monitor_id"),)

    id = db.Column(db.Integer, primary_key=True)
    disciplina_turma_id = db.Column(
        db.Integer, db.ForeignKey("disciplina_turma.id"), nullable=False
    )
    monitor_id = db.Column(db.Integer, db.ForeignKey("monitores.id"), nullable=False)

    disciplina_turma = db.relationship("DisciplinaTurma", back_populates="monitorias")
    monitor = db.relationship("Monitor", back_populates="monitorias")

    def __repr__(self):
        return f"<Monitoria monitor_id={self.monitor_id}>"


class Aviso(db.Model):
    """Aviso postado por um professor para uma disciplina.

    Quando `turma_id` é nulo, o aviso vale para todas as turmas da
    disciplina. Quando preenchido, é específico daquela turma — e a
    ForeignKeyConstraint composta abaixo garante que o par
    (disciplina_id, turma_id) é uma combinação real existente em
    DisciplinaTurma (não dá pra criar aviso para uma turma que não cursa
    a disciplina)."""

    __tablename__ = "avisos"
    __table_args__ = (
        db.ForeignKeyConstraint(
            ["disciplina_id", "turma_id"],
            ["disciplina_turma.disciplina_id", "disciplina_turma.turma_id"],
        ),
    )

    id = db.Column(db.Integer, primary_key=True)
    disciplina_id = db.Column(
        db.Integer, db.ForeignKey("disciplinas.id"), nullable=False
    )
    turma_id = db.Column(db.Integer, db.ForeignKey("turmas.id"), nullable=True)
    professor_id = db.Column(
        db.Integer, db.ForeignKey("professores.id"), nullable=False
    )
    titulo = db.Column(db.String(200), nullable=False)
    conteudo = db.Column(db.Text, nullable=False)
    data_publicacao = db.Column(
        db.DateTime(timezone=True),
        nullable=False,
        default=lambda: datetime.now(timezone.utc),
        server_default=db.func.now(),
    )

    disciplina = db.relationship("Disciplina", back_populates="avisos")
    turma = db.relationship("Turma", back_populates="avisos")
    professor = db.relationship("Professor", back_populates="avisos")

    def __repr__(self):
        alvo = self.turma.codigo if self.turma_id else "todas as turmas"
        return f"<Aviso {self.titulo!r} ({alvo})>"


class Horario(db.Model):
    """Horário semanal (aula ou monitoria) de uma DisciplinaTurma.

    Puramente informativo, no momento: um slot de dia/hora/local. `tipo`
    só se aplica a aulas (teórica, laboratório, ou outro tipo livre);
    monitorias não têm subtipo."""

    __tablename__ = "horarios"
    __table_args__ = (
        db.CheckConstraint(
            "categoria IN ('aula', 'monitoria')", name="ck_horario_categoria"
        ),
        db.CheckConstraint(
            "(categoria = 'aula' AND tipo IS NOT NULL) OR "
            "(categoria = 'monitoria' AND tipo IS NULL)",
            name="ck_horario_tipo_conforme_categoria",
        ),
        db.CheckConstraint(
            "dia_semana IN ('segunda', 'terca', 'quarta', 'quinta', 'sexta', "
            "'sabado', 'domingo')",
            name="ck_horario_dia_semana",
        ),
        db.CheckConstraint("hora_fim > hora_inicio", name="ck_horario_fim_apos_inicio"),
    )

    id = db.Column(db.Integer, primary_key=True)
    disciplina_turma_id = db.Column(
        db.Integer, db.ForeignKey("disciplina_turma.id"), nullable=False
    )
    categoria = db.Column(db.String(20), nullable=False)
    tipo = db.Column(db.String(30), nullable=True)
    dia_semana = db.Column(db.String(10), nullable=False)
    hora_inicio = db.Column(db.Time, nullable=False)
    hora_fim = db.Column(db.Time, nullable=False)
    local = db.Column(db.String(120), nullable=True)

    disciplina_turma = db.relationship("DisciplinaTurma", back_populates="horarios")

    def __repr__(self):
        return f"<Horario {self.categoria} {self.dia_semana} {self.hora_inicio}-{self.hora_fim}>"


class Recurso(db.Model):
    """Material de estudo (arquivo baixável ou link externo) postado por um
    professor. Pode ser vinculado a nenhuma, uma ou várias combinações de
    disciplina (todas as turmas) e/ou disciplina+turma específica — ver
    RecursoVinculo. Arquivos ficam no sistema de arquivos do servidor;
    `caminho_arquivo` guarda apenas o caminho relativo."""

    __tablename__ = "recursos"
    __table_args__ = (
        db.CheckConstraint("tipo IN ('arquivo', 'link')", name="ck_recurso_tipo"),
        db.CheckConstraint(
            "(tipo = 'arquivo' AND caminho_arquivo IS NOT NULL AND url IS NULL) OR "
            "(tipo = 'link' AND url IS NOT NULL AND caminho_arquivo IS NULL)",
            name="ck_recurso_campos_conforme_tipo",
        ),
    )

    id = db.Column(db.Integer, primary_key=True)
    professor_id = db.Column(
        db.Integer, db.ForeignKey("professores.id"), nullable=False
    )
    titulo = db.Column(db.String(200), nullable=False)
    descricao = db.Column(db.Text, nullable=True)
    tipo = db.Column(db.String(10), nullable=False)
    caminho_arquivo = db.Column(db.String(500), nullable=True)
    nome_arquivo = db.Column(db.String(255), nullable=True)
    url = db.Column(db.String(500), nullable=True)

    professor = db.relationship("Professor", back_populates="recursos")
    vinculos = db.relationship(
        "RecursoVinculo", back_populates="recurso", cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"<Recurso {self.titulo!r} ({self.tipo})>"


class RecursoVinculo(db.Model):
    """Associa um Recurso a uma disciplina (todas as turmas, se turma_id
    nulo) ou a uma disciplina+turma específica. Um mesmo Recurso pode ter
    vários vínculos — é assim que um recurso 'geral' serve várias
    disciplinas/turmas ao mesmo tempo."""

    __tablename__ = "recurso_vinculos"
    __table_args__ = (
        db.ForeignKeyConstraint(
            ["disciplina_id", "turma_id"],
            ["disciplina_turma.disciplina_id", "disciplina_turma.turma_id"],
        ),
        db.UniqueConstraint("recurso_id", "disciplina_id", "turma_id"),
        db.Index(
            "ix_recurso_vinculo_disciplina_unico_sem_turma",
            "recurso_id",
            "disciplina_id",
            unique=True,
            postgresql_where=db.text("turma_id IS NULL"),
        ),
    )

    id = db.Column(db.Integer, primary_key=True)
    recurso_id = db.Column(db.Integer, db.ForeignKey("recursos.id"), nullable=False)
    disciplina_id = db.Column(
        db.Integer, db.ForeignKey("disciplinas.id"), nullable=False
    )
    turma_id = db.Column(db.Integer, db.ForeignKey("turmas.id"), nullable=True)

    recurso = db.relationship("Recurso", back_populates="vinculos")
    disciplina = db.relationship("Disciplina", back_populates="recurso_vinculos")
    turma = db.relationship("Turma", back_populates="recurso_vinculos")

    def __repr__(self):
        alvo = self.turma.codigo if self.turma_id else "todas as turmas"
        return f"<RecursoVinculo recurso_id={self.recurso_id} disciplina_id={self.disciplina_id} ({alvo})>"
