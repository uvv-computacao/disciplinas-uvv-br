---
layout: page
title: Pessoal
grand_parent:
parent: Estrutura de Dados I
nav_exclude: false
nav_order: 40
has_toc: false
has_children: false
last_modified_date: 2025-02-10 12:26 -0300
---

## Professores

{% assign professores = site.pessoal 
   | where: "role", "Professor"
   | where_exp:"item", "item.disciplinas contains '20251-ed1'" %}
<div class="role">
{% for professor in professores %}
{{ professor }}
{% endfor %}
</div>


{% assign monitores = site.pessoal
   | where: "role", "Monitor"
   | where_exp:"item", "item.disciplinas contains '20251-ed1'" %}
{% assign numero_monitores = monitores | size %}
{% if numero_monitores != 0 %}
## Monitores

<div class="role">
  {% for monitor in monitores %}
  {{ monitor }}
  {% endfor %}
</div>
{% endif %}
