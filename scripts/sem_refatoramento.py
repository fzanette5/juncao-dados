import json
import csv

def leitura_json(path_json):
    dados_json = []
    with open(path_json, 'r') as file:
        dados_json = json.load(file)
    return dados_json

def leitura_csv(path_csv):
    dados_csv = []
    with open(path_csv, 'r') as file:
        spamreader = csv.DictReader(file, delimiter=',')
        for row in spamreader:
            dados_csv.append(row)
    return dados_csv

def leitura_dados(path, tipo_arquivo):
    dados = []

    if tipo_arquivo == 'csv':
        dados = leitura_csv(path)
    
    elif tipo_arquivo == 'json':
        dados = leitura_json(path)

    return dados

def get_columns(dados):
    return list(dados[0].keys())

def rename_columns(dados, key_mapping):
    new_dados_csv = []

    for old_dict in dados:
        dict_temp = {}
        for old_key, value in old_dict.items():
            dict_temp[key_mapping[old_key]] = value
        new_dados_csv.append(dict_temp)

    return new_dados_csv

def size_data(dados):
    return len(dados)

def join(dadosA, dadosB):
    combine_list = []
    combine_list.extend(dadosA)
    combine_list.extend(dadosB)
    return combine_list

def transformando_dados_tabela(dados, nomes_colunas):
    
    dados_comninados_tabela = [nomes_colunas]
    
    for row in dados:
        linha = []
        for coluna in nomes_colunas:
            linha.append(row.get(coluna, 'indisponível'))
        dados_comninados_tabela.append(linha)

    return dados_comninados_tabela

def salvando_dados(dados, path):
    with open(path, 'w') as file:
        writer = csv.writer(file)
        writer.writerows(dados)

path_json = 'data_raw/dados_empresaA.json'
path_csv = 'data_raw/dados_empresaB.csv'

#Iniciando a leitura
dados_json = leitura_dados(path_json, 'json')
nome_coluna_json = get_columns(dados_json)
tamanho_dados_json = size_data(dados_json)

print(f"Nome colunas dados json: {nome_coluna_json}")
print(f"Tamanho dos dados json: {tamanho_dados_json}")

dados_csv = leitura_dados(path_csv, 'csv')
nome_coluna_csv = get_columns(dados_csv)
tamanho_dados_csv = size_data(dados_csv)
print(f"Nome colunas dados csv: {nome_coluna_csv}")
print(f"Tamanho dos dados csv: {tamanho_dados_csv}")

#Transformação de dados

key_mapping = {'Nome do Item': 'Nome do Produto',
               'Classificação do Produto': 'Categoria do Produto',
               'Valor em Reais (R$)': 'Preço do Produto (R$)',
               'Quantidade em Estoque': 'Quantidade em Estoque',
               'Nome da Loja': 'Filial',
               'Data da Venda': 'Data da Venda',
                }

dados_csv = rename_columns(dados_csv, key_mapping)
nome_coluna_csv = get_columns(dados_csv)
print(nome_coluna_csv)

dados_fusao = join(dados_csv, dados_json)
nome_coluna_fusao = get_columns(dados_fusao)
tamanho_dados_fusao = size_data(dados_fusao)
print(nome_coluna_fusao)
print(tamanho_dados_fusao)

#Salvando os dados

dados_fusao_tabela = transformando_dados_tabela(dados_fusao, nome_coluna_fusao)

salvando_dados(dados_fusao_tabela, path_dados_combinados)

print(path_dados_combinados)