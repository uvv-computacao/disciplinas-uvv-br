---
layout: page
title: Syllabus
nav_exclude: false
parent: Bancos de Dados 1
nav_order: 05
has_children: false
---

# Syllabus
{:.no_toc}

Além do material oficial que está disponível no Portal do Aluno da UVV
(Universidade de Vila Velha), este documento contém mais detalhes sobre
a dinâmica da disciplina **Design e Desenvolvimento de Bancos de
Dados I**, para todas as deste semestre (2023/1). Leia-o com atenção e procure o
professor para esclarecer qualquer dúvida. Note que este *syllabus* não é um
documento "oficial": é um material extra, preparado pelo professor da disciplina
para proporcionar informações adicionais importantes para os alunos.

## Sumário
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## Visão geral da disciplina

Olá, seja muito bem-vindo!

Esta é a disciplina **Design e Desenvolvimento de Bancos de Dados I**, para os
cursos de Ciência da Computação e Sistemas de Informação da Universidade de Vila
Velha (UVV).

Esta disciplina é uma introdução aos conceitos fundamentais necessários para
projetar, usar e implementar sistemas de bancos de dados e aplicações de bancos
de dados, através de uma abordagem profunda e atualizada dos aspectos mais
importantes dos sistemas e aplicações de bancos de dados, bem como das tecnologias
relacionadas.

Nesta disciplina você terá o primeiro contato com os **bancos de dados** e também
com os **sistemas de gerenciamento de bancos de dados** *open-source* (tais como o
MySQL, MariaDB e o PostgreSQL) e comerciais (tais como o Oracle Database e
o Microsoft SQL Server).

Você aprenderá a projetar e implementar um banco de dados através de técnicas
de modelagem conceitual, lógica e física, de tal forma que o banco de dados seja
adequado para a tomada de decisões e com boa performance para uso no mundo
real. Também estudará o modelo relacional de dados, a linguagem SQL (*Structured
Query Language*), álgebra relacional, técnicas de normalização, bancos de dados de
objeto, XML, modelo de dados entidade-relacionamento e muito mais!

Além disso esta disciplina também contribuirá para que você desenvolva suas
habilidades de **pensamento computacional** quando você estiver aprendendo a
modelar bancos de dados: 1) você precisará **decompor** um problema complexo em
problemas menores, mais gerenciáveis; 2) você precisará usar técnicas de
**abstração** para se focar nas partes essenciais dos problemas, ignorando detalhes
irrelevantes; 3) você começará a usar técnicas de **reconhecimento de padrões**
para pensar em como resolver problemas; e 4) você começará a entender sobre
**algoritmos** e linguagens.

Em resumo, esta disciplina é sua porta de entrada para o fantástico mundo dos
bancos de dados.

Prepare-se, pois esta disciplina é muito **extensa**, **árdua** e **difícil**,
mas o resultado, se você se dedicar conforme descrito neste plano de ensino,
será recompensador!

## Pré-requisitos
- **Obrigatórios**:
  - **Matemática**: familiaridade e conforto com, pelo menos, a matemática
    do ensino médio (aritmética, álgebra, funções). Caso sua base matemática
    seja fraca, veja o texto [Preparação para graduação em áreas exatas:
    matemática além do básico](https://www.abrantes.pro.br/2020/05/20/preparacao-para-graduacao-em-areas-exatas-matematica-alem-do-basico/), com dicas para estudar novamente a matemática, do jeito certo;
  - **Computador**: você deve ter um computador com acesso a internet
    (câmera, microfone e caixas de som são recomendados) e com capacidade
    suficiente para instalar e executar os softwares que serão utilizados (um
    computador recente, com arquitetura Intel x86 de 64 bits, com Linux, Windows
    ou Mac, com 8 GiB de memória RAM e bastante espaço em disco). Verifique a
    Seção XXXXXXXXXXXXXXXX para maiores detalhes.
- **Desejáveis**:
  - **Inglês**: a maioria dos livros e leituras obrigatórias da disciplina estarão em
    português mas, excepcionalmente, algumas leituras opcionais em inglês
    serão ser indicadas;
  - **SQL**: algum curso introdutório em SQL;
  - **Programação**: algum curso introdutório de programação, em qualquer
    linguagem.

## Objetivos do curso e resultados esperados

### Objetivos de aprendizagem
- Aprender noções fundamentais sobre bancos de dados (banco de dados, sistemas de
  gerenciamento de bancos de dados, características de um sistema de bancos de dados,
  vantagens e desvantagens);
- Aprender o que é modelo de dados, a arquitetura dos bancos de dados, quais
  as linguagens e interfaces de acesso aos dados, e arquitetura cliente/servidor;
- Entender o modelo relacional de dados e suas restrições, bem como as operações de
  atualização, tansações e tratamento de violações de restrições;
- Aprender a usar comandos SQL básicos (select, insert, update, delete);
- Aprender a usar *queries* SQL mais avançadas (joins, triggers, views) e alterações
  no esquema de um banco de dados;
- Entender a relação entre a álgebra e o cálculo relacional com a SQL;
- Aprender a modelar um banco de dados utilizando o modelo entidade-relacionamento (ER);
- Aprender o modelo entidade-relacionamento estendido (EER) para trabalhar com subclasses,
  herança, especialização, generalização e conceitos relacionados;
- Aprender a mapear um modelo conceitual (ER ou EER) para o modelo relacional;
- Entender dependências funcionais e como normalizar um modelo relacional,
  sabendo usar diversas formas normais;
- Aprender sobre regras de inferência, equivalência, cobertura, algoritmos e
  decomposições relacionais;
- Aprender sobre sistemas de gerenciamento de bancos de dados de objeto e
  objeto-relacional;
- Diferenciar dados estruturados de não estruturados, sabendo utilizar modelos
  de dados hierárquicos da XML;
- Aprender as técnicas básicas de programação SQL (SQL embutida, SQL dinâmica
  e SQLJ); e
- tilizar bancos de dados na web através de um exemplo com PHP.

### Habilidades a serem adquiridas
- Projetar e modelar bancos de dados (modelos conceitual, lógico e físico);
- Implementar bancos de dados em diversos sistemas de gerenciamento de bancos
  de dados (MySQL, MariaDB, PostgreSQL, Oracle e SQL Server);
- Utilizar um sistema Linux para acesso aos bancos de dados, principalmente
  o uso da linha de comando;
- Aprender as interfaces de linha de comando para acesso aos bancos de dados;
- Aprender uma ferramenta gráfica para acesso a diversos bancos de dados (uti-
  lizaremos a [DBeaver](https://dbeaver.io/));
- Aprender uma ferramenta web para acesso a um banco de dados (utilizaremos
  o [phpMyAdmin](https://www.phpmyadmin.net/)); e
- Aprender uma ferramenta gráfica dedicada para acesso a um banco de dados
  (utilizaremos o [pgAdmin](https://www.pgadmin.org/)).

## Estrutura e informações sobre a disciplina

### Professor
Olá, meu nome é Abrantes Araújo Silva Filho e serei o professor responsável
pela sua turma. Algumas informações importantes:

- Sou graduado em **medicina** pela [UFES](https://ufes.br/) (1999), mestre em
  **epidemiologia e métodos quantitativos em saúde** pela [FIOCRUZ](https://portal.fiocruz.br/) (2002)
  e graduado em **ciência da computação** pela [FAESA](https://www.faesa.br/) (2021).
  Atualmente sou estudante do bacharelado em matemática, na modalidade de
  ensino a distância (EAD).
- [www.linkedin.com/in/abrantes-filho](https://www.linkedin.com/in/abrantes-filho/)
- [github.com/abrantesasf](https://github.com/abrantesasf) e também [github.com/computacaoraiz](https://github.com/computacaoraiz)
- [www.abrantes.pro.br](https://www.abrantes.pro.br/) e também [www.computacaoraiz.com.br](https://www.computacaoraiz.com.br)
- [abrantesasf@uvv.br](mailto:abrantesasf@uvv.br)
- [www.youtube.com/computacaoraiz](https://www.youtube.com/computacaoraiz)
- [cursos.computacaoraiz.com.br](https://cursos.computacaoraiz.com.br)
- (27) 9-9991-4393, para entrar em contato via [Signal](https://signal.org/) ou
  [Telegram](https://telegram.org/). ATENÇÃO: **eu NÃO USO** WhatsApp!

### Monitores, assistentes e tutores
Oficialmente ainda não está confirmada a participação de nenhum monitor,
assistente ou tutor. Todas as atividades serão conduzidas diretamente pelo
professor, de modo presencial.

Extra-oficialmente, alunos mais avançados ou que já tenham experiência prévia
podem ser voluntários para atuar como monitores informais da turma, auxiliando
os alunos com menor experiência e/ou dificuldade.

Para mais informações, consulte a Seção XXXXXXXXXXXXXXXXXX.

### Datas e horários das aulas
O período 2023/1 se inicia no dia 01/02/2023 e termina no dia 04/07/2023.

Oficialmente cada turma tem 2 aulas obrigatórias por semana. Além disso,
caso um monitor seja oficialmente selecionado pela UVV, as turmas terão
à disposição um monitor durante todas as tardes da semana para discussões,
esclarecimento de dúvidas, auxílio em exercícios e tarefas e muito mais.

Cada turma também utilizará a plataforma **Cursos do Computação Raiz**,
no endereço [https://cursos.computacaoraiz.com.br](https://cursos.computacaoraiz.com.br).
Os alunos serão automaticamente matriculados no curso *CR6.180A: Introdução
ao Projeto e Sistemas de Bancos de Dados* e deverão assistir aos vídeos,
realizar as provas, as atividades, os PSETs (mais sobre isso em breve) e
tudo o mais que estiver agendado. ATENÇÃO: o curso CR6.180A faz parte da
nota para sua aprovação nesta disciplina!

Cada turma deve consultar o site [Disciplias UVV](https://disciplinas.uvv.br) e
verificar seu horário semanal e o cronograma previsto de aulas e conteúdo
para a disciplina.

Aulas extras podem ser necessárias para a reposição de aulas canceladas
por motivo de força maior. As aulas de reposição são oficiais e devem ser
aprovadas por, pelo menos, 75% dos alunos.

### Laboratório de computação e computador pessoal
A estrutura de laboratórios de computação da UVV é excelente, possuindo máquinas
com hardware e software padronizados que facilitam a realização das atividades.
Além disso o benefício mais importante de trabalhar no laboratório é obter ajuda
direta do professor, dos assistentes, e de seus próprios colegas de turma.

Entretanto, por limitações de tempo, você precisará realizar tarefas em seu
próprio computador pessoal. Veja aqui as configurações mínimas necessárias para
que você consiga realizar todas as tarefas em seu próprio computador:

- **Processador**: deve ter arquitetura INTEL x86, de 64 bits. Outras arquiteturas,
  como a ARM (MacBook Air M1, por exemplo), não são suportadas. Qualquer
  computador relativamente recente com processador Intel ou AMD já está adequado;
- **Memória**: no mínimo 8 GiB de memória RAM (16 GiB é recomendável);
- **Disco rígido**: pelo menos 50 GiB de espaço livre em disco (70 GiB durate
  a instalação da máquina virtual do curso);
- **Sistema operacional**: Linux, Windos ou Mac;
- **Monitor**: no mínimo um monitor HD (Full HD é recomendável). Seu monitor
  deve ser grande o suficiente para que você possa trabalhar com conforto.
  Se você tiver dois monitores poderá realizar as tarefas em um monitor e
  usar o outro para ler o conteu´do ou consultar a documentação sobre bancos
  de dados disponível na Internet;
- **Internet**: você deve ter uma conexão razoavelmente rápida para fazer o
  download da máquina virtual. Além disso você precisa assistir todas as
  aulas e realizar as tarefas do curso CR6.180A;
- **Som**: necessário para fazer as aulas do curso CR6.180A;
- **Microfone**: não é obrigatório, mas pode ser utilizado caso ocorram
  aulas online síncronas;
- **Câmera**: não é obrigatória, mas pode ser utilizada caso ocorram
  aulas online síncronas.

Se você tiver um notebook pode utilizá-lo durante as aluas de laboratório, ao invés
dos computadores da UVV. A vantagem de usar seu próprio notebook é que você terá
o mesmo ambiente, tanto na UVV quanto em casa, e poderá seguir os exercícios e
tarefas de modo contínuo.

### Grau de dificuldade e esforço estimado
Tenha sempre em mente que esta disciplina é extensa e precisa de **dedicação**,
**estudo e leitura diária** para que você consiga aprender tudo o que é necessário.
Em especial atente-se para o seguinte:

- **Nível**: esta disciplina é de nível introdutório a intermediário;
- **Língua**: as aulas, livros e materiais da disciplina são em **português**
  mas alguns materiais extras (leituras, e vídeos) estão em inglês. Os
  softwares utilizados estão, em sua maioria, em inglês (alguns oferecem
  tradução para português);
- **Esforço total**: 10-15 horas de estudo por semana, **além da carga horária das
  aulas presenciais**, dependendo de seu conhecimento e habilidades prévias.
  Prepare-se para dedicar, em média, 1-2 horas diárias para leitura e realização
  das atividades programadas;
- **Leitura**: parte do esforço nessa disciplina é voltado para atividades de
  leitura. Prepare-se para ler, em média, **35 páginas por semana** (variando de 18
  a 52 páginas por semana). Não se assuste com a quantidade pois há muitas
  ilustrações, exemplos e códigos de programação nos livros utilizados, fazendo
  com que a leitura não seja tão hercúlea assim. Mantenha as leituras em dia,
  conforme o cronograma. Acumular leituras é “fatal” para o aprendizado; e
- **Trabalhos e atividades**: a maior parte do esforço nessa matéria é representada
  pelos trabalhos, PSETs e atividades práticas que você realizará semanalmente.

Você já percebeu que esta disciplina precisa de um grau de **dedicação de tempo
e esforço** consideráveis. Mesmo assim, se você estiver gastando mais tempo do que
esforço total indicado acima, pode ser um sinal de que você precisa de ajuda para
entender melhor o material. Entre imediatamente em contato com o professor, não
deixe acumular dúvidas.

Eu espero que você, como estudante universitário , esteja buscando aprender o
máximo possível e fazendo todo esforço para se dedicar nas atividades propostas e
aprender por conta própria de acordo com as orientações do professor. Lembre-se:
a única maneira de aprender é estudar! Leia os textos indicados abaixo para saber o
que faz a diferença no momento de estudar:

- [Como estudar? Dicas ao estudante iniciante](https://www.abrantes.pro.br/2020/08/09/como-estudar-dicas-ao-estudante-iniciante/)
- [O problema é o tamanho do lápis](https://www.abrantes.pro.br/2020/06/13/o-problema-e-o-tamanho-do-lapis/)
- [Você gasta sua borracha?](https://www.abrantes.pro.br/2020/10/24/voce-gasta-sua-borracha/)

Eu também espero que você seja um **estudante** e não um **aluno**. E que você
tenha **brio**, seja **bravo**, **persistente** e **resiliente** para encarar
o desafio! Assista os pequenos vídeos indicados a seguir para saber a diferença
entre aluno e estudante, e para saber a necessidade de brio para estudar:

- [Aluno ou estudante?](https://www.youtube.com/watch?v=SOQedoCAoLI) Do professor
  Pierluigi Piazzi; e
- [Você tem brio?](https://youtu.be/qwgfEfGZP1s) Do professor Clovis de Barros
  Filho (desconsidere os palavrões)

Para saber como **vencer a procrastinação e manter o estudo em dia**, assista
ao seguinte vídeo (ative as legendas em português se necessário):

- [Why we procrastinate?](https://www.youtube.com/watch?v=WD440CY2Vs0) de Vik Nithy.

