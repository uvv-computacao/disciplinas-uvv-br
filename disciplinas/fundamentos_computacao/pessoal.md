---
layout: page
title: Pessoal
parent: Fundamentos da Computação
has_children: false
has_toc: false
nav_exclude: false
nav_order: 40
last_modified_date: 2024-07-31 10:52 -0300
---

## Professores

{% assign professores = site.pessoal 
   | where: "role", "Professor"
   | where_exp:"item", "item.disciplinas contains '20242-fc'" %}
<div class="role">
{% for professor in professores %}
{{ professor }}
{% endfor %}
</div>


{% assign monitores = site.pessoal
   | where: "role", "Monitor"
   | where_exp:"item", "item.disciplinas contains '20242-fc'" %}
{% assign numero_monitores = monitores | size %}
{% if numero_monitores != 0 %}
## Monitores

<div class="role">
  {% for monitor in monitores %}
  {{ monitor }}
  {% endfor %}
</div>
{% endif %}

