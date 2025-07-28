---
layout: page
title: Horário semanal
grand_parent: Sistemas Operacionais
parent: 2025/2 - Turma EW1M/EW2M
nav_exclude: false
nav_order: 8
has_toc: false
has_children: false
last_modified_date: 2025-07-28 11:41 -0300
---

# Horário semanal
Este horário semanal apresenta os dias/horários de aula (obrigatórias).
Se disponíveis, também mostrará as aulas de monitoria e demais eventos.

{% assign horarios = site.horarios
     | where: "disciplina", "so"
     | where: "semestre", "20252"
     | where: "turma", "ew12m" %}
{% for horario in horarios %}
{{ horario }}
{% endfor %}
