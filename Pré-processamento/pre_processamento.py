#Bibliotecas importadas
import pandas as pd
import os

#Acessando o diretório dos arquivos CSV e carregando eles nas variáveis
os.chdir(r'C:\Users\Dan\Desktop\Projeto\VC_Analise_Exploratoria_Dataset\dataset')
dados2013 = pd.read_csv('2013.csv')
dados2014 = pd.read_csv('2014.csv')
dados2015 = pd.read_csv('2015.csv')
dados2016 = pd.read_csv('2016.csv')
dados2017 = pd.read_csv('2017.csv')
dados2018 = pd.read_csv('2018.csv')
dados2019 = pd.read_csv('2019.csv')
dados2020 = pd.read_csv('2020.csv')
dados2021 = pd.read_csv('2021.csv')

'''Lista dos dados por ano
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

#Removendo os dados referente a 2013 e 2014
dataset = dataset[2:]'''


#Pegando as colunas que tem dados válidos para a nossa análise
#2015
pp_dados2015 = dados2015.loc[:,[
    'dt_notificacao',
    'no_bairro_residencia',
    'dt_obito',
    'dt_encerramento',
    'dt_nascimento',
    'tp_sexo',
    'febre',
    'mialgia',
    'cefaleia',
    'exantema',
    'vomito',
    'nausea',
    'dor_costas',
    'conjutivite',
    'artrite',
    'artralgia',
    'petequia_n',
    'leucopenia',
    'laco',
    'dor_retro',
    'diabetes',
    'hematolog',
    'hepatopat',
    'renal',
    'hipertensao'
]]

#2016
pp_dados2016 = dados2016.loc[:,[
    'dt_notificacao',
    'no_bairro_residencia',
    'dt_obito',
    'dt_encerramento',
    'dt_nascimento',
    'tp_sexo',
    'febre',
    'mialgia',
    'cefaleia',
    'exantema',
    'vomito',
    'nausea',
    'dor_costas',
    'conjutivite',
    'artrite',
    'artralgia',
    'petequia_n',
    'leucopenia',
    'laco',
    'dor_retro',
    'diabetes',
    'hematolog',
    'hepatopat',
    'renal',
    'hipertensao'
]]

#2017
pp_dados2017 = dados2017.loc[:,[
    'dt_notificacao',
    'no_bairro_residencia',
    'dt_obito',
    'dt_encerramento',
    'dt_nascimento',
    'tp_sexo',
    'febre',
    'mialgia',
    'cefaleia',
    'exantema',
    'vomito',
    'nausea',
    'dor_costas',
    'conjutivite',
    'artrite',
    'artralgia',
    'petequia_n',
    'leucopenia',
    'laco',
    'dor_retro',
    'diabetes',
    'hematolog',
    'hepatopat',
    'renal',
    'hipertensao'
]]

#2018
pp_dados2018 = dados2018.loc[:,[
    'dt_notificacao',
    'no_bairro_residencia',
    'dt_obito',
    'dt_encerramento',
    'dt_nascimento',
    'tp_sexo',
    'febre',
    'mialgia',
    'cefaleia',
    'exantema',
    'vomito',
    'nausea',
    'dor_costas',
    'conjutivite',
    'artrite',
    'artralgia',
    'petequia_n',
    'leucopenia',
    'laco',
    'dor_retro',
    'diabetes',
    'hematolog',
    'hepatopat',
    'renal',
    'hipertensao'
]]

#2019
pp_dados2019 = dados2019.loc[:,[
    'dt_notificacao',
    'no_bairro_residencia',
    'dt_obito',
    'dt_encerramento',
    'dt_nascimento',
    'tp_sexo',
    'febre',
    'mialgia',
    'cefaleia',
    'exantema',
    'vomito',
    'nausea',
    'dor_costas',
    'conjutivite',
    'artrite',
    'artralgia',
    'petequia_n',
    'leucopenia',
    'laco',
    'dor_retro',
    'diabetes',
    'hematolog',
    'hepatopat',
    'renal',
    'hipertensao'
]]

#2020
pp_dados2020 = dados2020.loc[:,[
    'dt_notificacao',
    'no_bairro_residencia',
    'dt_obito',
    'dt_encerramento',
    'dt_nascimento',
    'tp_sexo',
    'febre',
    'mialgia',
    'cefaleia',
    'exantema',
    'vomito',
    'nausea',
    'dor_costas',
    'conjutivite',
    'artrite',
    'artralgia',
    'petequia_n',
    'leucopenia',
    'laco',
    'dor_retro',
    'diabetes',
    'hematolog',
    'hepatopat',
    'renal',
    'hipertensao'
]]

#2021
pp_dados2021 = dados2021.loc[:,[
    'dt_notificacao',
    'no_bairro_residencia',
    'dt_obito',
    'dt_encerramento',
    'dt_nascimento',
    'tp_sexo',
    'febre',
    'mialgia',
    'cefaleia',
    'exantema',
    'vomito',
    'nausea',
    'dor_costas',
    'conjutivite',
    'artrite',
    'artralgia',
    'petequia_n',
    'leucopenia',
    'laco',
    'dor_retro',
    'diabetes',
    'hematolog',
    'hepatopat',
    'renal',
    'hipertensao'
]]

#Removendo as linhas com valores nulos nos atributos referentes aos sintomas
#Removendo as linhas com valor nulo na data de nascimento
pp_dados2015.dropna(subset = ['febre', 'dt_nascimento', 'tp_sexo'], inplace=True) 
pp_dados2016.dropna(subset = ['febre', 'dt_nascimento', 'tp_sexo'], inplace=True)
pp_dados2017.dropna(subset = ['febre', 'dt_nascimento', 'tp_sexo'], inplace=True) 
pp_dados2018.dropna(subset = ['febre', 'dt_nascimento', 'tp_sexo'], inplace=True)
pp_dados2019.dropna(subset = ['febre', 'dt_nascimento', 'tp_sexo'], inplace=True) 
pp_dados2020.dropna(subset = ['febre', 'dt_nascimento', 'tp_sexo'], inplace=True)
pp_dados2021.dropna(subset = ['febre', 'dt_nascimento', 'tp_sexo'], inplace=True)

#Gera um novo dataset a partir dos dados obtidos no pré-processamento
#Exportar arquivo CSV a partir do novo dataset obtido
pp_dados2015.to_csv(r'..\Pré-processamento\2015.csv')
pp_dados2016.to_csv(r'..\Pré-processamento\2016.csv')
pp_dados2017.to_csv(r'..\Pré-processamento\2017.csv')
pp_dados2018.to_csv(r'..\Pré-processamento\2018.csv')
pp_dados2019.to_csv(r'..\Pré-processamento\2019.csv')
pp_dados2020.to_csv(r'..\Pré-processamento\2020.csv')
pp_dados2021.to_csv(r'..\Pré-processamento\2021.csv')