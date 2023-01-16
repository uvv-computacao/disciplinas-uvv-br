---
layout: page
title: Avisos
nav_exclude: false
nav_order: 9
grand_parent: Bancos de Dados 1
parent: 2023/1 - Turma CC1Mc
has_children: false
---

# Histórico de avisos: turma CC1Mc

Olá! Aqui está o histórico de **todos os avisos** feitos para a
disciplina de **Bancos de Dados 1**, semestre 2023/1, turma CC1Mc.

{% assign avisos = site.avisos
     | where: "disciplina", "bd1"
     | where: "semestre", "20231" 
     | where: "turma", "cc1mc"
     | reverse  %}
{% for aviso in avisos %}
{{ aviso }}
{% endfor %}
