---
layout: page
title: Horário semanal
nav_exclude: false
nav_order: 8
grand_parent: Linguagens de Programação
parent: 2023/1 - Turma CC3M
has_children: false
---

# Horário semanal

Este horário semanal apresenta os dias/horários de aula (obrigatório), junto
com as datas de monitoria (opcional) e a sugestão de horário para o estudo
individual através do Ambiente Virtual de Aprendizagem (obrigatório). Estão
disponíveis:

- **Aulas**: as aulas (obrigatórias) estão em cor vermelha. As aulas da
  segunda-feira são semanais, mas as aulas da sexta-feira são quinzenais.
  Verifique no cronograma da disciplina em quais sextas-feiras haverão
  aulas.

{% assign horarios = site.horarios
     | where: "disciplina", "lp"
     | where: "semestre", "20231"
     | where: "turma", "cc3m" %}
{% for horario in horarios %}
{{ horario }}
{% endfor %}
