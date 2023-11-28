from collections import Counter
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os
nRowsRead = 1000

dataset1 = pd.read_csv('./NCD_WHO_Data/Metadata_Country.csv', delimiter=',', nrows=nRowsRead)
dataset1.dataframeName = 'Metadata_Country.csv'

print(dataset1.columns)
unique_regions = dataset1['Region'].unique()

# Criando uma lista para armazenar os valores únicos
unique_regions_list = []

# Iterando sobre os valores únicos
for region in unique_regions:
    unique_regions_list.append(region)

# Exibindo a lista de valores únicos

unique_regions_list = np.array(unique_regions_list)
unique_regions_list = list(unique_regions_list)

if 'nan' in unique_regions_list:
    print('entrou')
    index_del = unique_regions_list.index('nan')
    del unique_regions_list[index_del]

print(unique_regions_list)
print(type(unique_regions))




incomes = np.array(dataset1['IncomeGroup'])
count_incomes = Counter(incomes)
dict_incomes = dict(count_incomes)

incomes = np.array(dict_incomes.keys())
incomes = [str(income) for income in dict_incomes.keys()]
print(type(incomes))
currents_income = [int(income) for income in dict_incomes.values()]

if 'nan' in incomes:
    index_del = incomes.index('nan')
    del incomes[index_del]
    del currents_income[index_del]

plt.bar(incomes, currents_income, width=0.4, color='mediumpurple')

plt.xticks(fontsize=8)
plt.xlabel('Receita')
plt.ylabel('Mortalidade DNT')
plt.title('Histograma de Receita x Frequencia')

plt.show()



###Segundo Dataset
# Nome do arquivo de entrada e saída
nome_arquivo = 'seu_arquivo.csv'
dataset2 = os.path.join(os.getcwd(), 'NCD_WHO_Data/Global Number of deaths attributed to non-communicable diseases by type of disease and sex 2009-2019.csv')
dataset2 = pd.read_csv(dataset2)
results = []
i_dataset1 = []

acumLAC = 0
acumSA = 0
acumSSA = 0
acumECA = 0
acumMENA = 0
acumEAP = 0
acumNA = 0
acumWRD = 0



for location_value in dataset2['Location']:
    # Verificando se o valor atual de 'Location' está contido em algum lugar da coluna 'TableName' em dataset1

    data = dataset1[dataset1['TableName'].str.contains(location_value, case=False, na=False)]
    print(data['Region'])
    region_value = data['Region'].iloc[0] if not data['Region'].empty else False
    dataset2.columns = [col.strip() for col in dataset2.columns]

    ultimo_valor = dataset2['Annual number of deaths by cause'].iloc[-1]

    if region_value:
        if region_value == 'Latin America & Caribbean':
            acumLAC += ultimo_valor
        elif region_value == 'South Asia':
            acumSA += ultimo_valor
        elif region_value == 'Sub-Saharan Africa':
            acumSSA += ultimo_valor
        elif region_value == 'Europe & Central Asia':
            print('Entrou')
            acumECA += ultimo_valor
        elif region_value == 'Middle East & North Africa':
            acumMENA += ultimo_valor
        elif region_value == 'East Asia & Pacific':
            acumEAP += ultimo_valor
        elif region_value == 'North America':
            acumNA += ultimo_valor
        else:
            acumWRD += ultimo_valor
    else:
        print('Regiao não encontrada')

print(acumNA)
print(acumSA)
print(acumEAP)
print(acumECA)
print(acumSSA)
print(acumMENA)
print(acumLAC)
print(acumWRD)

numeros = [acumLAC, acumMENA, acumSSA, acumECA, acumEAP, acumSA, acumNA]

# Criar um array numpy a partir da lista de números
array_numeros = np.array(numeros)




plt.figure(figsize=(10, 6))
plt.bar(unique_regions_list, array_numeros, width=0.4,color='rebeccapurple')

# Adicionar rótulos, título e tamanho de legenda
plt.xticks(fontsize=8)
plt.xlabel('Regiões')
plt.ylabel('Frequência de Mortalidade (2009-2019)')
plt.title('Frequência de Mortalidade por Região')

# Adicionar anotações de valores nas barras
for i, v in enumerate(array_numeros):
    plt.text(i, v + 1e6, f'{v:.1f}', ha='center', va='bottom', fontsize=8)

# Exibir o gráfico
plt.show()

# Mostrar o plot
plt.show()
