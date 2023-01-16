---
layout: default
title: 2023/1 - Turma CC1Mb
nav_exclude: false
nav_order: 30
parent: Bancos de Dados 1
has_children: true
has_toc: false
---

# **Bancos de Dados 1: turma CC1Mb**
{: .mb-2 }
UVV, Ciência da Computação, 1º Semestre de 2023.
{: .mb-2 .fs-6 .text-grey-dk-100 }

Uma introdução ao fantástico mundo dos sistemas de bancos de dados.
{: .mb-2 .fs-5 }

**Professor:** Abrantes Araújo Silva Filho
{: .fs-4 }

<div class="d-flex">
  <div class="flex-justify-start" style="flex-grow: 1">
  {% assign aviso = site.avisos
     | where: "disciplina", "bd1"
     | where: "semestre", "20231"
     | where: "turma", "cc1mb" %}
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
