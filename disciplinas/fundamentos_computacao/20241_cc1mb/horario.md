---
layout: page
title: Horário semanal
nav_exclude: false
nav_order: 8
grand_parent: Fundamentos da Computação
parent: 2024/1 - Turma CC1Mb
has_children: false
last_modified_date: 2024-05-05 16:48 -0300
---

# Horário semanal: turma CC1Mb

Este horário semanal apresenta os dias/horários de aula (obrigatórias). Se
disponíveis, também mostrará as aulas de monitoria.

{% assign horarios = site.horarios
     | where: "disciplina", "fundcomp"
     | where: "semestre", "20241"
     | where: "turma", "cc1mb" %}
{% for horario in horarios %}
{{ horario }}
{% endfor %}
