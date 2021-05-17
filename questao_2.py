# Ler o arquivo em txt

arquivo = open('./pib_municipio_2010_a_2018.txt' , encoding="utf8")

# Ler o arquivo por linhas

dados_do_arquivo = arquivo.readlines()

dados_do_arquivo = dados_do_arquivo[1:len(dados_do_arquivo)]

# Definir as variaveis para utilizar nas formulas

POSICAO_DO_ESTADO = 1
POSICAO_DO_PIB_PER_CAPITA = 13
POSICAO_DO_ANO = 0

# 2. Qual o ranking de estados por média de PIB per capita de 2010?
# ranking = ordenação - do maior pro menor
# Utilizar o dicionário para poder ver melhor os dados dentro da lista

dicionario_de_estados = {}

# Criou-se um dicionário de estados
# Usei um dicionário porque queria uma estrutura genérica para adicionar os estados assim q eles aparecessem na planilha

for linha in dados_do_arquivo:
    linha_separada_por_ponto_e_virgula = linha.split(';')
# Foi definido o for para toda linha quando a aparecer o ";" ele ser separado.

    if len(linha_separada_por_ponto_e_virgula) == 1:
        continue
    else:
        if  linha_separada_por_ponto_e_virgula[POSICAO_DO_ANO] =='2010':

                estado = linha_separada_por_ponto_e_virgula[POSICAO_DO_ESTADO]
# Foi definido a variavel linha_separada_por_ponto_e_virgula para ser utilizado no if e também o ano que queremos e a posição dos estados, para poder a formula entender aquilo que é pedido
        try:
            numero_do_pib_per_capita = float(linha_separada_por_ponto_e_virgula[POSICAO_DO_PIB_PER_CAPITA])
# Usou-se o try/except para tratar a equação e assim obter os resultados, mas percebi que alguns números dentro do arquivo, tinham número com "()". Por tanto a formula não leria esses números, assim aplicando erro. Sendo assim, utilizei o replace para retirar o "()" e assim poder obter o resultado
        except:
            texto_consertado = linha_separada_por_ponto_e_virgula[POSICAO_DO_PIB_PER_CAPITA].replace('(', '')
            texto_consertado = texto_consertado.replace(')', '')
            numero_do_pib_per_capita = float(texto_consertado)
            pass
        if estado in dicionario_de_estados:
            dicionario_de_estados[estado]['contador'] += 1
            dicionario_de_estados[estado]['soma_pib_per_capita'] += numero_do_pib_per_capita
            dicionario_de_estados[estado]['media_pib_per_capita'] = dicionario_de_estados[estado]['soma_pib_per_capita']/dicionario_de_estados[estado]['contador'] 
        else:
            dicionario_de_estados[estado] = {
                'contador': 1,
                'soma_pib_per_capita': numero_do_pib_per_capita,
                'media_pib_per_capita': numero_do_pib_per_capita
            }

# Aqui será feito uma lista de tuplas para poder pegar o estado e media_pib_per_capita e ficar mais fácil para analisar os dados e também porque não conseguimos ordernar um dicionário
# Essa lista de tuplas está no formato : [ ( <ESTADO> , <MEDIA_PIB_PER_CAPITA> ), ... ]
# Exemplo:  [('Ji-Paraná', 16885.883529411767), ('Porto Velho', 15701.723580246911), ('Rio Branco', 12958.440634920637), ...]
# Inserimos os dados que pegamos no dicionario_de_estados e colocamos na lista

lista_ordenada_cidade_pib_per_capita = []
for estado in dicionario_de_estados:
    lista_ordenada_cidade_pib_per_capita.append( ( estado, dicionario_de_estados[estado]['media_pib_per_capita']  ) )

# Aqui acontecerá o ordenanamento da lista:
# Vale ressaltar que a formula, sort(key=lambda a:a[1], reverse=True), é utilizada como forma de ordenamento onde pegaremos todas as chaves na posição [1], a qual se refere o pib_per_capita, dentro da nossa lista.
lista_ordenada_cidade_pib_per_capita.sort(key=lambda a:a[1], reverse=True)

# Depois de todo o processo imprime-se o TOP 10 da lista:
print('\n2. Qual o ranking de estados por média de PIB per capita de 2010?')
print('\nTOP 10:')
for estado in lista_ordenada_cidade_pib_per_capita[0:10]:
   print('Estado: ', estado[0], '\tPIB:', estado[1] )
