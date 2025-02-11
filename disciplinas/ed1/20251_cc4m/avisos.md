---
layout: page
title: Avisos
nav_exclude: false
nav_order: 9
grand_parent: Estrutura de Dados I
parent: 2025/1 - Turma CC4M
has_children: false
last_modified_date: 2025-02-10 12:17 -0300
---

# Histórico de avisos: turma CC4M

Olá! Aqui está o histórico de **todos os avisos** feitos para a
disciplina de **Estrutura de Dados I**, semestre 2025/1, turma CC4M.

{% assign avisos = site.avisos
     | where: "disciplina", "ed1"
     | where: "semestre", "20251"
     | where: "turma", "cc4m"
     | reverse  %}
{% for aviso in avisos %}
{{ aviso }}
{% endfor %}
