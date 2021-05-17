# Primeiramente temos que ler o arquivo em txt
arquivo = open('./pib_municipio_2010_a_2018.txt' , encoding="utf8")

#Agora coloca para ler o arquivo por linhas

dados_do_arquivo = arquivo.readlines()

# 1. Qual o valor médio de PIB per capita da cidade de Manaus no período que abrange o dataset?

#Precisamos definir as variaveis para ficar mais facil de trabalhar com os dados

CIDADE = 'Manaus'
POSICAO_DA_CIDADE = 3
POSICAO_DO_PIB_PER_CAPITA = 13

#Aqui adicionamos o contador para que toda vez que apareça a variavel, conte e some aquela variavel

contador_da_cidade = 0
somador_do_pib_per_capita = 0

#Usando a ferramenta for x in para analisar linha por linha do arquivo, para ficar mais facil a analise

for linha in dados_do_arquivo:
    linha_separada_por_ponto_e_virgula = linha.split(';')

    if len(linha_separada_por_ponto_e_virgula) == 1:
        continue
    else:
        
        if linha_separada_por_ponto_e_virgula[POSICAO_DA_CIDADE] == CIDADE:
            contador_da_cidade = contador_da_cidade + 1

            # Pegamos em string e convertemos para número
            numero_do_pib_per_capita = float(linha_separada_por_ponto_e_virgula[POSICAO_DO_PIB_PER_CAPITA])
            
            # Somar o pib per capita
            somador_do_pib_per_capita = somador_do_pib_per_capita + numero_do_pib_per_capita


#Imprimimos esse dados a partir dos resultados obtidos

print('A cidade: ', CIDADE, ' aparece ', contador_da_cidade, ' vezes na planilha')

#Abaixo tiramos a formula para calcular a media do pib per capita

media_pib_per_capita = somador_do_pib_per_capita / contador_da_cidade

print('\nA média do pib per capita de ', CIDADE ,' é:', media_pib_per_capita)
