---
layout: page
title: Avisos
nav_exclude: false
nav_order: 9
grand_parent: Linguagens de Programação
parent: 2023/1 - Turma CC3M
has_children: false
---

# Histórico de avisos: turma CC3M

Olá! Aqui está o histórico de **todos os avisos** feitos para a
disciplina de **Linguagens de Programação**, semestre 2023/1, turma CC3M.

{% assign avisos = site.avisos
     | where: "disciplina", "lp"
     | where: "semestre", "20231" 
     | where: "turma", "cc3m"
     | reverse  %}
{% for aviso in avisos %}
{{ aviso }}
{% endfor %}
