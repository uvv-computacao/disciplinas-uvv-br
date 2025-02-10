---
layout: default
title: 2025/1 - Turma CC4N
grand_parent: 
parent: Arq. de Computadores I
nav_exclude: false
nav_order: 50
has_toc: false
has_children: true
last_modified_date: 2025-02-09 09:20 -0300
---

# **Arquitetura de Computadores I: turma CC4N**
{: .mb-2 }
UVV, Ciência da Computação, 1º Semestre de 2025.
{: .mb-2 .fs-6 .text-grey-dk-100 }

A interface entre o hardware e o software!
{: .mb-2 .fs-5 }

**Professor:** Abrantes Araújo Silva Filho
{: .fs-4 }

<div class="d-flex">
  <div class="flex-justify-start" style="flex-grow: 1">
  {% assign aviso = site.avisos
     | where: "disciplina", "arqcomp1"
     | where: "semestre", "20251"
     | where: "turma", "cc4n" %}
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
