---
layout: page
title: Avisos
nav_exclude: false
nav_order: 9
grand_parent: Fundamentos da Computação
parent: 2023/1 - Turma SI1Nb
has_children: false
---

# Histórico de avisos: turma xxxx

Olá! Aqui está o histórico de **todos os avisos** feitos para a
disciplina de **Fundamentos da Computação**, semestre 202x/x, turma xxxx.

{% assign avisos = site.avisos
     | where: "disciplina", "fundcomp"
     | where: "semestre", "20231" 
     | where: "turma", "si1nb"
     | reverse  %}
{% for aviso in avisos %}
{{ aviso }}
{% endfor %}
