---
layout: page
title: Avisos
nav_exclude: false
nav_order: 9
grand_parent: Fundamentos da Computação
parent: 2024/1 - Turma CC1Ma
has_children: false
last_modified_date: 2023-12-20 11:55 -0300
---

# Histórico de avisos: turma CC1Ma

Olá! Aqui está o histórico de **todos os avisos** feitos para a
disciplina de **Fundamentos da Computação**, semestre 2024/1, turma CC1Ma.

{% assign avisos = site.avisos
     | where: "disciplina", "fundcomp"
     | where: "semestre", "20241"
     | where: "turma", "cc1ma"
     | reverse  %}
{% for aviso in avisos %}
{{ aviso }}
{% endfor %}
