---
layout: page
title: Avisos
grand_parent: NOME-DA-DISCIPLINA
parent: NOME-DA-TURMA
nav_exclude: false
nav_order: 9
has_toc: false
has_children: false
last_modified_date: 2023-12-20 10:27 -0300
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
