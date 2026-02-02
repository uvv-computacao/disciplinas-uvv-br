---
layout: page
title: Avisos
grand_parent: Robótica e Dispositivos Inteligentes
parent: 2026/1 - Turma EO1M
nav_exclude: false
nav_order: 9
has_toc: false
has_children: false
last_modified_date: 2026-02-01 11:23 -0300
---

# Histórico de avisos: turma EO1M

Olá! Aqui está o histórico de **todos os avisos** feitos para a
disciplina de **Robótica e Dispositivos Inteligentes**,
semestre 2026/1, turma EO1M.

{% assign avisos = site.avisos
     | where: "disciplina", "robotica"
     | where: "semestre", "20261" 
     | where: "turma", "eo1m"
     | reverse  %}
{% for aviso in avisos %}
{{ aviso }}
{% endfor %}
