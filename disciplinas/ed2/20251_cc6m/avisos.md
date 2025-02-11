---
layout: page
title: Avisos
nav_exclude: false
nav_order: 9
grand_parent: Estrutura de Dados II
parent: 2025/1 - Turma CC6M
has_children: false
last_modified_date: 2025-02-10 12:17 -0300
---

# Histórico de avisos: turma CC6M

Olá! Aqui está o histórico de **todos os avisos** feitos para a
disciplina de **Estrutura de Dados II**, semestre 2025/1, turma CC6M.

{% assign avisos = site.avisos
     | where: "disciplina", "ed2"
     | where: "semestre", "20251"
     | where: "turma", "cc6m"
     | reverse  %}
{% for aviso in avisos %}
{{ aviso }}
{% endfor %}
