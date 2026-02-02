---
layout: page
title: Avisos
nav_exclude: true
nav_order: 9
grand_parent: Internet das Coisas
parent: 2025/1 - Turma AN1tN
has_children: false
last_modified_date: 2025-02-08 15:00 -0300
---

# Histórico de avisos: turma AN1tN

Olá! Aqui está o histórico de **todos os avisos** feitos para a
disciplina de **Internet das Coisas**, semestre 2025/1, turma AN1tN.

{% assign avisos = site.avisos
     | where: "disciplina", "iot"
     | where: "semestre", "20251"
     | where: "turma", "an1tn"
     | reverse  %}
{% for aviso in avisos %}
{{ aviso }}
{% endfor %}
