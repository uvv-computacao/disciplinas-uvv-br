---
layout: default
title: 2023/1 - Turma CC3N
nav_exclude: false
nav_order: 20
parent: Arquit. de Computadores 1
has_children: true
has_toc: false
---

# **Arquitetura e Organização de Computadores 1: turma CC3N**
{: .mb-2 }
UVV, Ciência da Computação, 1º Semestre de 2023.
{: .mb-2 .fs-6 .text-grey-dk-100 }

O estudo da interface entre o *software* e o *hardware*.
{: .mb-2 .fs-5 }

**Professor:** Abrantes Araújo Silva Filho
{: .fs-4 }

<div class="d-flex">
  <div class="flex-justify-start" style="flex-grow: 1">
  {% assign aviso = site.avisos
     | where: "disciplina", "arqcomp1"
     | where: "semestre", "20231"
     | where: "turma", "cc3n" %}
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
