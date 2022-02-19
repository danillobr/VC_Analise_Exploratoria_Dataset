#Bibliotecas importadas
import pandas as pd
import os

#Acessando o diretório dos arquivos CSV e carregando eles nas variáveis
os.chdir(r'C:\Users\Dan\Desktop\Projeto\VC_Analise_Exploratoria_Dataset\Pré-processamento')
dados2015 = pd.read_csv('2015.csv', delimiter=None, header='infer', index_col=None, usecols=None, squeeze=None, mangle_dupe_cols=True, dtype=None, engine=None, converters=None, true_values=None, false_values=None, skipinitialspace=False, skiprows=None, skipfooter=0, nrows=None, na_values=None, keep_default_na=True, na_filter=True, verbose=False, skip_blank_lines=True, parse_dates=None, infer_datetime_format=False, keep_date_col=False, date_parser=None, dayfirst=False, cache_dates=True, iterator=False, chunksize=None, compression='infer', thousands=None, decimal='.', lineterminator=None, quotechar='"', quoting=0, doublequote=True, escapechar=None, comment=None, encoding=None, encoding_errors='strict', dialect=None, error_bad_lines=None, warn_bad_lines=None, on_bad_lines=None, delim_whitespace=False, low_memory=True, memory_map=False, float_precision=None, storage_options=None)
dados2016 = pd.read_csv('2016.csv')
dados2017 = pd.read_csv('2017.csv')
dados2018 = pd.read_csv('2018.csv')
dados2019 = pd.read_csv('2019.csv')
dados2020 = pd.read_csv('2020.csv')
dados2021 = pd.read_csv('2021.csv')

#Criar novo atributo ano para cada tabela
dados2015['ano'] = 2015
dados2016['ano'] = 2016
dados2017['ano'] = 2017
dados2018['ano'] = 2018
dados2019['ano'] = 2019
dados2020['ano'] = 2020
dados2021['ano'] = 2021

#Gera Gráfico casos confirmados por ano
totalcasos2015 = len(dados2015.index) 
totalcasos2016 = len(dados2016.index)
totalcasos2017 = len(dados2017.index)
totalcasos2018 = len(dados2018.index)
totalcasos2019 = len(dados2019.index)
totalcasos2020 = len(dados2020.index)
totalcasos2021 = len(dados2021.index)

graficoQuantidadeCasosAno = pd.DataFrame({
    'Ano': ['2015', '2016', '2017', '2018', '2019', '2020', '2021'],
    'Casos confirmados por Ano':[
        totalcasos2015,
        totalcasos2016,
        totalcasos2017,
        totalcasos2018,
        totalcasos2019,
        totalcasos2020,
        totalcasos2021
]})
graficoQuantidadeCasosAno.groupby(['Ano']).sum().plot(
    kind='pie',
    y='Casos confirmados por Ano',
    autopct='%1.1f%%',
    figsize=(9, 8),
    title=''
)

quantObito2015 = dados2015['dt_obito'].count()
quantObito2016 = dados2016['dt_obito'].count()
quantObito2017 = dados2017['dt_obito'].count()
quantObito2018 = dados2018['dt_obito'].count()
quantObito2019 = dados2019['dt_obito'].count()
quantObito2020 = dados2020['dt_obito'].count()
quantObito2021 = dados2021['dt_obito'].count()

casos = [
    totalcasos2015,
    totalcasos2016,
    totalcasos2017,
    totalcasos2018,
    totalcasos2019,
    totalcasos2020,
    totalcasos2021]
obitos = [quantObito2015, quantObito2016, quantObito2017, quantObito2018, quantObito2019, quantObito2020, quantObito2021]
ano = ['2015', '2016', '2017', '2018', '2019', '2020', '2021']
graficoQuantidadeCasosObitoAno = pd.DataFrame({
    'casos': casos,
    'obitos': obitos},
    index=ano)
graficoQuantidadeCasosObitoAno.plot(kind='barh', figsize=(10, 3), title='')
graficoQuantidadeCasosAno.plot(kind='barh', x='Ano', y='Casos confirmados por Ano', figsize=(10, 5), title='Gráfico de barras horizontal dos casos confirmados por ano')

#Criar um nome atributo mês para cada tabela de 2016
mes = dados2016['dt_notificacao'].str.split('-', n = 2, expand = True)
dados2016['mes'] = pd.to_datetime(mes[1], format='%m').dt.month_name().str.slice(stop=3)

#Gera Gráfico casos confirmados por mês do ano que mais apresentou casos
quantidadeCasosMes = dados2016.loc[:,[
    'mes',
    'ano'
]].groupby(['mes']).count()
jan = quantidadeCasosMes.loc['Jan']
fev = quantidadeCasosMes.loc['Feb']
mar = quantidadeCasosMes.loc['Mar']
abr = quantidadeCasosMes.loc['Apr']
maio = quantidadeCasosMes.loc['May']
jun = quantidadeCasosMes.loc['Jun']
jul = quantidadeCasosMes.loc['Jul']
ago = quantidadeCasosMes.loc['Aug']
sete = quantidadeCasosMes.loc['Sep']
out = quantidadeCasosMes.loc['Oct']
nov = quantidadeCasosMes.loc['Nov']
dez = quantidadeCasosMes.loc['Dec']

graficoQuantidadeCasosMes = pd.DataFrame({
    'Mês': ['Jan', 'Fev', 'Mar', 'Abr', 'Maio', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'],
    'Casos confirmados em 2016':[
        int(jan),
        int(fev),
        int(mar),
        int(abr),
        int(maio),
        int(jun),
        int(jul),
        int(ago),
        int(sete),
        int(out),
        int(nov),
        int(dez),
]})
graficoQuantidadeCasosMes.groupby(['Mês']).sum().plot(
    kind='pie',
    y='Casos confirmados em 2016',
    autopct='%1.1f%%',
    figsize=(12, 12),
    title=''
)

#Unir os dados/tabelas em um único dataset
dataset = pd.concat([dados2015, dados2016, dados2017, dados2018, dados2019, dados2020, dados2021], axis=0)

#Gera Gráfico casos confirmados por bairro
quantidadeCasosBairro = dataset.loc[:,[
    'no_bairro_residencia',
    'dt_notificacao'
]].groupby(['no_bairro_residencia'], as_index=False).count()
quantidadeCasosBairro = quantidadeCasosBairro.rename(columns={'no_bairro_residencia': 'bairro', 'dt_notificacao': 'total'})
quantidadeCasosBairro = quantidadeCasosBairro.sort_values(by=['total'])
quantidadeCasosBairro = quantidadeCasosBairro.tail(10)
               
#quantidadeCasosBairro = quantidadeCasosBairro.sort_values(by=['bairro'])
#quantidadeCasosBairro.plot.barh(x='bairro', y='total')
quantidadeCasosBairro.plot(kind='barh', x='bairro', y='total', figsize=(10, 5), title='')

#Gera Gráfico evolução dos casos
evolucao = dataset.loc[:,[
    'dt_obito',
    'dt_encerramento'
]]
evolucao['obitoEncerramento'] = evolucao['dt_obito'] + evolucao['dt_encerramento']

quantInconclusivo = len(evolucao.index)
quantObito = evolucao['dt_obito'].count()
quantEncerramento = evolucao['dt_encerramento'].count()
evolucao.dropna(subset = ['obitoEncerramento'], inplace=True) 
quantObitoEncerramento = evolucao['obitoEncerramento'].count()
quantInconclusivo = quantInconclusivo - quantObito - quantEncerramento + quantObitoEncerramento


graficoEvolucao = pd.DataFrame({
    'Estado': ['Obito', 'Cura', 'Inconclusivo'],
    'Total':[
        quantObito,
        quantEncerramento,
        quantInconclusivo]
})
graficoEvolucao.groupby(['Estado']).sum().plot(
    kind='pie',
    y='Total',
    autopct='%1.1f%%',
    figsize=(7, 7),
    title=''
)
graficoEvolucao.plot(kind='barh', x='Estado', y='Total', figsize=(12, 5), title='')

#Gera Histograma pela idade
auxIdade = dataset['dt_nascimento'].str.split('-', n = 1, expand = True)
idadePacientes = pd.DataFrame()
idadePacientes['Idades'] = dataset['ano'] - auxIdade[0].astype(int)
idadePacientes.plot.hist(bins=10, alpha=0.5, title='')
idadePacientes.hist()

#Gera Gráfico sobre como a dengue afeta os sexos diferentes
sexoFebreExantemaVomitoNause = dataset.loc[:,[
    'tp_sexo',
    'febre',
    'exantema',
    'vomito',
    'nausea'
]]
sexoFebreExantemaVomitoNause['media dos sintomas'] = (
    sexoFebreExantemaVomitoNause['febre'] +
    sexoFebreExantemaVomitoNause['exantema'] +
    sexoFebreExantemaVomitoNause['vomito'] +
    sexoFebreExantemaVomitoNause['nausea']
) / 4

sexoFebreExantemaVomitoNause.groupby('tp_sexo').hist(figsize=(9, 9))
sexoFebreExantemaVomitoNause.groupby('tp_sexo').count()
sexoFebreExantemaVomitoNause.groupby('tp_sexo').describe()
sexoFebreExantemaVomitoNause.groupby('tp_sexo').mean()