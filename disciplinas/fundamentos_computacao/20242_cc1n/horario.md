---
layout: page
title: Horário semanal
nav_exclude: false
nav_order: 8
grand_parent: Fundamentos da Computação
parent: 2024/2 - Turma CC1N
has_children: false
last_modified_date: 2024-07-06 15:37 -0300
---

# Horário semanal: turma CC1N

Este horário semanal apresenta os dias/horários de aula (obrigatórias). Se
disponíveis, também mostrará as aulas de monitoria.

{% assign horarios = site.horarios
     | where: "disciplina", "fundcomp"
     | where: "semestre", "20242"
     | where: "turma", "cc1n" %}
{% for horario in horarios %}
{{ horario }}
{% endfor %}
