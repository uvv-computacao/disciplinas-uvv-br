#!/bin/bash
#
# Script para criar a estrutura de diretório de uma DISCIPLINA e,
# dentro da disciplinas, das TURMAS de um determinado semestre.
#
# Para rodar: AJUSTE AS VARIÁVEIS ABAIXO e execute o script,
# DE DENTRO DO RAIZ DO JEKYLL!
# Sim, curto grosso mesmo...

nome_disciplina="Fundamentos da Computação"
nome_disciplina_abreviado="fc"
nome_dir_disciplina="fundamentos_computacao"
nome_dir_disciplina_abreviado="fundcomp"
ano="2023"
semestre="1"
turmas="cc1nb si1nb"

# Você está dentro do Jekyll do Disciplinas UVV?
GEMFILE="Gemfile"
CONFIGFILE="_config.yml"
if [[ ! -f "$GEMFILE" || ! -f "$CONFIGFILE" ]]; then
    echo "Arquivo $GEMFILE e/ou $CONFIGFILE não encontrado, você NÃO ESTÁ no diretório raiz do"
    echo "Jekyll para o site Disciplinas UVV. LEIA A DOCUMENTAÇÃO dentro do próprio script."
    echo "Em protesto, vou parar de executar. Moriturus te saluto!"
    exit
fi

# Diretório e arquivos iniciais para a disciplina:
if [[ ! -d disciplinas/$nome_dir_disciplina ]]; then
    mkdir disciplinas/$nome_dir_disciplina;
    mkdir -p assets/disciplinas/${nome_dir_disciplina_abreviado}/${ano}_${semestre}
    mkdir -p assets/images/posts/${nome_dir_disciplina_abreviado}
    mkdir -p _avisos/${nome_dir_disciplina_abreviado}/${ano}${semestre}
    echo "Diretório disciplinas/$nome_dir_disciplina criado."

    for i in index.md leituras.md recursos.md syllabus.md pessoal.md
    do
        cp modelos/$i disciplinas/$nome_dir_disciplina;
	sed -i "s/NOME-DA-DISCIPLINA/$nome_disciplina/g" disciplinas/$nome_dir_disciplina/$i
	if [[ -f disciplinas/$nome_dir_disciplina/pessoal.md ]]; then
	    sed -i "s/SEMESTRE-DISCIPLINA/${ano}${semestre}-${nome_disciplina_abreviado}/g" disciplinas/$nome_dir_disciplina/$i;
	fi
	echo "Página $i criada.";
    done

    for i in $turmas
    do
        mkdir disciplinas/$nome_dir_disciplina/${ano}${semestre}_${i};
	echo "Diretório da turma ${ano}${semestre}_${i} criado.";

	for j in index.md avisos.md calendario.md horario.md
	do
	    cp modelos/turmas/$j disciplinas/$nome_dir_disciplina/${ano}${semestre}_${i};
	    sed -i "s/NOME-DA-DISCIPLINA/$nome_disciplina/g" disciplinas/$nome_dir_disciplina/${ano}${semestre}_${i}/$j
	    if [ $i == "cc1m" ]; then
		texto="${ano}/${semestre} - Turma CC1M";
	        sed -i "s@NOME-DA-TURMA@$texto@g" disciplinas/$nome_dir_disciplina/${ano}${semestre}_${i}/$j;
		for k in index.md avisos.md;
		do
		    if [ "$j" = "$k" ]; then
		        sed -i "s@ANOSEMESTRE@${ano}${semestre}@g" disciplinas/$nome_dir_disciplina/${ano}${semestre}_${i}/$j;
		        sed -i "s@TURMA@${i}@g" disciplinas/$nome_dir_disciplina/${ano}${semestre}_${i}/$j;
		    fi
		done
	    elif [ $i == "cc1mb" ]; then
		texto="${ano}/${semestre} - Turma CC1Mb"
	        sed -i "s@NOME-DA-TURMA@$texto@g" disciplinas/$nome_dir_disciplina/${ano}${semestre}_${i}/$j
		for k in index.md avisos.md;
		do
		    if [ "$j" = "$k" ]; then
		        sed -i "s@ANOSEMESTRE@${ano}${semestre}@g" disciplinas/$nome_dir_disciplina/${ano}${semestre}_${i}/$j;
		        sed -i "s@TURMA@${i}@g" disciplinas/$nome_dir_disciplina/${ano}${semestre}_${i}/$j;
		    fi
		done
	    elif [ $i == "cc1mc" ]; then
		texto="${ano}/${semestre} - Turma CC1Mc"
	        sed -i "s@NOME-DA-TURMA@$texto@g" disciplinas/$nome_dir_disciplina/${ano}${semestre}_${i}/$j
		for k in index.md avisos.md;
		do
		    if [ "$j" = "$k" ]; then
		        sed -i "s@ANOSEMESTRE@${ano}${semestre}@g" disciplinas/$nome_dir_disciplina/${ano}${semestre}_${i}/$j;
		        sed -i "s@TURMA@${i}@g" disciplinas/$nome_dir_disciplina/${ano}${semestre}_${i}/$j;
		    fi
		done
	    elif [ $i == "cc1md" ]; then
		texto="${ano}/${semestre} - Turma CC1Md"
	        sed -i "s@NOME-DA-TURMA@$texto@g" disciplinas/$nome_dir_disciplina/${ano}${semestre}_${i}/$j
		for k in index.md avisos.md;
		do
		    if [ "$j" = "$k" ]; then
		        sed -i "s@ANOSEMESTRE@${ano}${semestre}@g" disciplinas/$nome_dir_disciplina/${ano}${semestre}_${i}/$j;
		        sed -i "s@TURMA@${i}@g" disciplinas/$nome_dir_disciplina/${ano}${semestre}_${i}/$j;
		    fi
		done
	    elif [ $i == "cc1n" ]; then
		texto="${ano}/${semestre} - Turma CC1N"
	        sed -i "s@NOME-DA-TURMA@$texto@g" disciplinas/$nome_dir_disciplina/${ano}${semestre}_${i}/$j
		for k in index.md avisos.md;
		do
		    if [ "$j" = "$k" ]; then
		        sed -i "s@ANOSEMESTRE@${ano}${semestre}@g" disciplinas/$nome_dir_disciplina/${ano}${semestre}_${i}/$j;
		        sed -i "s@TURMA@${i}@g" disciplinas/$nome_dir_disciplina/${ano}${semestre}_${i}/$j;
		    fi
		done
	    elif [ $i == "cc1nb" ]; then
		texto="${ano}/${semestre} - Turma CC1Nb"
	        sed -i "s@NOME-DA-TURMA@$texto@g" disciplinas/$nome_dir_disciplina/${ano}${semestre}_${i}/$j
		for k in index.md avisos.md;
		do
		    if [ "$j" = "$k" ]; then
		        sed -i "s@ANOSEMESTRE@${ano}${semestre}@g" disciplinas/$nome_dir_disciplina/${ano}${semestre}_${i}/$j;
		        sed -i "s@TURMA@${i}@g" disciplinas/$nome_dir_disciplina/${ano}${semestre}_${i}/$j;
		    fi
		done
	    elif [ $i == "si1n" ]; then
		texto="${ano}/${semestre} - Turma SI1N"
	        sed -i "s@NOME-DA-TURMA@$texto@g" disciplinas/$nome_dir_disciplina/${ano}${semestre}_${i}/$j
		for k in index.md avisos.md;
		do
		    if [ "$j" = "$k" ]; then
		        sed -i "s@ANOSEMESTRE@${ano}${semestre}@g" disciplinas/$nome_dir_disciplina/${ano}${semestre}_${i}/$j;
		        sed -i "s@TURMA@${i}@g" disciplinas/$nome_dir_disciplina/${ano}${semestre}_${i}/$j;
		    fi
		done
	    elif [ $i == "si1nb" ]; then
		texto="${ano}/${semestre} - Turma SI1Nb"
	        sed -i "s@NOME-DA-TURMA@$texto@g" disciplinas/$nome_dir_disciplina/${ano}${semestre}_${i}/$j
		for k in index.md avisos.md;
		do
		    if [ "$j" = "$k" ]; then
		        sed -i "s@ANOSEMESTRE@${ano}${semestre}@g" disciplinas/$nome_dir_disciplina/${ano}${semestre}_${i}/$j;
		        sed -i "s@TURMA@${i}@g" disciplinas/$nome_dir_disciplina/${ano}${semestre}_${i}/$j;
		    fi
		done
	    fi
	    echo "Página $j criada.";
	done
    done

fi
