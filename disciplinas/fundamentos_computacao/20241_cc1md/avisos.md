---
layout: page
title: Avisos
nav_exclude: false
nav_order: 9
grand_parent: Fundamentos da Computação
parent: 2024/1 - Turma CC1Md
has_children: false
last_modified_date: 2024-02-05 16:34 -0300
---

# Histórico de avisos: turma CC1Md

Olá! Aqui está o histórico de **todos os avisos** feitos para a
disciplina de **Fundamentos da Computação**, semestre 2024/1, turma CC1Mc.

{% assign avisos = site.avisos
     | where: "disciplina", "fundcomp"
     | where: "semestre", "20241"
     | where: "turma", "cc1md"
     | reverse  %}
{% for aviso in avisos %}
{{ aviso }}
{% endfor %}
