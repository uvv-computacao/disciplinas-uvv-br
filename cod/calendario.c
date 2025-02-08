/*
 * Imprime a tabela padrão para o calendário prevista dos turmas,
 * para ser colocado no site Disciplinas UVV.
 * Abrantes Araújo Silva Filho
 */
#define _XOPEN_SOURCE
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

/* DEFINIÇÕES E VARIÁVEIS GLOBAIS */
#define INICIO "2025-02-02 00:00:00"    /* Início em um DOMINGO */
#define FIM    "2025-07-05 00:00:00"    /* Final em um SÁBADO */
char diames[6];                         /* Armazenará string com dd/mm */

/* PROTÓTIPOS DOS SUBPROGRAMAS */
long soma_dias(int dias);
char *dia_da_semana (struct tm *data);
void set_diames (struct tm *data);

/* INICIA O PROGRAMA */
int main(void)
{
    struct tm inicio;
    struct tm fim;
    struct tm *atual = NULL;

    memset(&inicio, 0, sizeof(struct tm));
    memset(&fim, 0, sizeof(struct tm));

    strptime(INICIO, "%Y-%m-%d %H:%M:%S", &inicio);
    strptime(FIM, "%Y-%m-%d %H:%M:%S", &fim);

    if (inicio.tm_wday != 0)
    {
	printf("Erro! A data de início deve ser um domingo.\n");
	exit(EXIT_FAILURE);
    }
    else if (fim.tm_wday != 6)
    {
	printf("Erro! A data de fim deve ser um sábado.\n");
	exit(EXIT_FAILURE);
    }

    time_t data1 = mktime(&inicio);
    time_t data2 = mktime(&fim);

    if (data1 >= data2)
    {
	printf("Erro! A data inicial não pode ser maior do que a final.\n");
	exit(EXIT_FAILURE);
    }

    int diff = (int) (difftime(data2, data1) / (60 * 60 * 24));
    int semanas = (diff + 1) / 7;

    // Imprime início da tabela
    printf("<table class=\"table table-bordered schedule-table\">\n");
    printf("  <thead>\n");
    printf("    <tr>\n");
    printf("      <th class=\"center schedule-week-num\">Semana</th>\n");
    printf("      <th>Data</th>\n");
    printf("      <th>Aula</th>\n");
    printf("      <th>Estudo</th>\n");
    printf("      <th>Autolab</th>\n");
    printf("      <th><i>Hand out</i></th>\n");
    printf("      <th><i>Hand in</i></th>\n");
    printf("    </tr>\n");
    printf("  </thead>\n");
    printf("  <tbody class=\"js-scheduleContent\">\n");

    // Imprime o corpo da tabela
    for (int i = 1; i <= semanas; i++)
    {
	printf("\n    <!-- %iª SEMANA -->\n", i);
	for (int ds = 0; ds <= 6; ds++)
	{
	    atual = gmtime(&data1);
	    set_diames(atual);
	    if (ds == 1)
	    {
		printf("    <tr>\n");
		printf("      <td rowspan=5>%i</td> <!-- Número da semana-->\n", i);
		printf("      <th>%s<br />%s</th> <!-- Dia e Data -->\n", dia_da_semana(atual), diames);
		printf("      <td></td> <!-- Aula -->\n");
		printf("      <td></td> <!-- Estudo -->\n");
		printf("      <td></td> <!-- Autolab -->\n");
		printf("      <td></td> <!-- Hand out -->\n");
		printf("      <td></td> <!-- Hand in -->\n");
		printf("    </tr>\n");
	    }
	    else if (ds >= 2 && ds <= 5)
	    {
		printf("    <tr>\n");
                printf("      <th>%s<br />%s</th> <!-- Dia e Data -->\n", dia_da_semana(atual), diames);
                printf("      <td></td> <!-- Aula -->\n");
                printf("      <td></td> <!-- Estudo -->\n");
                printf("      <td></td> <!-- Autolab -->\n");
                printf("      <td></td> <!-- Hand out -->\n");
                printf("      <td></td> <!-- Hand in -->\n");
                printf("    </tr>\n");
	    }
	data1 += soma_dias(1);
	}
    }

    // Imprime fim da tabela
    printf("  </tbody>\n");
    printf("</table>\n");

    // Finaliza programa
    exit(EXIT_SUCCESS);
}


long soma_dias(int dias)
{
    return dias * (24 * 60 * 60);
}

char *dia_da_semana (struct tm *data)
{
    switch (data->tm_wday)
    {
        case 0:
	    return "Dom";
	    break;
	case 1:
	    return "Seg";
	    break;
	case 2:
	    return "Ter";
	    break;
	case 3:
	    return "Qua";
	    break;
	case 4:
	    return "Qui";
	    break;
	case 5:
	    return "Sex";
	    break;
	case 6:
	    return "Sáb";
	    break;
    }
    return "";
}

void set_diames (struct tm *data)
{
    sprintf(diames, "%i/%i", data->tm_mday, data->tm_mon + 1);
}
