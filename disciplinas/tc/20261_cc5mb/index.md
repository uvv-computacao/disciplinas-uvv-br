---
layout: default
title: 2026/1 - Turma CC5Mb
grand_parent: 
parent: Teoria da Computação
nav_exclude: false
nav_order: 50
has_toc: false
has_children: true
last_modified_date: 2026-02-01 11:34 -0300
---

# **Teoria da Computação: turma CC5Mb**
{: .mb-2 }
UVV, Teoria da Computação, 1º Semestre de 2026.
{: .mb-2 .fs-6 .text-grey-dk-100 }

**Professor:** Abrantes Araújo Silva Filho
{: .fs-4 }

<div class="d-flex">
  <div class="flex-justify-start" style="flex-grow: 1">
  {% assign aviso = site.avisos
     | where: "disciplina", "tc"
     | where: "semestre", "20261"
     | where: "turma", "cc5mb" %}
  {% if aviso %}
    {{ aviso.last }}
  {% endif %}
  </div>
</div>
<div style="flex-grow: 0">
  <a href="{{ page.dir }}avisos" class="btn btn-outline">Avisos anteriores</a>
</div>

## Calendário previsto
- Este é o calendário previsto para o semestre e pode sofrer algumas variações e
  ajustes em virtude de situações que fogem ao nosso controle. Visite sempre
  esta página para ficar atualizado;
  
{% include_relative calendario.md %}
