import pandas as pd

def clean_crypto_data(df):
    print("Colunas recebidas:", df.columns)

    df = df.copy()


    df = df.dropna()


    df = df.drop_duplicates()

    return df
