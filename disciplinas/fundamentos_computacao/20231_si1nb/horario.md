---
layout: page
title: Horário semanal
nav_exclude: false
nav_order: 8
grand_parent: Fundamentos da Computação
parent: 2023/1 - Turma SI1Nb
has_children: false
---

# Horário semanal: turma SI1Nb

Este horário semanal apresenta os dias/horários de aula (obrigatórias). Se disponíveis, também mostrará as aulas de monitoria.

{% assign horarios = site.horarios
     | where: "disciplina", "fundcomp"
     | where: "semestre", "20231"
     | where: "turma", "si1nb" %}
{% for horario in horarios %}
{{ horario }}
{% endfor %}
