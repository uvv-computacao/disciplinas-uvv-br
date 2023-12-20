---
layout: default
title: 2023/1 - Turma CC3M
nav_exclude: false
nav_order: 20
parent: Linguagens de Programação
has_children: true
has_toc: false
---

# **Linguagens de Programação: turma CC3M**
{: .mb-2 }
UVV, Ciência da Computação, 1º Semestre de 2023.
{: .mb-2 .fs-6 .text-grey-dk-100 }

O estudo das características fundamentais à todas as linguagens
de programção.
{: .mb-2 .fs-5 }

**Professor:** Abrantes Araújo Silva Filho
{: .fs-4 }

<div class="d-flex">
  <div class="flex-justify-start" style="flex-grow: 1">
  {% assign aviso = site.avisos
     | where: "disciplina", "lp"
     | where: "semestre", "20231"
     | where: "turma", "cc3m" %}
  {% if aviso %}
    {{ aviso.last }}
  {% endif %}
  </div>
</div>
<div style="flex-grow: 0">
  <a href="{{ page.dir }}avisos" class="btn btn-outline">Avisos anteriores</a>
</div>

## Calendário previsto

{% include_relative calendario.md %}
