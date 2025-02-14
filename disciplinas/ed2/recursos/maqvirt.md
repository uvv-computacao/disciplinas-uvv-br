---
layout: page
title: Instalação do Desktop Virtual Linux 1.0
grand_parent: Estrutura de Dados II
parent: Recursos
has_children: false
has_toc: true
nav_exclude: false
nav_order: 10
last_modified_date: 2025-02-14 08:12 -0300
---

# Instalação do Desktop Virtual Linux
{:.no_toc}


## Sumário
{: .no_toc .text-delta }

* TOC
{:toc}

## 1. Instalação do sistema de virtualização
Faça o download do [sistema de virtualização
**vmware**](/disciplinas/ed2/recursos/#softwares-de-virtualizao) apropriado para
seu sistema operacional. A instalação é padrão.

## 2. Download da máquina virtual
Faça o download do [arquivo compactado de instalação do desktop
virtual](/disciplinas/ed2/recursos/#desktop-virtual-linux). Salve esse arquivo
(`desktop-1.0.rar`) em algum diretório em seu computador. **Importante**: o
arquivo tem cerca de 13 GB de tamanho e, portanto, você deve garantir que seu
computador tenha, pelo menos, 30 GB de espaço livre em disco para fazer a
instalação.

## 3. Descompactar o arquivo da máquina virtual
Depois que você está com o sistema de virtualização instalado e que você fez o
download do arquivo de instalação do Desktop Virtual Linux 1.0, você deve
descompactar esse arquivo de instalação (o arquivo está compactado no formato
RAR; use o [WinRAR](https://www.win-rar.com), [rar](https://www.rarlab.com) ou
outro descompactador). Ao descompactar será criado o diretório
**`desktop-1.0`**, com os arquivos de instalação. Depois disso você pode apagar
o arquivo RAR para liberar espaço em seu computador. A imagem a seguir demonstra
esse processo utilizando um computador Linux como demonstração:

![Descompactar e apagar](/assets/maqvirt/dl1/01.png)

## 4. Importação da máquina virtual
Agora você deve importar os arquivos do Desktop Virtual Linux para o sistema de
virtualização.

Em primeiro lugar, abra o sistema de virtualização e, no menu *File*, clique em
*Open*:

![Menu open](/assets/maqvirt/dl1/02.png)

Usando a caixa de diálogo, vá até o diretório **`desktop-1.0`**, escolha o
arquivo **`desktop-1.0.ovf`** e clique no botão *Open*:

![Arquivo da máquina virtual](/assets/maqvirt/dl1/03.png)

Agora você deve informar um nome para a máquina virtual e escolher o diretório
onde ela será instalada. Recomenda-se manter as configurações padrão, mas você
pode escolher qualquer coisa adequada ao seu sistema:

![Nome e diretório](/assets/maqvirt/dl1/04.png)

Se tudo correu bem, a importação da máquina virtual começará (tenha paciência):

![Importação da MV](/assets/maqvirt/dl1/05.png)

Se a importação ocorrer sem erros, você verá a máquina virtual disponível no
sistema de virtualização:

![Pós-importação](/assets/maqvirt/dl1/06.png)

**Atenção agora**: por padrão o Desktop Virtual Linux 1.0 está configurado para
utilizar 8 GB de memória RAM e 4 processadores (cores). Se seu computador não
tem pelo menos 16 GB de memória e/ou não tem mais do que 4 cores, você precisará
diminuir esses parâmetros na configuração da máquina virtual. Se esse for seu
caso, clique com o botão direito no nome da máquina e escolha a opção
*Settings*:

![Configuração geral](/assets/maqvirt/dl1/07.png)

Nas configurações você pode diminuir a quantidade de memória RAM disponível para
a máquina virtual:

![Configuração RAM](/assets/maqvirt/dl1/08.png)

E também pode diminuir a quantidade de cores disponíveis:

![Configuração Cores](/assets/maqvirt/dl1/09.png)

Depois de acertar as configurações, basta iniciar a máquina virtual:

![Máquina instalada](/assets/maqvirt/dl1/10.png)

Por último, para liberar espaço em disco, você pode remover o diretório com os
arquivos de instalação da máquina virtual:

![Limpeza de arquivos](/assets/maqvirt/dl1/11.png)

## 5. Em caso de problemas
Se você tiver algum problema, entre em contato com os monitores da disciplina ou
com o professor.
