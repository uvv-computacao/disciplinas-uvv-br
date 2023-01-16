---
layout: page
title: Avisos
nav_exclude: false
nav_order: 9
grand_parent: Bancos de Dados 1
parent: 2023/1 - Turma CC1N
has_children: false
---

# Histórico de avisos: turma CC1N

Olá! Aqui está o histórico de **todos os avisos** feitos para a
disciplina de **Bancos de Dados 1**, semestre 2023/1, turma CC1N.

{% assign avisos = site.avisos
     | where: "disciplina", "bd1"
     | where: "semestre", "20231" 
     | where: "turma", "cc1n"
     | reverse  %}
{% for aviso in avisos %}
{{ aviso }}
{% endfor %}
