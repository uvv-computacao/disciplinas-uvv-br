---
layout: page
title: Horário semanal
grand_parent: Arq. de Computadores I
parent: 2026/2 - Turma CC4M
nav_exclude: false
nav_order: 8
has_toc: false
has_children: false
last_modified_date: 2026-08-01 08:39 -0300
---

# Horário semanal
Este horário semanal apresenta os dias/horários de aula (obrigatórias).
Se disponíveis, também mostrará as aulas de monitoria e demais eventos.

{% assign horarios = site.horarios
     | where: "disciplina", "arqcomp1"
     | where: "semestre", "20262"
     | where: "turma", "cc4m" %}
{% for horario in horarios %}
{{ horario }}
{% endfor %}
