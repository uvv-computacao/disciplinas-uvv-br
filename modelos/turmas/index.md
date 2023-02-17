---
layout: default
title: NOME-DA-TURMA
nav_exclude: false
nav_order: 20
parent: NOME-DA-DISCIPLINA
has_children: true
has_toc: false
---

# **NOME-DA-DISCIPLINA: turma xxxx**
{: .mb-2 }
UVV, xxx nome do curso xxx, xº Semestre de 202x.
{: .mb-2 .fs-6 .text-grey-dk-100 }

oneliner da disciplina.
{: .mb-2 .fs-5 }

**Professor:** xxxxxxxx
{: .fs-4 }

<div class="d-flex">
  <div class="flex-justify-start" style="flex-grow: 1">
  {% assign aviso = site.avisos
     | where: "disciplina", "NOME-DA-DISCIPLINA"
     | where: "semestre", "ANOSEMESTRE"
     | where: "turma", "TURMA" %}
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
