"""Helpers de formatação de exibição em pt-br.

Os valores internos (dia_semana, categoria de Atividade) ficam sem acento
no banco de propósito — são usados em CHECK constraints e comparações, não
em telas. Esses mapas só existem para a camada de apresentação."""

DIAS_SEMANA = {
    "segunda": "Segunda",
    "terca": "Terça",
    "quarta": "Quarta",
    "quinta": "Quinta",
    "sexta": "Sexta",
    "sabado": "Sábado",
    "domingo": "Domingo",
}

MESES_ABREV = {
    1: "JAN", 2: "FEV", 3: "MAR", 4: "ABR", 5: "MAI", 6: "JUN",
    7: "JUL", 8: "AGO", 9: "SET", 10: "OUT", 11: "NOV", 12: "DEZ",
}

CATEGORIAS_ATIVIDADE = {
    "exercicio": "Exercício",
    "lista": "Lista",
    "pset": "PSET",
    "projeto": "Projeto",
    "trabalho": "Trabalho",
    "lab": "Laboratório",
}


def dia_semana_label(valor):
    return DIAS_SEMANA.get(valor, valor)


def data_curta(data):
    """Formata como '17 AGO', no padrão pt-br — independe do locale do SO."""
    if data is None:
        return "—"
    return f"{data.day:02d} {MESES_ABREV[data.month]}"


def categoria_label(valor):
    return CATEGORIAS_ATIVIDADE.get(valor, valor.capitalize())


def numero_padded(numero):
    if numero is None:
        return ""
    return f"{numero:02d}"


def professor_responsavel(oferta):
    """Professor a destacar para uma DisciplinaTurma: o principal, se houver
    um marcado como tal (Regencia.principal); senão o primeiro professor
    vinculado. Retorna None se a oferta ainda não tem professor cadastrado."""
    for regencia in oferta.regencias:
        if regencia.principal:
            return regencia.professor
    if oferta.regencias:
        return oferta.regencias[0].professor
    return None
