#Bibliotecas importadas
import pandas as pd
import os, matplotlib

#Acessando o diretório dos arquivos CSV e carregando eles nas variáveis
os.chdir(r'C:\Users\Dan\Desktop\Projeto\VC_Analise_Exploratoria_Dataset\Pré-processamento')
dados2015 = pd.read_csv('2015.csv')
dados2016 = pd.read_csv('2016.csv')
dados2017 = pd.read_csv('2017.csv')
dados2018 = pd.read_csv('2018.csv')
dados2019 = pd.read_csv('2019.csv')
dados2020 = pd.read_csv('2020.csv')
dados2021 = pd.read_csv('2021.csv')

'''#Criar novo atributo ano para cada tabela
dados2015['ano'] = 2015
dados2016['ano'] = 2016
dados2017['ano'] = 2017
dados2018['ano'] = 2018
dados2019['ano'] = 2019
dados2020['ano'] = 2020
dados2021['ano'] = 2021

#Unir os dados/tabelas em um único dataset
dataset = pd.concat([dados2015, dados2016, dados2017, dados2018, dados2019, dados2020, dados2021], axis=0)'''

#Gera Gráfico Pizza casos confirmados por ano
graficoQuantidadeCasosAno = pd.DataFrame({
    'Ano': ['2015', '2016', '2017', '2018', '2019', '2020', '2021'],
    'Casos confirmados por Ano':[
        len(dados2015.index),
        len(dados2016.index),
        len(dados2017.index),
        len(dados2018.index),
        len(dados2019.index),
        len(dados2020.index),
        len(dados2021.index)]})

graficoQuantidadeCasosAno.groupby(['Ano']).sum().plot(
    kind='pie',
    y='Casos confirmados por Ano',
    autopct='%1.1f%%',
    figsize=(6, 6))

print(len(dados2015.index))
#Gerar Histograma
#grafico.groupby('tp_sexo').hist()





#Gera gráfico da linha Febre
dataset.plot(y="tp_sexo")

#Gera gráfico da linha Febre (histograma)
dados2015.hist("febre")
