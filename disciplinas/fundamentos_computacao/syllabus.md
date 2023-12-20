---
layout: page
title: Syllabus
nav_exclude: false
parent: Fundamentos da Computação
nav_order: 1
has_children: false
last_modified_date: 2023-12-20 15:24 -0300
---

# Syllabus[^1]
{:.no_toc}
[^1]: Ementa, plano detalhado de estudo, programa de estudos.

## Sumário
{: .no_toc .text-delta }

* TOC
{:toc}

## 1. Professor
<p>Abrantes Araújo Silva Filho
<br />
<a href="mailto:abrantesasf@uvv.br">abrantesasf@uvv.br</a></p>

## 2. Descrição
Esta é a disciplina **Fundamentos de Tecnologia da Computação** (Fundamentos da
Computação) da Universidade Vila Velha (UVV), voltada para alunos iniciantes nos
cursos da área de computação (Ciência da Computação, Sistemas de Informação,
Análise e Desenvolvimento de Sistemas, Engenharia da Computação e, na verdade,
qualquer pessoa interessada, com ou sem experiência anterior em computação e/ou
programação). Não se preocupe se você não tiver nenhuma experiência prévia na
área: estatísticas globais mostram que $$2/3$$ dos estudantes em disciplinas
introdutórias como esta não tinham nenhuma experiência prévia na área.

Esta disciplina é uma adaptação da "[CR6.100B: Introdução à Ciência da
Computação](https://www.computacaoraiz.com.br/cr6100b/)", do Computação Raiz,
que, por sua vez, é uma tradução e adaptação da disciplina "[CS50: Introduction
to Computer Science](https://cs50.harvard.edu/x/2023/)", da Universidade de
Harvard, acrescida de idéias e conceitos de outras disciplinas
([BJC](https://bjc.edc.org/) e [CS10](https://cs10.org/fa23/), da Universidade
da Califórnia em Berkeley; [6.001](http://tinyurl.com/sicpocw) e
[6.0001](http://tinyurl.com/j5xvz8tp) do MIT). Para deixar mais claro:

![Origem da disciplina](/assets/disciplinas/fundcomp/origem_cr6100b.png)

Este curso ensina você a **resolver problemas**, com e sem código, com ênfase em
correção, design e estilo. Os tópicos incluem pensamento computacional,
abstração, algoritmos, estruturas de dados e ciência da computação de forma mais
ampla. Teremos PSETs (conjuntos de problemas desafiadores)[^2] inspirados nas
artes, humanidades, ciências sociais e ciências.

[^2]: PSET: é uma abreviatura para _Problem Set_, Conjunto de Problemas. Os
    PSETs são problemas altamente difíceis, que forçarão seu estudo e capacidade
    de resolução de problemas.

Mais do que ensinar você a programar em uma determinada linguagem, este curso
ensina os **fundamentos da computação** e os **fundamentos da programação**, de
forma que você consiga, por conta própria, ensinar a você mesmo novas linguagens
no final das contas.

O curso começa com uma linguagem tradicional, mas onipresente, chamada **C**,
que foi uma precursora e base para algumas linguagens de programação mais
modernas, através da qual você aprenderá não apenas sobre funções, variáveis,
condicionais, loops e mais, mas, também, sobre como os computadores funcionam
por "baixo do capô", memória e tudo mais.

Dependendo do cronograma da UVV e, principalmente, do ritmo de estudo e
comprometimento dos alunos, talvez seja possível ainda:

* Fazer a transição para a **Python**, uma linguagem de alto nível mais
  moderna que você compreenderá muito mais por causa do C;
* Aprendermos sobre **SQL**, uma linguagem através da qual você pode armazenar
  dados em bancos de dados;
* Aprendermos sobre **HTML**, **CSS** e **JavaScript**, através dos quais você
  pode criar aplicativos web e móveis; e
* Juntar todo o aprendizado em um grane projeto final a ser exibido para toda a
  UVV!

### 2.1. Diferenças entre a CR6.100B e a Fundamentos da Computação
A única diferença entre a CR6.100B e a Fundamentos da Computação é em relação ao
tempo/quantidade de conteúdo. Como a CR6.100B é uma disciplina online, tem um
cronograma mais "lento", no ritmo do próprio aluno; já a Fundamentos da
Computação deve se adequar ao calendário acadêmico da UVV e, por isso, nem todo
o conteúdo da CR6.100B será visto: a Fundamentos da Computação faz uma seleção
de conteúdos para os alunos.

Dependendo do calendário acadêmico da UVV e, principalmente, do ritmo de estudo
e comprometimento dos alunos, a Fundamentos da Computação pode conseguir cumprir
todo o conteúdo de estudo da CR6.100B. Mas isso depende muito mais dos alunos do
que da disciplina em si: se os alunos forem comprometidos, participarem de todas
as atividades e estudarem com afinco, mais conteúdos podem ser vistos. O núcleo
central do conteúdo (dos fundamentos até estruturas de dados) é sempre estudado,
mas os conteúdos adicionais dependem do ritmo dos alunos.


## 3. Dinâmica da disciplina
Esta disciplina tem carga horária total de 60 horas semestrais (40h presenciais
e 20h online) e está dividida em **aulas**, **monitorias**, **tutorias**,
**diários de aprendizagem**, **exercícios**, **laboratórios** e **PSETs** (estes
três últimos realizados no Autolab).

* **AULAS**: cada turma terá 1 (uma) aula presencial por semana, com 1:40h de
  duração, conforme o calendário da UVV (consulte a seção específica de sua
  turma para ver os dias/horários de sua turma). A presença nas aulas é
  obrigatória e terá peso na nota da disciplina.
  
  {: .attention }
  Conforme normas da UVV você pode acumular até 10 horas de faltas, o que
  corresponde a perder 5 dias de aula. Caso você ultrapasse as 10 horas (ou 5
  dias) de faltas você será automaticamente reprovado na disciplina, sem
  possibilidade de recurso. O professor tem liberdade de escolher a política de
  tomada de presença que melhor lhe convier (por exemplo: fazer uma única
  chamada durante a aula, fazer uma chamada no início e outra no final, utilizar
  listas em papel ou o sistema online).
  
* **MONITORIAS**: cada turma terá, além das horas de aula normais, até 6 horas
  de monitoria por semana, com um aluno monitor (um aluno que já passou pela
  disciplina e agora ajuda aos que estão começando). As monitorias são
  realizadas no período vespertino, conforme calendário específico de cada
  turma. A presença em, pelo menos, 2 horas semanais de monitoria é obrigatória
  e terá peso na nota da disciplina. Os monitores farão o seguinte:
  * Aulas de revisão do conteúdo da aula
  * Aulas com conteúdos extras importantes
  * Ajudarão nos **exercícios**, **laboratórios** e **PSETs** no Autolab
  * Estarão à disposição para esclarecimento de dúvidas
  * Receberão e farão a conferência dos **diários de aprendizagem**
  * Avaliarão os códigos que vocês enviarem no Autolab, quanto à correção,
    design e estilo
  * Utilizarão ferramentas de inteligência artificial para a detecção de cola ou
    plágio nas atividades do Autolab
  * Fornecerão feedback nas atividades do Autolab
  
  {: .attention }
  A **participação nas monitorias é essencial** para seu aprendizado! Apesar de
  introdutória esta não é uma disciplina fácil e você terá que dedicar um tempo
  considerável de estudo e realização de atividades. Você terá muitas dúvidas
  que devem ser sanadas com os monitores.

---
**Notas:**
