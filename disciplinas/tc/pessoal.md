---
layout: page
title: Pessoal
grand_parent:
parent: Teoria da Computação
nav_exclude: false
nav_order: 40
has_toc: false
has_children: false
last_modified_date: 2026-02-01 11:32 -0300
---

## Professores

{% assign professores = site.pessoal 
   | where: "role", "Professor"
   | where_exp:"item", "item.disciplinas contains '20261-tc'" %}
<div class="role">
{% for professor in professores %}
{{ professor }}
{% endfor %}
</div>


{% assign monitores = site.pessoal
   | where: "role", "Monitor"
   | where_exp:"item", "item.disciplinas contains '20261-tc'" %}
{% assign numero_monitores = monitores | size %}
{% if numero_monitores != 0 %}
## Monitores

<div class="role">
  {% for monitor in monitores %}
  {{ monitor }}
  {% endfor %}
</div>
{% endif %}
