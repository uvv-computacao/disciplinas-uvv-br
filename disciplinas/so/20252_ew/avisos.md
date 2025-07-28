---
layout: page
title: Avisos
grand_parent: Sistemas Operacionais
parent: 2025/2 - Turma EW1M/EW2M
nav_exclude: false
nav_order: 9
has_toc: false
has_children: false
last_modified_date: 2025-07-28 11:40 -0300
---

# Histórico de avisos: turma EW1M/EW2M

Olá! Aqui está o histórico de **todos os avisos** feitos para a
disciplina de **Sistemas Operacionais**, semestre 2025/2, turma
EW1M/EW2M.

{% assign avisos = site.avisos
     | where: "disciplina", "so"
     | where: "semestre", "20252" 
     | where: "turma", "ew12m"
     | reverse  %}
{% for aviso in avisos %}
{{ aviso }}
{% endfor %}
