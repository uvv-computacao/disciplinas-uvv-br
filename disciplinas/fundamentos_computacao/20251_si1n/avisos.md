---
layout: page
title: Avisos
nav_exclude: false
nav_order: 9
grand_parent: Fundamentos da Computação
parent: 2025/1 - Turma SI1N
has_children: false
last_modified_date: 2025-02-07 15:01 -0300
---

# Histórico de avisos: turma SI1N

Olá! Aqui está o histórico de **todos os avisos** feitos para a
disciplina de **Fundamentos da Computação**, semestre 2025/1, turma SI1N.

{% assign avisos = site.avisos
     | where: "disciplina", "fundcomp"
     | where: "semestre", "20251"
     | where: "turma", "si1n"
     | reverse  %}
{% for aviso in avisos %}
{{ aviso }}
{% endfor %}
