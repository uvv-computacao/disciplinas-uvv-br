---
layout: default
title: NOME-DA-TURMA
grand_parent: 
parent: NOME-DA-DISCIPLINA
nav_exclude: false
nav_order: 20
has_toc: false
has_children: true
last_modified_date: 2023-12-20 10:27 -0300
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
- Este é o calendário previsto para o semestre e pode sofrer algumas variações e
  ajustes em virtude de situações que fogem ao nosso controle. Visite sempre
  esta página para ficar atualizado;
- *Hand out*: aquilo que nós entregamos para você;
- *Hand in*: aquilo que você entrega para nós (professor e/ou monitores e/ou
  Autolab); e
- **As datas de hand in são rígidas**, não atrase as entregas para não sofrer
  penalidades na nota!

{% include_relative calendario.md %}
