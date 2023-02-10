---
layout: page
title: Avisos
nav_exclude: false
nav_order: 9
grand_parent: Arquit. de Computadores 1
parent: 2023/1 - Turma CC3N
has_children: false
---

# Histórico de avisos: turma CC3N

Olá! Aqui está o histórico de **todos os avisos** feitos para a
disciplina de **Arquitetura e Organização de Computadores 1**,
semestre 2023/1, turma CC3N.

{% assign avisos = site.avisos
     | where: "disciplina", "arqcomp1"
     | where: "semestre", "20231" 
     | where: "turma", "cc3n"
     | reverse  %}
{% for aviso in avisos %}
{{ aviso }}
{% endfor %}
