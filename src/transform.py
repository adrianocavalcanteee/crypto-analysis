import pandas as pd


def transform_crypto_data(df):
    # Converter timestamp para datetime
    df["date"] = pd.to_datetime(df["timestamp"], unit="ms")

    # Ordenar por data
    df = df.sort_values("date")

    # Calcular retorno diário
    df["return"] = df["price"].pct_change()

    return df
