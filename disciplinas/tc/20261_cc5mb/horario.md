---
layout: page
title: Horário semanal
grand_parent: Teoria da Computação
parent: 2026/1 - Turma CC5Mb
nav_exclude: false
nav_order: 8
has_toc: false
has_children: false
last_modified_date: 2026-02-01 11:36 -0300
---

# Horário semanal
Este horário semanal apresenta os dias/horários de aula (obrigatórias).
Se disponíveis, também mostrará as aulas de monitoria e demais eventos.

{% assign horarios = site.horarios
     | where: "disciplina", "tc"
     | where: "semestre", "20261"
     | where: "turma", "cc5mb" %}
{% for horario in horarios %}
{{ horario }}
{% endfor %}
