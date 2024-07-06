---
layout: page
title: Avisos
nav_exclude: false
nav_order: 9
grand_parent: Fundamentos da Computação
parent: 2024/2 - Turma CC1Mb
has_children: false
last_modified_date: 2024-07-06 15:38 -0300
---

# Histórico de avisos: turma CC1Mb

Olá! Aqui está o histórico de **todos os avisos** feitos para a
disciplina de **Fundamentos da Computação**, semestre 2024/2, turma CC1Mb.

{% assign avisos = site.avisos
     | where: "disciplina", "fundcomp"
     | where: "semestre", "20242"
     | where: "turma", "cc1mb"
     | reverse  %}
{% for aviso in avisos %}
{{ aviso }}
{% endfor %}
