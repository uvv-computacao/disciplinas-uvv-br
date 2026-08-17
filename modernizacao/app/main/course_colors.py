"""Cor de destaque (--course-color) de cada disciplina.

Em vez de uma classe CSS fixa por disciplina (o que exigiria editar o CSS
toda vez que uma disciplina nova fosse cadastrada), a cor é escolhida a
partir de uma paleta fixa usando um hash determinístico do slug — a mesma
disciplina sempre recebe a mesma cor, sem precisar de configuração manual.
"""

PALETA = [
    ("#315ca8", "#edf3fd"),  # azul
    ("#7545a4", "#f4effa"),  # roxo
    ("#087f73", "#eaf7f5"),  # verde-azulado
    ("#a14c32", "#fbefeb"),  # terracota
    ("#4b7a3d", "#eef6ea"),  # verde
    ("#a13f6a", "#fbeaf1"),  # rosa
]


def course_color(slug):
    """Retorna (cor, cor_suave) determinístico para o slug informado."""
    indice = sum(ord(c) for c in slug) % len(PALETA)
    return PALETA[indice]
