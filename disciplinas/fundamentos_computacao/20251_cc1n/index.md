---
layout: default
title: 2025/1 - Turma CC1N
nav_exclude: false
nav_order: 50
parent: Fundamentos da Computação
has_children: true
has_toc: false
last_modified_date: 2025-02-07 14:44 -0300
---

# **Fundamentos da Computação: turma CC1N**
{: .mb-2 }
UVV, Ciência da Computação, 1º Semestre de 2025.
{: .mb-2 .fs-6 .text-grey-dk-100 }

Uma visão geral da computação!
{: .mb-2 .fs-5 }

**Professor:** Abrantes Araújo Silva Filho
{: .fs-4 }

<div class="d-flex">
  <div class="flex-justify-start" style="flex-grow: 1">
  {% assign aviso = site.avisos
     | where: "disciplina", "fundcomp"
     | where: "semestre", "20251"
     | where: "turma", "cc1n" %}
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
- *Hand out*: aquilo que nós entregamos para você;
- *Hand in*: aquilo que você entrega para nós (professor e/ou monitores e/ou
  Autolab); e
- **As datas de hand in são rígidas**, não atrase as entregas para não sofrer
  penalidades na nota!
  
{% include_relative calendario.md %}
