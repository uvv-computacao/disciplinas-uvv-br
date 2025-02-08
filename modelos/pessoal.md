---
layout: page
title: Pessoal
grand_parent:
parent: NOME-DA-DISCIPLINA
nav_exclude: false
nav_order: 10
has_toc: false
has_children: false
last_modified_date: 2023-12-20 10:27 -0300
---

## Professores

{% assign professores = site.pessoal 
   | where: "role", "Professor"
   | where_exp:"item", "item.disciplinas contains 'SEMESTRE-DISCIPLINA'" %}
<div class="role">
{% for professor in professores %}
{{ professor }}
{% endfor %}
</div>


{% assign monitores = site.pessoal
   | where: "role", "Monitor"
   | where_exp:"item", "item.disciplinas contains 'SEMESTRE-DISCIPLINA'" %}
{% assign numero_monitores = monitores | size %}
{% if numero_monitores != 0 %}
## Monitores

<div class="role">
  {% for monitor in monitores %}
  {{ monitor }}
  {% endfor %}
</div>
{% endif %}

