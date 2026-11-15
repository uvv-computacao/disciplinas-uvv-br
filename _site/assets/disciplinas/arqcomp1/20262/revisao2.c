#include <CRpaic.h>
#include <float.h>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>

/* Constantes simbólicas */
#define QTDREF 2
#define IMIN 0
#define IMAX 1
#define TMIN 2.0
#define TMAX 8.0
#define LOTE_MIN 1
#define LOTE_MAX 1000
#define CORRECAO 0.5
#define TEMPMIN -100.0
#define TEMPMAX 100.0
#define SENSORMIN -10.0
#define SENSORMAX 10.0

/* Tipos de dados */
struct st_resultado
{
    double media;
    double minima;
    double maxima;
    int qtd_alertas;
    int qtd_analises;
};
typedef struct st_resultado resultado_t;

/* Variáveis globais */
double const limites_temperatura[QTDREF] = {TMIN, TMAX};
double correcao_sensor = CORRECAO;
int total_alertas;
double soma_temperaturas;

/* Protótipos das funções */
void registrar_temperaturas (double *medicoes, int qtd_medicoes);
resultado_t analisar_temperaturas (double const *medicoes, int qtd_medicoes);
void exibir_relatorio (int qtd_medicoes, resultado_t resultado);

/* FUNÇÃO MAIN */
int main (void)
{
    printf("%s\n", "=== MONITORAMENTO DE TEMPERATURA ===");

    int qtd_medicoes;
    char stop;

    do
    {
        do
        {
            qtd_medicoes = get_int("\nQuantidade de medições: ");
        }
        while (qtd_medicoes < LOTE_MIN || qtd_medicoes > LOTE_MAX);

        double *medicoes = malloc(sizeof(*medicoes) * (size_t) qtd_medicoes);
        if (!medicoes)
        {
            fprintf(stderr, "ERRO: não foi possível alocar a memória.\n");
            return EXIT_FAILURE;
        }

        do
        {
            correcao_sensor = get_double("Correção do sensor (°C): ");
        }
        while (!isfinite(correcao_sensor)  ||
               correcao_sensor < SENSORMIN || correcao_sensor > SENSORMAX);
        
        registrar_temperaturas(medicoes, qtd_medicoes);
        resultado_t resultado = analisar_temperaturas(medicoes, qtd_medicoes);

        free(medicoes);
        medicoes = NULL;

        exibir_relatorio(qtd_medicoes, resultado);
        
        stop = get_char("\nDeseja analisar outro lote (S/N)? ");
    }
    while (stop == 'S' || stop == 's');

    printf("\nPrograma encerrado.\n");
    return EXIT_SUCCESS;
}

/* Implementação das funções */
void registrar_temperaturas (double *medicoes, int qtd_medicoes)
{
    printf("\n");
    double temp = 0;
    for (int i = 0; i < qtd_medicoes; i++)
    {
        do
        {
            temp = get_double("Temperatura %d: ", i + 1);
        }
        while (!isfinite(temp) ||
               temp < TEMPMIN || temp > TEMPMAX);
        medicoes[i] = temp + correcao_sensor;
    }
}

resultado_t analisar_temperaturas (double const *medicoes, int qtd_medicoes)
{
    static int total_analises = 0;
    total_alertas = 0;

    resultado_t resultado = {0};
    soma_temperaturas = 0.0;
    double tempmin = DBL_MAX;
    double tempmax = -DBL_MAX;

    for (int i = 0; i < qtd_medicoes; i++)
    {
        if (medicoes[i] < tempmin)
            tempmin = medicoes[i];
        if (medicoes[i] > tempmax)
            tempmax = medicoes[i];
        if (medicoes[i] < limites_temperatura[IMIN] ||
            medicoes[i] > limites_temperatura[IMAX])
            total_alertas++;
        soma_temperaturas += medicoes[i];
    }

    total_analises++;

    resultado.media = soma_temperaturas / (double) qtd_medicoes;
    resultado.minima = tempmin;
    resultado.maxima = tempmax;
    resultado.qtd_alertas = total_alertas;
    resultado.qtd_analises = total_analises;

    return resultado;
}

void exibir_relatorio (int qtd_medicoes, resultado_t resultado)
{
    printf("\n");
    printf("=== RELATÓRIO ===\n");
    printf("Total de medições coletadas : %d\n", qtd_medicoes);
    printf("Temperatura mínima permitida: %.2f °C\n",
           limites_temperatura[IMIN]);
    printf("Temperatura máxima permitida: %.2f °C\n",
           limites_temperatura[IMAX]);
    printf("Correção aplicada ao sensor : %.2f °C\n", correcao_sensor);
    printf("\nTemperatura média: %.2f °C\n", resultado.media);
    printf("Menor temperatura: %.2f °C\n", resultado.minima);
    printf("Maior temperatura: %.2f °C\n", resultado.maxima);
    printf("Medições problemáticas: %d\n", resultado.qtd_alertas);
    printf("Percentual de alertas : %.2f %%\n",
           (double) resultado.qtd_alertas / (double) qtd_medicoes * 100.0);
    printf("\nTotal de análises: %d\n", resultado.qtd_analises);
}
