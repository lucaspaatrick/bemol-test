# Ler o arquivo em txt
arquivo = open('./pib_municipio_2010_a_2018.txt', encoding="utf8")

# Ler o arquivo por linhas

arquivo = arquivo.readlines()

arquivo = arquivo[1:len(arquivo)]

# 3. Qual a proporção do valor adicionado bruto médio do setor de serviços em relação ao valor adicionado bruto total médio no estado do Amazonas no ano de 2018?
ESTADO = "AM"
POSICAO_DO_ESTADO = 1
POSICAO_DOS_SERVICOS = 8
POSICAO_DO_BRUTO = 10

somador_servicos = 0
somador_bruto = 0

for linha in arquivo:
    linha_separada_por_ponto_e_virgula = linha.split(';')

    # Existe uma linha em branco entre cada linha
    if len(linha_separada_por_ponto_e_virgula) == 1:
        continue
    else:
        # if linha_separada_por_ponto_e_virgula[POSICAO_DO_ESTADO] == ESTADO and linha_separada_por_ponto_e_virgula[0] == '2010':
        if linha_separada_por_ponto_e_virgula[POSICAO_DO_ESTADO] == ESTADO and linha_separada_por_ponto_e_virgula [0] == "2018":
            
            somador_servicos = somador_servicos + 1

            # Pegamos em string e convertemos para número
            servicos = float(linha_separada_por_ponto_e_virgula[POSICAO_DOS_SERVICOS])
            bruto = float(linha_separada_por_ponto_e_virgula[POSICAO_DO_BRUTO])
            
            # Somar/Acumular o pib per capita
            somador_servicos = somador_servicos + servicos
            somador_bruto = somador_bruto + bruto

proporcao= somador_servicos/somador_bruto
print('A média é de' , proporcao)

