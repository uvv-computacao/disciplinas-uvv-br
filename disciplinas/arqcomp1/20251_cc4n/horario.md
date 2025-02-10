---
layout: page
title: Horário semanal
grand_parent: Arq. de Computadores I
parent: 2025/1 - Turma CC4N
nav_exclude: false
nav_order: 8
has_toc: false
has_children: false
last_modified_date: 2025-02-09 23:27 -0300
---

# Horário semanal
Este horário semanal apresenta os dias/horários de aula (obrigatórias).
Se disponíveis, também mostrará as aulas de monitoria e demais eventos.

{% assign horarios = site.horarios
     | where: "disciplina", "arqcomp1"
     | where: "semestre", "20251"
     | where: "turma", "cc4n" %}
{% for horario in horarios %}
{{ horario }}
{% endfor %}
