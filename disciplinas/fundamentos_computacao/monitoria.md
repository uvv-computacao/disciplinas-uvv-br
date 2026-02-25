---
layout: default
title: Monitoria e Laboratórios
parent: Fundamentos da Computação
has_children: false
has_toc: false
nav_exclude: true
nav_order: 27
last_modified_date: 2025-03-13 18:46-0300
---

# Previsão das monitorias e laboratórios

Aqui estão listados, em ordem cronológica, as datas previstas para as atividades
de **monitoria** e de **laboratório**, bem como uma breve descrição do que será
feito em cada uma dessas atividades.

{% assign monitorias = site.monitorias
     | where: "disciplina", "fundcomp"
     | where: "semestre", "20251" %}
{% for monitoria in monitorias %}
{{ monitoria }}
{% endfor %}
