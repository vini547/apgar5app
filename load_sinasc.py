import pandas as pd
import numpy as np

# -----------------
# PARÂMETROS GLOBAIS
# -----------------
cols_to_drop = [
    'ORIGEM','DTRECEBIM','DIFDATA','CODMUNNATU','CODUFNATU','TPDOCRESP','TPFUNCRESP','DTDECLARAC',
    'HORANASC','PARIDADE','NUMEROLOTE','VERSAOSIST','DTCADASTRO','CODMUNRES','DTRECORIGA','CODPAISRES',
    'STDNNOVA','DTNASC','DTDECLARAC','DTULTMENST','DTNASCMAE','DTRECORIGA','DTRECEBIM','contador','CODESTAB', 
    'CODMUNNASC','CODANOMAL','OPORT_DN','TPMETESTIM','ESMAE2010','SERIESCMAE','ESCMAE2010','ESCMAEAGR1',
    'CONTADOR','CODOCUPMAE','IDADEPAI','LOCNASC','QTDPARTCES','IDANOMAL','STDNEPIDEM','IDADEMAE','ESCMAE',
    'QTDFILMORT','GRAVIDEZ'
]

cont_cols = [
    'QTDFILVIVO','PESO','QTDGESTANT',
    'QTDPARTNOR','QTDPARTCES','IDADEPAI',
    'SEMAGESTAC','CONSPRENAT','APGAR5','APGAR1'
]

ordinal_cols = ['GESTACAO','CONSULTAS']

target_col = 'APGAR5'

data_sinasc = [
    'SINASC_2015.csv','SINASC_2017.csv','SINASC_2018.csv','SINASC_2019.csv',
    'SINASC_2020.csv','SINASC_2021.csv','SINASC_2022.csv','SINASC_2023.csv','SINASC_2024.csv'
]

sep = ';'
state = 123

# -----------------
# FUNÇÃO DE CARREGAMENTO
# -----------------
def load_sampled_csv(csv_file, frac, state=state, sep=sep,
                     cols_to_drop=cols_to_drop, cont_cols=cont_cols,
                     ordinal_cols=ordinal_cols, target_col=target_col):

    df_sample = (
        pd.read_csv(csv_file, sep=sep,low_memory=False)
          .sample(frac=frac, random_state=state)
          .replace({9: np.nan, 99: np.nan})
          .copy()
    )

    cont_cols_existing = [c for c in cont_cols if c in df_sample.columns and c not in cols_to_drop]
    ordinal_cols_existing = [c for c in ordinal_cols if c in df_sample.columns and c not in cols_to_drop]
    cat_cols_existing = [c for c in df_sample.columns if c not in cont_cols_existing + ordinal_cols_existing  + cols_to_drop]  

    
    df_sample.drop(columns=[c for c in cols_to_drop if c in df_sample.columns], inplace=True)
    numeric_cols = cont_cols_existing + ordinal_cols_existing

    for col in numeric_cols:
        df_sample[col] = pd.to_numeric(df_sample[col], errors='coerce').astype('Int64')

    for col in cat_cols_existing:
        df_sample[col] = df_sample[col].astype('category')

    return df_sample
