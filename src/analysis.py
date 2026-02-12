import numpy as np
from src.api_collector import get_crypto_data
from src.transform import transform_crypto_data
import pandas as pd


def calculate_metrics(df):
    metrics = {}

    cumulative_return = (1 + df["return"]).cumprod().iloc[-1] - 1
    metrics["cumulative_return"] = float(cumulative_return)

    volatility = df["return"].std() * np.sqrt(365)
    metrics["volatility"] = float(volatility)

    mean_return = df["return"].mean() * 365
    sharpe = mean_return / volatility if volatility != 0 else 0
    metrics["sharpe_ratio"] = float(sharpe)

    return metrics


def analyze_multiple_cryptos(crypto_list):
    results = {}

    for crypto in crypto_list:
        df = get_crypto_data(crypto)
        df = transform_crypto_data(df)
        metrics = calculate_metrics(df)

        results[crypto] = metrics

    return results


def generate_ranking(metrics_dict):
    metrics_df = pd.DataFrame(metrics_dict).T
    ranking_sharpe = metrics_df.sort_values(by="sharpe_ratio", ascending=False)
    ranking_return = metrics_df.sort_values(by="cumulative_return", ascending=False)
    ranking_volatility = metrics_df.sort_values(by="volatility")
    return metrics_df, ranking_sharpe, ranking_return, ranking_volatility
