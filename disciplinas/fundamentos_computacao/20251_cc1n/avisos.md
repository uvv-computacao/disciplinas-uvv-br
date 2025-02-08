---
layout: page
title: Avisos
nav_exclude: false
nav_order: 9
grand_parent: Fundamentos da Computação
parent: 2025/1 - Turma CC1N
has_children: false
last_modified_date: 2025-02-07 15:00 -0300
---

# Histórico de avisos: turma CC1N

Olá! Aqui está o histórico de **todos os avisos** feitos para a
disciplina de **Fundamentos da Computação**, semestre 2025/1, turma CC1N.

{% assign avisos = site.avisos
     | where: "disciplina", "fundcomp"
     | where: "semestre", "20251"
     | where: "turma", "cc1n"
     | reverse  %}
{% for aviso in avisos %}
{{ aviso }}
{% endfor %}
