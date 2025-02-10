---
layout: page
title: Avisos
grand_parent: Arq. de Computadores I
parent: 2025/1 - Turma CC4N
nav_exclude: false
nav_order: 9
has_toc: false
has_children: false
last_modified_date: 2025-02-09 23:27 -0300
---

# Histórico de avisos: turma CC4N

Olá! Aqui está o histórico de **todos os avisos** feitos para a
disciplina de **Arquitetura e Organização de Computadores I**,
semestre 2025/1, turma CC4N.

{% assign avisos = site.avisos
     | where: "disciplina", "arqcomp1"
     | where: "semestre", "20251" 
     | where: "turma", "cc4n"
     | reverse  %}
{% for aviso in avisos %}
{{ aviso }}
{% endfor %}
