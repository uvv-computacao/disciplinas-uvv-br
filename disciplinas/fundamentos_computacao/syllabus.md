---
layout: page
title: Syllabus
nav_exclude: false
parent: Fundamentos da Computação
nav_order: 10
has_children: false
last_modified_date: 2023-12-20 15:24 -0300
---

# Syllabus
{:.no_toc}

[(clique aqui para a versão PDF deste
documento)](/assets/disciplinas/fundcomp/syllabus_2024_1.pdf)

Além do material oficial que está disponível no Portal do Aluno da UVV
(Universidade de Vila Velha), este documento contém mais detalhes sobre a
dinâmica da disciplina **Fundamentos de Tecnologia da Computação** (Fundamentos
da Computação) para as turmas deste semestre (2024/1). Leia-o com atenção e
procure o professor para esclarecer qualquer dúvida. O *syllabus*[^1] funcionará
como a nossa "constituição", ou seja, será a base para todas as regras,
políticas e funcionamento de nosso curso. Além do *syllabus* a ementa oficial da
disciplina está [disponível para
download](/assets/disciplinas/fundcomp/ementa_2024_1.pdf).

[^1]: Ementa, plano detalhado de estudo, programa de estudos.

## Sumário
{: .no_toc .text-delta }

* TOC
{:toc}

## 1. Visão geral da disciplina
Olá, seja muito bem-vindo!

Esta é a disciplina **Fundamentos de Tecnologia da Computação** (Fundamentos da
Computação), para os cursos de [Ciência da
Computação](https://uvv.br/ensino-presencial/graduacao/ciencia-da-computacao/) e
[Sistemas de
Informação](https://uvv.br/ensino-presencial/graduacao/sistemas-de-informacao/)
da Universidade de Vila Velha (UVV).

Esta disciplina está voltada para alunos iniciantes nos cursos da área de
computação (Ciência da Computação, Sistemas de Informação, Análise e
Desenvolvimento de Sistemas, Engenharia da Computação) mas, na verdade, qualquer
pessoa interessada, de qualquer outra área ou curso, com ou sem experiência
anterior em computação e/ou programação, tem condições de fazer a disciplina e
aprender.

Não se preocupe se você não tiver nenhuma experiência prévia na
área: estatísticas globais (Universidades de Harvard e Yale) mostram que $$2/3$$
dos estudantes em disciplinas introdutórias como esta não tinham nenhuma
experiência prévia na área.

O conteúdo da disciplina é uma adaptação da "[CR6.100B: Introdução à Ciência da
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
ampla. Teremos **PSETs**[^2] (conjuntos de problemas desafiadores) inspirados
nas artes, humanidades, ciências sociais e ciências.

[^2]: PSET: é uma abreviatura para _Problem Set_, Conjunto de Problemas. Os
    PSETs são problemas altamente difíceis, que forçarão seu estudo e capacidade
    de resolução ao máximo.

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

Prepare-se, pois esta disciplina é muito **extensa**, **árdua** e **difícil**,
mas o resultado, se você se dedicar conforme descrito neste plano de ensino,
será recompensador!

### 1.1. Diferenças entre a CR6.100B e a Fundamentos da Computação
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


## 2. Pré-requisitos
- **OBRIGATÓRIOS**[^3]:
  - **Matemática**: familiaridade e conforto com, pelo menos, a matemática
    do ensino médio (aritmética, álgebra, funções e conjuntos). Caso sua base
    matemática seja fraca, veja o texto [Preparação para graduação em áreas
    exatas: matemática além do
    básico](https://www.abrantes.pro.br/2020/05/20/preparacao-para-graduacao-em-areas-exatas-matematica-alem-do-basico/),
    com dicas para estudar novamente a matemática, do jeito certo.
- **RECOMENDADOS**[^4]:
  - **Computador**: você deve ter um computador com acesso a internet (câmera,
    microfone e caixas de som são recomendados) e com capacidade suficiente para
    instalar e executar os softwares que serão utilizados (um computador
    recente, com arquitetura Intel x86 de 64 bits, com Linux, Windows ou Mac,
    com 8 GiB de memória RAM e bastante espaço em disco). Verifique a Seção
    [Laboratório de computação e computador
    pessoal](#laboratrio-de-computao-e-computador-pessoal) para maiores
    detalhes. Caso você não tenha um computador e/ou notebook, poderá utilizar
    os laboratórios de informática da UVV, no período vespertino, para estudar e
    realizar as atividades da disciplina; e
  - **Inglês**: os livros e leituras obrigatórias ou opcionais da disciplina
    estarão em português mas haverá também bastante conteúdo em inglês
    (principalmente leitura de documentação técnica). Na área da computação é
    absolutamente fundamental o domínio de inglês (se você não sabe inglês
    COMECE JÁ a estudar).
- **NÃO OBRIGATÓRIOS**[^5]:
  - **Programação**: algum curso introdutório de programação, em qualquer
    linguagem.

[^3]: São conhecimentos prévios e/ou recursos que você, obrigatoriamente, deve
    ter para que possa acompanhar adequadamente a disciplina e aprender o
    conteúdo. Caso você não possua algum dos pré-requisitos obrigatórios poderá
    ter dificuldade para acompanhar as aulas ou realizar todas as atividades
    propostas pelo professor (nesse caso converse **imediatamente** com o
    professor para explicar a situação e tentar encontrar uma solução).

[^4]: São conhecimentos e/ou recursos que facilitarão muito o seu estudo. Caso
    você não possua os requisitos recomendados, sugere-se que você faça um plano
    para obtê-los com o tempo.

[^5]: São conhecimentos prévios e/ou recursos não obrigatórias mas que, se você
    tiver, podem facilitar seu estudo (você já terá uma base a partir da qual
    irá desenvolver novas habilidades). Se você não tiver nenhum dos requisitos
    não obrigatórios, não se preocupe: você conseguirá acompanhar a disciplina.

## 3. Objetivos de aprendizagem
Ao final desta disciplina você deverá ser capaz de:

* Entender o que é computação, ciência da computação e programação;
* Entender os componentes do pensamento computacional, aplicando-os na resolução
  de diversos problemas importantes;
* Entender como a estrutura de um computador (processador e memória) influenciam
  nos programas que você criar para resolver problemas;
* Pensar mais metodicamente;
* Representar e processar informação;
* Se comunicar de forma sucinta e precisa;
* Resolver problemas de modo correto e eficaz;
* Utilizar técnicas de gerenciamento de complexidade ao resolver problemas;
* Decompor um problema complexo em partes menores e achar a solução para essas
  partes;
* Operar com conforme em múltiplos níveis de abstração;
* Programar proceduralmente;
* Separar os detalhes de projeto (design) dos detalhes de implementação;
* Inferir, a partir dos princípios, como os sistemas funcionam;
* Avaliar a corretude, design e estilo do código de um programa;
* Entender o básico sobre complexidade de algoritmos, e reconhecer alguns dos
  algoritmos clássicos da computação;
* Entender o básico sobre estruturas de dados, e reconhecer algumas das
  estruturas de dados clássicas da computação;
* Aprender por conta própria outras linguagens de programação;
* Ler documentação técnica e tirar conclusões a partir das especificações;
* Testar as soluções criadas, encontrando falhas e identificando casos extremos
  que o programa trata, ou não, com corretude;
* Descrever precisamente os sinais e sintomas de problemas;
* Perguntar questões de modo claro;
* Utilizar o terminal Linux, especificamente uma interface de linha de comando,
  para interagir com o sistema operacional;
* Utilizar um ambiente de desenvolvimento integrado; e
* Sentir-se seguro e confiante na resolução de problemas de modo computacional.

{: .important }
Em última análise, o curso pretende fornecer uma base sólida para estudos
adicionais em ciência da computação (e áreas afins) e capacitá-lo a aplicar a
computação a problemas em outros domínios.


## 4. Estrutura e recursos da disciplina

### 4.1. Professor
Olá, meu nome é Abrantes Araújo Silva Filho e serei o professor responsável pela
sua turma. Algumas informações sobre mim:

- Sou graduado em **medicina** pela [UFES](https://ufes.br/) (1999), mestre em
  **epidemiologia e métodos quantitativos em saúde** pela
  [FIOCRUZ](https://portal.fiocruz.br/) (2002) e graduado em **ciência da
  computação** pela [FAESA](https://www.faesa.br/) (2021). Atualmente sou
  estudante do bacharelado em **matemática** da
  [Uninter](https://www.uninter.com/), na modalidade de ensino a distância
  (EAD).
- Meus principais sites:
  - [www.linkedin.com/in/abrantes-filho](https://www.linkedin.com/in/abrantes-filho/)
  - [github.com/abrantesasf](https://github.com/abrantesasf) e também
    [github.com/computacaoraiz](https://github.com/computacaoraiz)
  - [www.abrantes.pro.br](https://www.abrantes.pro.br/) e também
    [www.computacaoraiz.com.br](https://www.computacaoraiz.com.br)
  - [www.youtube.com/computacaoraiz](https://www.youtube.com/computacaoraiz)
  - [cursos.computacaoraiz.com.br](https://cursos.computacaoraiz.com.br)
- Informações de contato:
  - [abrantesasf@uvv.br](mailto:abrantesasf@uvv.br)
  - (27) 9-9991-4393, para entrar em contato via
    [Signal](https://signal.org/)[^6] (eu não uso WhatsApp).

[^6]: Eu não uso o WhatsApp por motivos de privacidade. Se quiser me mandar uma
    mensagem, você terá que usar o Signal.

### 4.2. Monitores
Esta disciplina conta com diversos monitores para auxiliar o estudo e orientar
os alunos. Conheça os monitores na página sobre o
[Pessoal](/disciplinas/fundamentos_computacao/pessoal/) da disciplina.

Os monitores, em conjunto, proporcionarão 10 horas semanais de orientação, das
quais você tem que participar obrigatoriamente em 2 horas. Essas horas
obrigatórias de monitoria serão realizadas em um dia fixo específico da semana,
durante o período vespertino. Você deverá escolher o dia da semana de sua
preferência ao responder o questionário inicial da disciplina.

{: .note }
Os monitores são alunos que já fizeram (e foram aprovados) na disciplina, e
estão voluntariamente dedicando tempo e esforço para ajudar os novos alunos. Por
favor, entenda que os monitores, por mais capacitados que estejam, podem não
saber alguns aspectos mais avançados da matéria. Contamos com sua compreensão:
os monitores são alunos, assim como vocês.

O papel dos monitores é variado e inclui, entre outros:

- Dar aulas de revisão do conteúdo visto com o professor;
- Dar aulas com conteúdo extra importante;
- Ajudar nos exercícios, laboratórios e PSETs a serem realizados no Autolab (mas
  sem dar as respostas!);
- Receber, conferir e vistar os diários de aprendizagem;
- Avaliar os códigos dos programas que vocês enviarão no Autolab, quanto à
  correção, estilo e design;
- Fornecer *feedback* nas atividades do Autolab; e
- Utilizar ferramentas de detecção de cola ou plágio nas atividades do Autolab.

{: .important }
A participação semanal em 1 tarde de monitoria é obrigatória (2 horas de
monitoria) e contará pontos para a nota final da disciplina mas, mais importante
do que os pontos, é a aprendizagem que você terá: a participação na monitoria é
**essencial** para seu aprendizado. Não menospreze a monitoria!

### 4.3. Laboratório de computação e computador pessoal
A estrutura de laboratórios de computação da UVV é excelente, possuindo máquinas
com hardware e software padronizados que facilitam a realização das atividades.
Além disso o benefício mais importante de trabalhar no laboratório é obter ajuda
direta do professor, dos assistentes, e de seus próprios colegas de turma.

Entretanto, por limitações de tempo, você precisará realizar tarefas em seu
próprio computador pessoal. Veja aqui as configurações mínimas necessárias para
que você consiga realizar todas as tarefas em seu próprio computador:

- **Processador**: deve ter arquitetura INTEL x86, de 64 bits. Outras
  arquiteturas, como a ARM (MacBook Air M1, por exemplo), podem não funcionar
  em todos os casos (entre em contato com os monitores ou o professor em caso de
  dúvidas). Qualquer computador relativamente recente com processador Intel ou
  AMD já está adequado;
- **Memória**: no mínimo 8 GiB de memória RAM (16 GiB é recomendável);
- **Disco rígido**: se você optar pelas ferramentas online, qualquer quantidade
  de espaço em disco já está adequada; se você optar pela máquina virtual da
  disciplina, deve ter pelo menos 50 GiB de espaço livre em disco (70 GiB
  durante a instalação da máquina virtual do curso);
- **Sistema operacional**: Linux, Windows ou Mac (Linux é altamente
  recomendado!);
- **Monitor**: no mínimo um monitor HD (Full HD é recomendável). Seu monitor
  deve ser grande o suficiente para que você possa trabalhar com conforto.
  Se você tiver dois monitores poderá realizar as tarefas em um monitor e
  usar o outro para ler o conteúdo ou consultar a documentação técnica;
- **Internet**: você deve ter uma conexão razoavelmente rápida para fazer o
  download da máquina virtual. Além disso você precisará de uma conexão à
  Internet para acessar e realizar as atividades no Autolab;
- **Som**: não é obrigatório, exceto se algumas aulas extras online forem
  realizadas;
- **Microfone**: não é obrigatório, exceto se algumas aulas extras online forem
  realizadas; e
- **Câmera**: não é obrigatória, mas uma *webcam* pode ser utilizada caso alguma
  aula extra seja feita de forma online.

### 4.4. Grau de dificuldade e esforço estimado
Tenha sempre em mente que esta disciplina é extensa e precisa de **dedicação**,
**estudo** e **atividades diárias** para que você consiga aprender tudo o que é
necessário. Em especial atente-se para o seguinte:

- **Nível**: esta disciplina é de nível introdutório a intermediário;
- **Língua**: as aulas, livros e materiais da disciplina são em **português**,
  mas alguns materiais (leituras e vídeos) estão em inglês. Os softwares
  utilizados estão, em sua maioria, em inglês (alguns oferecem   tradução para
  português);
- **Esforço total**: 10-15 horas de estudo por semana, **além da carga horária
  das aulas presenciais**, dependendo de seu conhecimento e habilidades prévias.
  Prepare-se para dedicar, em média, 1-2 horas diárias para leitura e realização
  das atividades programadas;
- **Leitura**: parte do esforço nessa disciplina é voltado para atividades de
  leitura. Prepare-se para ler bastante conteúdo online e, também, bastante
  documentação técnica em inglês; e
- **Trabalhos e atividades**: a maior parte do esforço nessa matéria é
  representada pelas atividades de diários de aprendizagem e trabalhos no
  Autolab (em especial, os **PSETs** são atividades que consumirão bastante
  tempo de dedicação).

Você já percebeu que esta disciplina precisa de um grau de **dedicação de tempo
e esforço** consideráveis. Mesmo assim, se você estiver gastando mais tempo do
que esforço total indicado acima, pode ser um sinal de que você precisa de ajuda
para entender melhor o material. Entre imediatamente em contato com o professor,
não deixe acumular dúvidas.

Eu espero que você, como estudante universitário[^7], esteja buscando aprender o
máximo possível e fazendo todo esforço para se dedicar nas atividades propostas e
aprender por conta própria de acordo com as orientações do professor. Lembre-se:
a única maneira de aprender é estudar! Leia os textos indicados abaixo para saber o
que faz a diferença no momento de estudar:

[^7]: O estudo em nível universitário é **muito diferente** do estudo em nível de ensino médio. Na universidade você terá que ler muito e aprender muita coisa por conta própria. Não espere que o professor vá passar todo o conteúdo mastigado e resumido para você decorar para a prova, essa vida acabou!

- [Como estudar? Dicas ao estudante iniciante](https://www.abrantes.pro.br/2020/08/09/como-estudar-dicas-ao-estudante-iniciante/)
- [O problema é o tamanho do lápis](https://www.abrantes.pro.br/2020/06/13/o-problema-e-o-tamanho-do-lapis/)
- [Você gasta sua borracha?](https://www.abrantes.pro.br/2020/10/24/voce-gasta-sua-borracha/)

Eu também espero que você seja um **estudante** e não um **aluno**. E que você
tenha **brio**, seja **bravo**, **persistente** e **resiliente** para encarar
o desafio! Assista os pequenos vídeos indicados a seguir para saber a diferença
entre aluno e estudante, e para saber a necessidade de brio para estudar:

- [Aluno ou estudante?](https://www.youtube.com/watch?v=SOQedoCAoLI) Do
  professor Pierluigi Piazzi; e
- [Você tem brio?](https://www.youtube.com/watch?v=TRPBY_lxJfE) Do professor
  Clovis de Barros Filho (desconsidere os palavrões, assista até o final!)

Para saber como **vencer a procrastinação e manter o estudo em dia**, assista
ao seguinte vídeo (ative as legendas em português se necessário):

- [Why we procrastinate?](https://www.youtube.com/watch?v=WD440CY2Vs0) de Vik
  Nithy.


## 3. Dinâmica da disciplina
Esta disciplina tem carga horária total de 60 horas semestrais (40h presenciais
e 20h online) e está dividida em **aulas**, **monitorias**, **tutorias**,
**diários de aprendizagem**, **exercícios**, **laboratórios** e **PSETs** (estes
três últimos realizados no Autolab).

### 3.1. Aulas
Cada turma terá 1 (uma) aula presencial por semana, com 1:40h de duração,
conforme o calendário da UVV (consulte a seção específica de sua turma para
ver os dias/horários de sua turma). A presença nas aulas é obrigatória e terá
peso na nota da disciplina. 
  
{: .attention }
Conforme normas da UVV você pode acumular até 10 horas de faltas, o que
corresponde a perder 5 dias de aula. Caso você ultrapasse as 10 horas (ou 5
dias) de faltas você será automaticamente reprovado na disciplina, sem
possibilidade de recurso. O professor tem liberdade de escolher a política de
tomada de presença que melhor lhe convier (por exemplo: fazer uma única
chamada durante a aula, fazer uma chamada no início e outra no final, utilizar
listas em papel ou o sistema online).

### 3.2. Monitorias
Cada turma terá, além das horas de aula normais, até 6 horas de monitoria por
semana, com um aluno monitor (um aluno que já passou pela disciplina e agora
ajuda aos que estão começando). As monitorias são realizadas no período
vespertino, conforme calendário específico de cada turma. A presença em, pelo
menos, 2 horas semanais de monitoria é obrigatória e terá peso na nota da
disciplina. Os monitores farão o seguinte:

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
que devem ser sanadas com os monitores. Como a participação nas monitorias é
fundamental para seu aprendizado, é obrigatório que você participe de, pelo
menos, 2 horas de monitoria por semana (você pode participais de mais horas
e/ou dias de monitoria, se houver vaga). Você não será reprovado se faltar às
monitorias, mas perderá pontuação na nota da disciplina.

### 3.3. Tutorias
Além de poder participar das monitorias, juntamente com seus colegas, você pode
marcar tutorias com o professor. As tutorias são pequenas reuniões (presenciais
ou online) que você faz, de modo individual ou em pequenos grupos, com o
professor, para esclarecimento de dúvidas ou busca de ajuda. A participação nas
tutorias é opcional.

{: .attention }
As tutorias têm duração de 20 minutos e devem ser agendadas previamente. O
calendário e a forma de agendamento serão divulgadas no momento oportuno.

### 3.4. Diários de aprendizagem
São exercícios discursivos sobre o conteúdo da matéria. Praticamente em todas as
semanas você receberá um arquivo PDF com as questões discursivas referentes ao
conteúdo da semana. Esse arquivo deve ser **impresso e respondido de forma
manuscrita**, e entregue para seu monitor nas datas especificadas. Os diários
também têm peso na nota da disciplina.
    
{: .attention }
Os **diários de aprendizagem** são uma ferramenta poderosa de estudo e
auto-avaliação. Eles serão vistoriados pelos monitores e/ou professor, mas
não serão corrigidos. Todas as dúvidas e dificuldades nos exercícios dos
diários devem ser discutidas com os monitores nos dias de monitoria. Verifique
no calendário de sua turma as datas de entrega dos diários, para não perder
pontos por atraso.

### 3.5. Atividades no Autolab
Durante todo o curso você fará diversas atividades de programação para a
resolução de problemas nos mais variados campos do conhecimento humano. Apesar
de você programar as soluções para os problemas, o foco não é em aprender uma ou
outro linguagem de programação mas, sim, aprender computação. Essas atividades
no Autolab são divididas em três grupos:

* **Exercícios**: são tarefas básicas e relativamente fáceis de programação,
  geralmente para ajudar a fixar um conceito ou uma técnica;
* **Laboratórios (labs)**: são tarefas mais complexas de programação, que
  envolverão mais raciocínio e compreensão mais profunda da matéria; e
* **PSETs**: são problemas extremamente difíceis que desafiarão toda sua
  capacidade de resolução e pensamento computacional. Prepare-se para gastar
  várias horas por semana na resolução dos PSETs.
  
{: .attention }
Todas as atividades no Autolab **são obrigatórias** e valerão um peso
considerável da nota da disciplina. Além disso a entrega de cada atividade é
rigorosamente controlada: entregas em atrasos podem ter a pontuação
severamente prejudicada e/ou zerada. Verifique no calendário de sua turma as
datas de entrega de cada atividade no Autolab.

{: .cuidado }
> Todas as atividades de programação enviadas para o Autolab são analisadas para
> a detecção de plágio e/ou cola e/ou cópia de código da Internet. A verificação
> é feita através de dois sistemas altamente sofisticados:
>
> * [MOSS: Measure of Software Similarity](http://moss.stanford.edu/), da
>   Universidade de Stanford; e
> * [COMPARE50: Similarity in Code](https://tinyurl.com/compare50), da
>   Universidade de Harvard.
>
> Esses sistemas são extremamente sofisticados e detectam plágio e/ou cópia de
> código mesmo que você tente disfarçar ou modificar o programa (trocar nomes de
> variáveis, mudar a indentação, reescrever comentários, etc.). Por favor, **não
> tente a sorte**: você não vencerá os softwares, receberá nota 0 (zero) na
> atividade e poderá ser encaminhado para a coordenação para as sanções
> disciplinares previstas nas regras da UVV.

## 4. O que esperamos de você?
Nós esperamos que você:

* Esteja presente em todas as aulas (prestando atenção e participando ativamente
  das discussões);
* Esteja presente em, pelo menos, 2 horas semanais de monitoria (grosso modo uma
  tarde por semana). Você pode até participar de mais horas de monitoria, se
  sentir necessidade e houver disponibilidade de vaga);
* Faça e entregue todos os diários de aprendizagem para análise do monitor e/ou
  professor;
* Faça todos os exercícios e laboratórios no Autolab;
* Faça todos os PSETs (no momento temos 6 no cronograma); e
* Siga todas as normas de integridade acadêmica da disciplina.



---
**Notas:**
