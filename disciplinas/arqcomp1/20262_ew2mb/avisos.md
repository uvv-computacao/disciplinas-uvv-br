---
layout: page
title: Avisos
grand_parent: Arq. de Computadores I
parent: 2026/2 - Turma EW2Mb
nav_exclude: false
nav_order: 9
has_toc: false
has_children: false
last_modified_date: 2026-08-01 08:40 -0300
---

# Histórico de avisos: turma EW2Mb

Olá! Aqui está o histórico de **todos os avisos** feitos para a
disciplina de **Arquitetura e Organização de Computadores I**,
semestre 2026/2, turma EW2Mb.

{% assign avisos = site.avisos
     | where: "disciplina", "arqcomp1"
     | where: "semestre", "20262" 
     | where: "turma", "ew2mb"
     | reverse  %}
{% for aviso in avisos %}
{{ aviso }}
{% endfor %}
