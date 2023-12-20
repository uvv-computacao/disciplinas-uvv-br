---
layout: default
title: 2024/1 - Turma CC1Ma
nav_exclude: false
nav_order: 20
parent: Fundamentos da Computação
has_children: true
has_toc: false
last_modified_date: 2023-12-20 11:22 -0300
---

# **Fundamentos da Computação: turma CC1Ma**
{: .mb-2 }
UVV, Ciência da Computação, 1º Semestre de 2024.
{: .mb-2 .fs-6 .text-grey-dk-100 }

Uma visão geral da computação!
{: .mb-2 .fs-5 }

**Professor:** Abrantes Araújo Silva Filho
{: .fs-4 }

<div class="d-flex">
  <div class="flex-justify-start" style="flex-grow: 1">
  {% assign aviso = site.avisos
     | where: "disciplina", "fundcomp"
     | where: "semestre", "20241"
     | where: "turma", "cc1ma" %}
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
