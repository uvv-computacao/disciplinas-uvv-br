---
layout: page
title: Roteiro de estudo
grand_parent:
parent: Arq. de Computadores I
nav_exclude: false
nav_order: 20
has_toc: false
has_children: false
last_modified_date: 2026-11-19 13:42 -0300
---

# Roteiro de estudo

**Estudo da 17ª Semana**<a id="re17sem"></a> (16/11 - 22/11)
{: .label .label-reading }

Esta é nossa **última semana** de aula antes das provas AV2 e, portanto, você
deve se dedicar a fazer uma grande revisão do conteúdo do segundo bimestre e se
preparar para a prova. Conforme já avisado inúmeras vezes, a AV2 é **difícil**,
na verdade é **muito difícil**, e você deve vir muito bem preparado para a
avaliação. Também conforme já avisado, são 60 questões objetivas, de todo o
conteúdo do segundo bimestre, e a correção será feita imediatamente no momento
em que você entregar a prova (você sai da prova já sabendo sua nota).

Aqui estão dois **EXERCÍCIOS DE REVISÃO** para você verificar o nível de
dificuldade da prova e você saber se está bem preparado para a prova (pelo menos
o conteúdo cobrado nesses exercícios de revisão). Minha sugestão é a seguinte:
tente fazer esses exercícios de revisão sozinho, em um primeiro momento, e
depois em um pequeno grupo com seus colegas. Discuta cada questão, anote as
dúvidas e me procure nessa semana para esclarecer qualquer dúvida.

* [**Revisão de Arquitetura da
  CPU**](/assets/disciplinas/arqcomp1/20262/revisao1.pdf) (2 páginas e 5
  perguntas discursivas)
  * **Turmas CC4M, CC4Mb, EW2M e EW2Mb:** esse exercício aborda arquitetura da
    CPU, combinado com representação de dados binários inteiros signed, ponto
    flutuante, notação enviesada, IEEE-754 e instruções em assembly e binário
    RISC-V. Com tudo o que vocês estudaram durante o segundo bimestre vocês têm
    condições de responder com segurança. Use calculadora.
  
* [**Revisão de Arquitetura da
  Memória**](/assets/disciplinas/arqcomp1/20262/revisao2.pdf) (12 páginas e 18
  perguntas discursivas)
  * **Turmas CC4M e CC4Mb:** como vocês já estudaram sobre linguagem C (na
    disciplina "Laboratório de Programação") vocês têm a obrigação de entender
    todo o programa mostrado nesse documento e, de fato, saber exatamente o que
    está ocorrendo em qualquer parte do programa. Durante a AV2 eu posso fazer
    perguntas sobre a programação C em si.
  * **Turmas EW2M e EW2Mb:** como vocês ainda não estudaram sobre linguagem C,
    se vocês não entenderem algumas partes da linguagem C, tentem se focar mais
    nas declarações e inicializações das variáveis e entender em que trechos do
    código essas declarações estão, para entender quais segmentos da memória
    estão envolvidos.
  * **Todas as turmas:** muitas perguntas abordam o mesmo assunto e podem ser
    consideradas "repetitivas". Se vocês quiserem priorizar a ordem de
    resolução, podem deixar as questões 6, 10, 13, 15, 17 e 18 como opcionais
    ou, no mínimo, para responder após as outras.
    
Para ajudar você a entender melhor os segmentos de memória e a como escolher o
segmento específico para colocar uma variável, aqui está um pequeno programa de
demonstração (em C23) que utiliza todos os segmentos de memória, criando
variáveis globais e locais. Tenha certeza de que você **sabe exatamente o
motivo** para cada variável estar no segmento indicado. Você pode apenas ler o
PDF ou usar um compilador C23 para rodar o programa por conta própria:

* [memoria.c.pdf](/assets/disciplinas/arqcomp1/20262/memoria.c.pdf)
* [memoria.c](/assets/disciplinas/arqcomp1/20262/memoria.c)
    
---

**Estudo da 16ª Semana**<a id="re16sem"></a> (09/11 - 15/11)
{: .label .label-reading }

- **Leituras obrigatórias:**
  - [Notas de Aula: Arquitetura da
    Memória](/assets/disciplinas/arqcomp1/20262/memoria.pdf)

---

**Estudo da 15ª Semana**<a id="re15sem"></a> (02/11 - 08/11)
{: .label .label-reading }

- **Leituras obrigatórias:**
  - [Notas de Aula: Processo de compilação e linguagem de
    máquina](/assets/disciplinas/arqcomp1/20262/cap02c.pdf)

---

**Estudo da 14ª Semana**<a id="re14sem"></a> (26/10 - 01/11)
{: .label .label-reading }

- **Leituras obrigatórias:**
  - [Notas de Aula: Números _signed_ e
    _unsigned_](/assets/disciplinas/arqcomp1/20262/cap02b.pdf)
- **Outras atividades:**
  - Entregue o **Diário de Aprendizagem n.º 1** até o dia 30/10/2026, 12:00h.

---

**Estudo da 13ª Semana**<a id="re13sem"></a> (19/10 - 25/10)
{: .label .label-reading }

- **Leituras obrigatórias:**
  - [Notas de Aula: Performance](/assets/disciplinas/arqcomp1/20262/cap01c.pdf)
  - [Notas de Aula: Conjunto de
    Instruções](/assets/disciplinas/arqcomp1/20262/cap02a.pdf)
- **Outras atividades:**
  - Continue fazendo o **Diário de Aprendizagem n.º 1**. Lembre-se de que a data
    de entrega é até o dia 30/10/2026, 12:00h.

---

**Estudo da 12ª Semana**<a id="re12sem"></a> (12/10 - 18/10)
{: .label .label-reading }

Esta será uma semana atípica pois três dias serão feriados e atrapalharão nosso
cronograma. Para que o conteúdo da disciplina não fique muito fora de sintonia
entre as diversas turmas, não haverá aula de conteúdo e também não será feita a
lista de presença: ao invés disso você deve, durante o horário da aula,
continuar fazendo o **Diário de Aprendizagem n.º 1** (lembre-se de que a data
máxima de entrega é dia 30/10/2026 12:00h). O professor estará em sala de aula,
na terça e na quarta, para tirar dúvidas a respeito desse conteúdo.

- **Exercícios:**
  - Continuar o [Diário de Aprendizagem n.º
    1](/assets/disciplinas/arqcomp1/20262/diario_1.pdf).
    - **PRAZO DE ENTREGA: até 30/10/2026, 12:00h.** Você pode me entregar o
      Diário de Aprendizagem em qualquer dia da semana. O local mais provável de
      você me encontrar é na sala de aula (nos dias/horários de sua aula), ou no
      laboratório de hardware.Diário de Aprendizagem n.º 1.

---

**Estudo da 11ª Semana**<a id="re11sem"></a> (05/10 - 11/10)
{: .label .label-reading }

Nesta semana aprenderemos sobre como algumas tecnologias de input e output de
dados são fabricadas, e também sobre o processo de fabricação de CPUs e
memória. Além disso começaremos a aprender como a performance dos computadores é
calculada e entenderemos alguns conceitos básicos como o clock dos
processadores.

{: .danger }
> A partir dessa semana você deverá assistir à inúmeros vídeos de conteúdo e
> fazer um exercício **GIGANTE** sobre computação (o exercício tem quase 40
> páginas de perguntas discursivas). O prazo de entrega rígido mas você terá
> bastante tempo para isso (3 semanas). Não deixe acumular os exercícios pois
> eles farão parte razoável da nota bimestral, juntamente com o caderno de
> estudo individual.

- **Leituras obrigatórias:**
  - [Notas de Aula: Dentro dos computadores; Tecnologias para a construção de
    CPU e memória](/assets/disciplinas/arqcomp1/20262/cap01b.pdf)
  - [Notas de Aula: Performance](/assets/disciplinas/arqcomp1/20262/cap01c.pdf)
- **Vídeos obrigatórios:**
  - [Parte 0: Visão Geral](https://www.youtube.com/watch?v=XbuHXSoKZOM)
  - [Parte 1: O que é ciência da
    computação](https://www.youtube.com/watch?v=qzxw-Tm8UgI) 
  - [Parte 2: Representação de
    dados](https://www.youtube.com/watch?v=8T_hJhYg4R0) 
    - [Parte 2, Anexo 1: Conversão entre
      bases](https://www.youtube.com/watch?v=7u4lJQE2xOk) 
    - [Parte 2, Anexo 2: Outros
      conceitos](https://www.youtube.com/watch?v=MxdbxybOlmE) 
    - [Parte 2, Anexo 3: Binários
       negativos](https://www.youtube.com/watch?v=gLBV2iU_EbM) 
    - [Parte 2, Anexo 4: Binários
      fracionários](https://www.youtube.com/watch?v=QdOMYMvn2h8) 
    - [Parte 2, Anexo 5: BCD](https://www.youtube.com/watch?v=8Tl0I2Ihc0w)
  - [Parte 3, Algoritmos](https://www.youtube.com/watch?v=NIy_YxAS570)
  - [Parte 4, Pensamento
    Computacional](https://www.youtube.com/watch?v=w4XK1nY-pMc)
  - [Parte 5, Abstração](https://www.youtube.com/watch?v=pPNKC6ii8cE)
- **Exercícios:**
  - [Diário de Aprendizagem n.º
    1](/assets/disciplinas/arqcomp1/20262/diario_1.pdf). Por favor, preste muita
    atenção às seguintes instruções referentes a esses exercícios:
    - Esses exercícios eram originalmente da disciplina "Fundamentos da
      Computação", do 1º período. Estou exigindo que vocês façam esses
      exercícios (baseados principalmente nos vídeos que apontei acima) pois
      vocês precisam dominar esse conteúdo. Por favor, ignorem as referências à
      essa disciplina.
    - Todas as perguntas precisam ser respondidas.
    - Você deve **imprimir** as questões e responder de forma **manuscrita**.
    - **PRAZO DE ENTREGA: até 30/10/2026, 12:00h.** Você pode me entregar o
      Diário de Aprendizagem em qualquer dia da semana. O local mais provável de
      você me encontrar é na sala de aula (nos dias/horários de sua aula), ou no
      laboratório de hardware.

---

**Estudo da 10ª Semana**<a id="re10sem"></a> (28/09 - 04/10)
{: .label .label-reading }

Após dois meses intensos de atividades práticas no Laboratório de Hardware,
faremos um bloco de aulas teóricas sobre Arquitetura de Computadores. Nesta
semana temos um conteúdo um pouco mais simples, com os conceitos iniciais da
disciplina.

{: .important }
> Além da matéria de **Arquitetura de Computadores I** por si mesma, você tem a
> **obrigação** de assistir a diversos vídeos que eu gravei para a disciplina
> **CR6.100B: Introdução à Ciência da Computação**, que é uma disciplina
> específica para os **Fundamentos da Computação**. Esses vídeos são
> absolutamente essenciais para que você aprenda a representar diversos tipos de
> dados em binário e comece a entender de fato as bases da computação que são
> importantes para o entendimento da arquitetura dos computadores. Não importa
> se você está no curso de Ciência da Computação, Engenharia da Computação,
> Engenharia de Software, Sistemas de Informação, Análise e Desenvolvimento de
> Sistemas ou outro qualquer: se você é da área da computação, esses vídeos
> serão absolutamente essenciais para você.

{: .danger }
> A partir desta semana você fará **MUITOS EXERCÍCIOS** a respeitos dos vídeos
> gravados. Os exercícios são **gigantescos** e têm prazo de entrega rígido. Não
> deixe acumular os exercícios pois eles farão parte razoável da nota bimestral,
> juntamente com o caderno de estudo individual.

- **Leituras obrigatórias:**
  - [Notas de Aula - Motivação 1: Computador é magia ou
    servo?](/assets/disciplinas/arqcomp1/20262/1_motivacao.pdf)
  - [Notas de Aula - Motivação 2: int não é
    Z](/assets/disciplinas/arqcomp1/20262/2_int_nao_e_z.pdf)
  - [Notas de Aula - Motivação 3: Olá,
    mundo!](/assets/disciplinas/arqcomp1/20262/3_ola_mundo.pdf)
  - [Notas de Aula - Motivação 4:
    Memória](/assets/disciplinas/arqcomp1/20262/4_memoria.pdf)
  - [Notas de Aula - Motivação 5:
    I/O](/assets/disciplinas/arqcomp1/20262/5_entrada_saida_rede.pdf)
  - [Notas de Aula: Introdução, Grandes Idéias da Computação, Abaixo dos
    Programas](/assets/disciplinas/arqcomp1/20262/cap01a.pdf)
- **Vídeos obrigatórios:**
  - [Apresentação da CR6.100B](https://www.youtube.com/watch?v=eyph1kcLnVw)
  - [Motivação e diferenças com a
    CS50](https://www.youtube.com/watch?v=d7uDtdECwGg)
  - [Como fazer a CR6.100B](https://www.youtube.com/watch?v=an7aEc5du0o)
  - [Unidade 0: Introdução à
    CR6.100B](https://www.youtube.com/watch?v=-aY8U8s5Kv4)
- **Leituras recomendadas:**
  - [Edsger Wybe Dijkstra: _Why numbering should start at
    zero?_](https://www.cs.utexas.edu/users/EWD/ewd08xx/EWD831.PDF)
- **Exercícios:**
  - [Diário de Aprendizagem n.º
    0](/assets/disciplinas/arqcomp1/20262/diario_0.pdf). Por favor, preste muita
    atenção às seguintes instruções referentes a esses exercícios:
    - Esses exercícios eram originalmente da disciplina "Fundamentos da
      Computação", do 1º período. Estou exigindo que vocês façam esses
      exercícios (baseados principalmente nos vídeos que apontei acima) pois
      vocês precisam dominar esse conteúdo. Por favor, ignorem as referências à
      essa disciplina.
    - Algumas questões são específicas da matéria de Fundamentos da Computação e
      não precisam ser feitas. As questões que não precisam ser respondidas são
      as questões: 6, 13, 20, 21, 22 e 27.
    - Você deve **imprimir** as questões e responder de forma **manuscrita**.
    - **PRAZO DE ENTREGA: até 09/10/2026, 12:00h.** Você pode me entregar o
      Diário de Aprendizagem em qualquer dia da semana. O local mais provável de
      você me encontrar é na sala de aula (nos dias/horários de sua aula), ou no
      laboratório de hardware.

---

**Estudo da 9ª Semana**<a id="re09sem"></a> (21/09 - 27/09)
{: .label .label-reading }

- **Sumô Tech Fight InovaWeek 2026!**
  - Após o trabalho árduo de construção, programação e teste de seu robô, agora
    é hora de colocá-lo à prova no Sumô Tech Fight 2026! Participe das
    competições nos dias 23 e 24 de setembro (verifique a planilha com das
    datas, chaves, horários e dojôs).

---

**Estudo da 8ª Semana**<a id="re08sem"></a> (14/09 - 20/09)
{: .label .label-reading }

- **Leituras obrigatórias:**
  - [Regras para o Sumô Tech Fight 2026](/assets/robo_sumo/regras_2026.pdf)
- **Outras atividades:**
  - Construção do robô de sua equipe.

---

**Estudo da 7ª Semana**<a id="re07sem"></a> (07/09 - 13/09)
{: .label .label-reading }

- **Leituras obrigatórias:**
  - [Regras para o Sumô Tech Fight 2026](/assets/robo_sumo/regras_2026.pdf)
- **Outras atividades:**
  - Construção do robô de sua equipe.

---

**Estudo da 6ª Semana**<a id="re06sem"></a> (31/08 - 06/09)
{: .label .label-reading }

- **Leituras obrigatórias:**
  - [Regras para o Sumô Tech Fight 2026](/assets/robo_sumo/regras_2026.pdf)
- **Outras atividades:**
  - Construção do robô de sua equipe.

---

**Estudo da 5ª Semana**<a id="re05sem"></a> (24/08 - 30/08)
{: .label .label-reading }

- **Leituras obrigatórias:**
  - [Regras para o Sumô Tech Fight 2026](/assets/robo_sumo/regras_2026.pdf)
- **Outras atividades:**
  - Construção do robô de sua equipe.

---

**Estudo da 4ª Semana**<a id="re04sem"></a> (17/08 - 23/08)
{: .label .label-reading }

- **Leituras obrigatórias:**
  - Para a construção do **Robô Sumô**: ler as seguintes "_Dicas para a
    construção do robô sumô_" (que estão disponíveis na [página de
    recursos](../recursos)):
    - [Dica 01: visão geral da
      eletrônica](/assets/robo_sumo/dica_01_visao_geral_da_eletronica.pdf)
    - [Dica 02: lista de compra de
      componentes](/assets/robo_sumo/dica_02_lista_de_compras.pdf)
  - Para aprender a usar os sensores de ultrassom que o seu robô sumô usará
    para detectar o adversário, leia a "Apostila Eletrogate: Intermediate",
    Exemplo 10. A apostila está na [página de recursos](../recursos).
  - Para aprender a usar os sensores infravermelhos que o seu robô sumô usará
    para detectar a borda branca da arena, leia a "Apostila Eletrogate:
    Advanced", Exemplo 8. A apostila está na [página de recursos](../recursos).
- **Vídeos obrigatórios:**
  - [O que é um sensor ultrassônico
    (HC-SR04)](https://www.youtube.com/watch?v=QmyByyhiiwk)
  - [HC-SR04 ULTRASONIC SENSOR - WHAT it is and HOW to use
    it](https://www.youtube.com/watch?v=1E4TDZC-xaY)
  - [Arduino ROBOT Mini SUMO - SENSOR
    IR](https://www.youtube.com/watch?v=o0FMSIltwu4)
  - [Sensor Ótico Reflexivo
    TCRT5000](https://www.youtube.com/watch?v=_EpC9TYzIuM)
- **Leituras recomendadas:**
  - (nada no momento)
- **Vídeos recomendados:**
  - [Sensor de Distância (HC-SR04) no
    Arduino](https://www.youtube.com/watch?v=l-jlKjbfDsQ)
  - [Sensor reflexivo infravermelho
    TCRT5000](https://www.youtube.com/watch?v=LuX_ZGIRCzo)
- **Exercícios:**
  - [2ª Lista de Exercício:
    Arduino](/assets/disciplinas/arqcomp1/20262/arduino02.pdf). Esta lista deve
    ser feita individualmente, de forma manuscrita. Você deve imprimir a lista e
    responder diretamente nos espaços reservados para as respostas. Você deve
    entregar essa lista até o dia 21/08/2026, 12:00h, no Laboratório de
    Hardware. Coloque seu nome completo e sua turma de forma legível na primeira
    página da lista. Não serão aceitas entregas posteriores, sob hipótese
    nenhuma. Lembre-se de que este exercício substituirá o visto/carimbo nos
    cadernos individuais de estudo enquanto estivermos construindo o robô sumô
    e, assim, fará parte de 40% de sua nota semestral.
- **Outras atividades:**
  - A partir da lista de compra de componentes, você e o seu time de robô sumô
    devem escolher as peças do robô e discutir com o professor, DURANTE ESTA
    SEMANA, a lista de compras. Depois da aprovação do professor sua equipe deve
    comprar o mais rápido possível os componentes.

---

**Estudo da 3ª Semana**<a id="re03sem"></a> (10/08 - 16/08)
{: .label .label-reading }

- **Leituras obrigatórias:**
  - Para aprender sobre o **Caderno de Engenharia**: leia as [instruções para o
    caderno de
    engenharia](/assets/docs/caderno_engenharia/engineering_notebook.pdf) e
    tenha certeza de que você (e todo o resto de seu grupo) compreendeu a
    importância e como fazer registros no caderno de engenharia.
  - Para aprender sobre o **Arduino**: para começar a aprender a montar
    circuitos e a programar o Arduino, ler os seguintes capítulos do livro
    "Official Arduino Projects Book" (o PDF do livro está na [página de
    recursos](../recursos)). **Recomendo enfaticamente** que você faça essa
    leitura construindo os circuitos propostos em um Arduino e componentes
    eletrônicos reais ou, no mínimo, usando um programa de simulação online
    gratuito como o [Tinkercad](https://www.tinkercad.com/).
    - Capítulo 2 (páginas 32-41): programação básica do Arduino, configuração
      básica com a função `setup()`, execução do programa com a função
      `loop()`, funções de escrita digital nos pinos de I/O, operações
      condicionais, leitura de código de cores de resistores.
    - Capítulo 3 (páginas 42-51): uso de sensor de temperatura, monitor serial
      do Arduino, estrutura de repetição, variáveis, operadores lógicos.
  - Para a construção do **Robô Sumô**: ler as seguintes "_Dicas para a
    construção do robô sumô_" (que estão disponíveis na [página de
    recursos](../recursos)):
    - [Dica 01: visão geral da
      eletrônica](/assets/robo_sumo/dica_01_visao_geral_da_eletronica.pdf)
- **Vídeos obrigatórios:**
  - [Conheça os sensores do
    Arduino](https://www.youtube.com/watch?v=vEdYjAbzrAE)
  - [How to Use an Arduino](https://www.youtube.com/watch?v=cd04o5yqSAU)
- **Leituras recomendadas:**
  - [Arduino Uno Rev. 3 Datasheet](/assets/arduino/arduino_uno_r3_datasheet.pdf)
  - [C Programming](/assets/disciplinas/arqcomp1/c_programming.pdf) (PDF): se
    você não tem uma boa base na linguagem C ou se precisa de uma revisão
    rápida, este arquivo é o PDF do "Anexo C" do livro *Digital Design and
    Computer Architecture* (também [disponível
    online](https://booksite.elsevier.com/9780128000564/index.php)). Estude esse
    material para aprender/revisar programação C.
- **Vídeos recomendados:**
  - [Sensor de temperatura de alta precisão e baixo custo
    (LM35)](https://www.youtube.com/watch?v=VjHfjkd5KuE)
  - [How to Use a TMP36 Temperature Sensor with
    Arduino](https://www.youtube.com/watch?v=5nF5R4CGZG4)
- **Exercícios:**
  - [1ª Lista de Exercício:
    Arduino](/assets/disciplinas/arqcomp1/20262/arduino01.pdf). Esta lista deve
    ser feita individualmente, de forma manuscrita. Você deve imprimir a lista e
    responder diretamente nos espaços reservados para as respostas. Você deve
    entregar essa lista até o dia 14/08/2026, 12:00h, no Laboratório de
    Hardware. Coloque seu nome completo e sua turma de forma legível na primeira
    página da lista. Não serão aceitas entregas posteriores, sob hipótese
    nenhuma. Lembre-se de que este exercício substituirá o visto/carimbo nos
    cadernos individuais de estudo enquanto estivermos construindo o robô sumô
    e, assim, fará parte de 40% de sua nota semestral.
- **Outras atividades:**
  - Seu time do robô sumô deve **levar o caderno de engenharia** na aula do
    Laboratório de Hardware. Conforme explicado na sala de aula, qualquer
    **LIVRO DE ATAS** vendido em papelarias será suficiente (livros com 50
    páginas são suficientes). Será feita uma vistoria do caderno de
    engenharia. O professor entregará a capa e o sumário padronizados que devem
    ser colados no caderno de engenharia. Lembre-se de que o visto no caderno de
    engenharia também faz parte dos 40% de sua nota semestral.

---

**Estudo da 2ª Semana**<a id="re02sem"></a> (03/08 - 09/08)
{: .label .label-reading }

- **Leituras obrigatórias:**
  - [Notas de aula: fundamentos físicos da
    computação](/assets/disciplinas/arqcomp1/20262/fund_fisicos.pdf)
  - Para o laboratório, você deve ler os seguintes capítulos do livro "Official
    Arduino Projects Book" (o PDF do livro está na [página de
    recursos](../recursos))
    - Capítulo 1 do "Official Arduino Projects Book" (páginas 20-31): seu
      primeiro projeto com o Arduino, um LED controlado por botão
- **Vídeos obrigatórios:**
  - [Como funciona uma protoboard](https://www.youtube.com/watch?v=DfU6llvIMcM)
  - [Como funciona um multímetro](https://www.youtube.com/watch?v=1WIWrmc-rBk)
- **Leituras recomendadas:**
  - (nada no momento)
- **Vídeos recomendados:**
  - (nada no momento)
- **Registro do estudo semanal no seu caderno:**
  - Enquanto você está estudando o conteúdo desta semana, registre em seu
    caderno de estudos tudo o que você está aprendendo. Você pode fazer um
    resumo, um mapa mental, um diagrama... você deve registrar a data do estudo
    e o que foi estudado, o que foi aprendido e quais são as dúvidas para
    perguntar ao professor. Lembre-se de que o professor irá vistoriar
    semanalmente seu caderno para verificar se você está mantendo o caderno de
    estudos em dia (isso vale 40% de sua nota).
- **Exercícios:**
  - (nada no momento)
- **Outras atividades:**
  - (nada no momento)

---

**Estudo da 1ª Semana**<a id="re01sem"></a> (27/07 - 02/08)
{: .label .label-reading }

- **Leituras obrigatórias:**
  - [Notas de aula: fundamentos físicos da
    computação](/assets/disciplinas/arqcomp1/20262/fund_fisicos.pdf)
  - Para o laboratório, você deve ler os seguintes capítulos do livro "Official
    Arduino Projects Book" (o PDF do livro está na [página de
    recursos](../recursos))
    - Capítulo 0 do "Official Arduino Projects Book" (páginas 1-19): informações
      básicas sobre o que é o Arduino, aprender os principais componentes
      eletrônicos, circuitos, protoboard e instalação do software;
- **Vídeos obrigatórios:**
  - [O que é Arduino, afinal de
    contas?](https://www.youtube.com/watch?v=sv9dDtYnE1g)
  - [Para que servem os componentes
    eletrônicos?](https://www.youtube.com/watch?v=C54Cp819Ebc)
- **Leituras recomendadas:**
  - [Arduino Uno Rev. 3 Datasheet](/assets/arduino/arduino_uno_r3_datasheet.pdf)
- **Vídeos recomendados:**
  - [Ferramentas: tudo o que você queria
    saber](https://www.youtube.com/watch?v=5JxN3ELqo9I)
- **Registro do estudo semanal no seu caderno:**
  - Enquanto você está estudando o conteúdo desta semana, registre em seu
    caderno de estudos tudo o que você está aprendendo. Você pode fazer um
    resumo, um mapa mental, um diagrama... você deve registrar a data do estudo
    e o que foi estudado, o que foi aprendido e quais são as dúvidas para
    perguntar ao professor. Lembre-se de que o professor irá vistoriar
    semanalmente seu caderno para verificar se você está mantendo o caderno de
    estudos em dia (isso vale 40% de sua nota).
- **Exercícios:**
  - (nada no momento)
- **Outras atividades:**
  - (nada no momento)

---
**Notas:**
