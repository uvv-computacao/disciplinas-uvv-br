---
layout: page
title: Pessoal
nav_exclude: false
parent: Projeto Integrado
nav_order: 10
has_children: false
---

## Professores

{% assign professores = site.pessoal 
   | where: "role", "Professor"
   | where_exp:"item", "item.disciplinas contains '20231-proj-int'"
   | reverse %}
<div class="role">
{% for professor in professores %}
{{ professor }}
{% endfor %}
</div>


{% assign monitores = site.pessoal
   | where: "role", "Monitor"
   | where_exp:"item", "item.disciplinas contains '20231-proj-int'" %}
{% assign numero_monitores = monitores | size %}
{% if numero_monitores != 0 %}
## Monitores
<div class="role">
  {% for monitor in monitores %}
  {{ monitor }}
  {% endfor %}
</div>
{% endif %}

