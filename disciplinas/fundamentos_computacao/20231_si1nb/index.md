---
layout: default
title: 2023/1 - Turma SI1Nb
nav_exclude: true
nav_order: 30
parent: Fundamentos da Computação
has_children: true
has_toc: false
---

# **Fundamentos da Computação: turma SI1Nb**
{: .mb-2 }
UVV, Sistemas de Informação, 1º Semestre de 2023.
{: .mb-2 .fs-6 .text-grey-dk-100 }

Uma visão geral da computação!
{: .mb-2 .fs-5 }

**Professor:** Abrantes Araújo Silva Filho
{: .fs-4 }

<div class="d-flex">
  <div class="flex-justify-start" style="flex-grow: 1">
  {% assign aviso = site.avisos
     | where: "disciplina", "fundcomp"
     | where: "semestre", "20231"
     | where: "turma", "si1nb" %}
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
