---
layout: page
title: Horário semanal
nav_exclude: false
nav_order: 8
grand_parent: Fundamentos da Computação
parent: 2024/1 - Turma CC1Ma
has_children: false
last_modified_date: 2023-12-20 11:57 -0300
---

# Horário semanal: turma CC1Ma

Este horário semanal apresenta os dias/horários de aula (obrigatórias). Se
disponíveis, também mostrará as aulas de monitoria.

{% assign horarios = site.horarios
     | where: "disciplina", "fundcomp"
     | where: "semestre", "20241"
     | where: "turma", "cc1ma" %}
{% for horario in horarios %}
{{ horario }}
{% endfor %}
