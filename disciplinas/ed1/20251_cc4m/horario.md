---
layout: page
title: Horário semanal
nav_exclude: false
nav_order: 8
grand_parent: Estrutura de Dados I
parent: 2025/1 - Turma CC4M
has_children: false
last_modified_date: 2025-02-10 12:17 -0300
---

# Horário semanal: turma CC4M

Este horário semanal apresenta os dias/horários de aula (obrigatórias). Se
disponíveis, também mostrará as aulas de monitoria.

{% assign horarios = site.horarios
     | where: "disciplina", "ed1"
     | where: "semestre", "20251"
     | where: "turma", "cc4m" %}
{% for horario in horarios %}
{{ horario }}
{% endfor %}
