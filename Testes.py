#Bibliotecas importadas
import pandas as pd
import os

#Acessando o diretório dos arquivos CSV e carregando eles nas variáveis
os.chdir(r'C:\Users\Dan\Desktop\Projeto\VC_Analise_Exploratoria_Dataset\Dataset')
dados2013 = pd.read_csv('2013.csv')
dados2014 = pd.read_csv('2014.csv')
dados2015 = pd.read_csv('2015.csv')
dados2016 = pd.read_csv('2016.csv')
dados2017 = pd.read_csv('2017.csv')
dados2018 = pd.read_csv('2018.csv')
dados2019 = pd.read_csv('2019.csv')
dados2020 = pd.read_csv('2020.csv')
dados2021 = pd.read_csv('2021.csv')

#Lista dos dados por ano
dataset = [
    dados2013,
    dados2014,
    dados2015,
    dados2016,
    dados2017,
    dados2018,
    dados2019,
    dados2020,
    dados2021
]

#Concatenação
pd.concat(dataset, axis=0)

print("foi")


#Analissar caracteristicas do dataset (sumário estatístico dos dados)
#contagem, média, desvio padrão, minimo, os quartz, valor máximo da coluna
dataset[0].describe()

#Exibir todas as colunas de um ano específico
dataset[0].columns

#Analisar caracteristicas da coluna de um ano específico 
#contagem, média, desvio padrão, minimo, os quartz, valor máximo da coluna
dataset[0]['_id'].describe()

#Consulta da linha 10 de um ano
dataset[0].loc[10]

#Consulta do intervalo 100-400 linha de um ano
dataset[0].loc[100:400]

#Consulta do intervalo 400 até a última linha de um ano
dataset[0].loc[400:]

#Consulta atributos específicos (filtrar colunas)
sintomas_Febre_vomito_2021 = dataset[8].loc[:, ['febre', 'vomito']]

#Medidas estatísticas de um atributo
dataset[8]['febre'].mean()
sintomas_Febre_vomito_2021.febre.mean()

dataset[8]['febre'].max()
dataset[8]['febre'].sum()
sintomas_Febre_vomito_2021.febre.max()

#Criar novos atributos/coluna
dataset[8]['nova coluna'] = 100

#Pegar colunas de um conjuto e por em outro
sintomas_Febre_vomito_2021['bairro'] = dataset[8]['no_bairro_residencia']

#Operações entre as colunas
sintomas_Febre_vomito_2021['febre_cinco_vezes_mais_vomito'] = dataset[8].febre*5 + dataset[8].vomito

#Exportar arquivo CSV a partir do dataset pré-processado
diretorio = r'..\Pré-processamento\20218.csv'
sintomas_Febre_vomito_2021.to_csv(diretorio)

#Remove uma coluna pelo nome
sintomas_Febre_vomito_2021 = sintomas_Febre_vomito_2021.drop(columns=['bairro'])

#Romeve uma linha pelo índice
sintomas_Febre_vomito_2021 = sintomas_Febre_vomito_2021.drop(5)
