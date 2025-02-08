---
layout: page
title: Horário semanal
nav_exclude: false
nav_order: 8
grand_parent: Fundamentos da Computação
parent: 2025/1 - Turma SI1N
has_children: false
last_modified_date: 2025-02-07 15:02 -0300
---

# Horário semanal: turma SI1N

Este horário semanal apresenta os dias/horários de aula (obrigatórias). Se
disponíveis, também mostrará as aulas de monitoria.

{% assign horarios = site.horarios
     | where: "disciplina", "fundcomp"
     | where: "semestre", "20251"
     | where: "turma", "si1n" %}
{% for horario in horarios %}
{{ horario }}
{% endfor %}
