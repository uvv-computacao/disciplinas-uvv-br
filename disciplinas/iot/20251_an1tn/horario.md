---
layout: page
title: Horário semanal
nav_exclude: false
nav_order: 8
grand_parent: Internet das Coisas
parent: 2025/1 - Turma AN1tN
has_children: false
last_modified_date: 2025-02-08 15:01 -0300
---

# Horário semanal: turma AN1tN

Este horário semanal apresenta os dias/horários de aula (obrigatórias). Se
disponíveis, também mostrará as aulas de monitoria.

{% assign horarios = site.horarios
     | where: "disciplina", "iot"
     | where: "semestre", "20251"
     | where: "turma", "an1tn" %}
{% for horario in horarios %}
{{ horario }}
{% endfor %}
