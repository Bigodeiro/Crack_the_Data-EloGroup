import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
 
def carregar_dados():
    """Carrega todos os datasets necessários"""
    return (
        pd.read_csv('data/transactional_data (1).csv', sep=';'),
        pd.read_csv('data/exams_data.csv'),
        pd.read_csv('data/DemographicData_ZCTAs.csv'),
        pd.read_csv('data/df_geocode (1).csv')
    )

def processar_transactional(transactional, exams):
    """Processa e limpa os dados transacionais"""
    # Conversão e limpeza de valores
    transactional['Testing Cost'] = transactional['Testing Cost'].replace({',': '.'}, regex=True).astype(float)
    transactional.dropna(inplace=True)
    
    # Remoção de outliers
    upper_bound = transactional['Testing Cost'].quantile(0.99)
    transactional = transactional[
        (transactional['Testing Cost'] < upper_bound) &
        (transactional['Testing Cost'] != 0)
    ]
    
    # Cálculo de lucro por exame
    transactional = transactional.merge(exams[['CodItem', 'Testing Cost']], on='CodItem', suffixes=('', '_ExamCost'))
    transactional['LucroExame'] = transactional['Testing Cost'] - transactional['Testing Cost_ExamCost']
    
    return transactional[transactional['LucroExame'] > 0]

def processar_demografico(demographic):
    """Processa os dados demográficos"""
    # Cria uma cópia para evitar problemas com views
    demographic = demographic.copy()
    
    # Extração e formatação do ZCTA usando .loc para deixar explícito
    demographic.loc[:, 'ZCTA'] = demographic['GeographicAreaName'].str.extract(r'ZCTA5 (\d+)').astype(int)
    demographic.drop(columns=['GeographicAreaName'], inplace=True)
    
    # Filtragem e normalização (adicionando .copy() para evitar o warning)
    demographic = demographic[demographic.isin([0]).sum(axis=1) <= 4].copy()
    demographic.rename(columns={'SexRatio(males per 100 females)': 'SexRatio'}, inplace=True)
    
    # Remoção de outliers do SexRatio
    lower_bound = demographic['SexRatio'].quantile(0.01)
    upper_bound = demographic['SexRatio'].quantile(0.99)
    return demographic[(demographic['SexRatio'] > lower_bound) & (demographic['SexRatio'] < upper_bound)]


def calcular_potencial_economico(df_final, transactional):
    """Calcula o índice de potencial econômico"""
    # Cálculo de proporções de gênero
    percentuais = transactional['Gender'].value_counts(normalize=True) * 100
    fator_genero = percentuais['F'] / percentuais['M']
    
    # Cálculo do índice final
    df_final['Índice de Potencial Econômico'] = (df_final['TotalPopulation'] / df_final['SexRatio']) * fator_genero
    return df_final.sort_values('Índice de Potencial Econômico', ascending=False)

def main():
    # Carregamento de dados
    transactional, exams, demographic, geocodes = carregar_dados()
    
    # Processamento dos dados
    transactional = processar_transactional(transactional, exams)
    demographic = processar_demografico(demographic)
    geocodes.dropna(inplace=True)
    
    # Criação do dataset final
    df_final = demographic[['ZCTA', 'TotalPopulation', 'SexRatio']].copy()
    df_final['TemLab'] = df_final['ZCTA'].isin(geocodes['Zipcode']).astype(int)
    df_final['SexRatio'] /= 100
    df_final = df_final[df_final['TemLab'] == 0].drop(columns=['TemLab'])
    
    # Cálculo do potencial econômico
    df_final = calcular_potencial_economico(df_final, transactional)
    
    # Resultado final
    top3_ZCTA = df_final.head(3)['ZCTA'].values
    print(f'As minhas recomendações para escolha de ZCTAs para construir novos laboratórios são: {top3_ZCTA[0]}, {top3_ZCTA[1]} e {top3_ZCTA[2]}')

if __name__ == '__main__':
    main()