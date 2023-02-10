---
layout: page
title: Horário semanal
nav_exclude: false
nav_order: 8
grand_parent: Arquit. de Computadores 1
parent: 2023/1 - Turma CC3N
has_children: false
---

# Horário semanal

Este horário semanal apresenta os dias/horários de aula (obrigatório), junto
com as datas de monitoria (opcional) e a sugestão de horário para o estudo
individual através do Ambiente Virtual de Aprendizagem (obrigatório). Estão
disponíveis:

- **Aulas**: as aulas estão em cor vermelha.

{% assign horarios = site.horarios
     | where: "disciplina", "arqcomp1"
     | where: "semestre", "20231"
     | where: "turma", "cc3n" %}
{% for horario in horarios %}
{{ horario }}
{% endfor %}
