---
layout: page
title: Horário semanal
grand_parent: NOME-DA-DISCIPLINA
parent: NOME-DA-TURMA
nav_exclude: false
nav_order: 8
has_toc: false
has_children: false
last_modified_date: 2023-12-20 10:27 -0300
---

# Horário semanal

Este horário semanal apresenta os dias/horários de aula (obrigatório), junto
com as datas de monitoria (opcional) e a sugestão de horário para o estudo
individual através do Ambiente Virtual de Aprendizagem (obrigatório). Estão
disponíveis:

- **Aulas**: as aulas (obrigatórias) estão em cor vermelha. São de presença
  obrigatória, nos dias e horários indicados. O local da aula também está
  indicado mas pode variar (confira o local da aula nos monitores que estão
  na entrada do edicífio de tecnologia).
- **Monitorias**: as monitorias (opcionais) estão em cor verde. A presença é
  opcional mas fortemente recomendada para que você discuta a matéria com o
  monitor, esclareça suas dúvidas e faça os exercícios e tarefas exigidos
  pelo professor. Em geral as monitorias ocorrem todas as tardes, em algum
  dos laboratórios de informática (o laboratório que estiver disponível,
  procure pelo monitor).
- **Estudo**: as horas de estudo no ambiente virtual de aprendizagem (AVA) são
  obrigatórias: parte dos exercícios e da nota para aprovação na disciplina
  são realizados no AVA. Os dias/horários apontados são apenas uma sugestão:
  o AVA está disponível 24 horas por dia e, portanto, você pode escolher os
  melhores dias/horários para estudo. **ATENÇÃO:** as atividades no AVA têm
  prazo definido e não são aceitas entregas em atraso. Fique atento aos
  prazos.

{% assign horarios = site.horarios
     | where: "disciplina", "bd1"
     | where: "semestre", "20231"
     | where: "turma", "cc1m" %}
{% for horario in horarios %}
{{ horario }}
{% endfor %}
