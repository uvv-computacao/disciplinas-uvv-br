---
layout: page
title: Avisos
grand_parent: Teoria da Computação
parent: 2026/1 - Turma CC5Mb
nav_exclude: false
nav_order: 9
has_toc: false
has_children: false
last_modified_date: 2026-02-01 11:25 -0300
---

# Histórico de avisos: turma CC5Mb

Olá! Aqui está o histórico de **todos os avisos** feitos para a
disciplina de **Teoria da Computação**, semestre 2026/1, turma
CC5Mb.

{% assign avisos = site.avisos
     | where: "disciplina", "tc"
     | where: "semestre", "20261" 
     | where: "turma", "cc5mb"
     | reverse  %}
{% for aviso in avisos %}
{{ aviso }}
{% endfor %}
