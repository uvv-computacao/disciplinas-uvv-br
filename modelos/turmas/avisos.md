---
layout: page
title: Avisos
nav_exclude: false
nav_order: 9
grand_parent: NOME-DA-DISCIPLINA
parent: NOME-DA-TURMA
has_children: false
---

# Histórico de avisos: turma xxxx

Olá! Aqui está o histórico de **todos os avisos** feitos para a
disciplina de **NOME-DA-DISCIPLINA**, semestre 202x/x, turma xxxx.

{% assign avisos = site.avisos
     | where: "disciplina", "NOME-DA-DISCIPLINA"
     | where: "semestre", "ANOSEMESTRE" 
     | where: "turma", "TURMA"
     | reverse  %}
{% for aviso in avisos %}
{{ aviso }}
{% endfor %}
