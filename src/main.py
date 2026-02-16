import os
import pandas as pd

from src.api_collector import get_crypto_data
from src.transform import transform_crypto_data
from src.analysis import calculate_metrics
from src.cleaning import clean_crypto_data

def ensure_directories():
    os.makedirs("data/raw", exist_ok=True)
    os.makedirs("data/processed", exist_ok=True)
    os.makedirs("data/results", exist_ok=True)

def run_pipeline(crypto_list):
    ensure_directories()

    all_metrics = {}

    for crypto in crypto_list:
        print(f"Processando {crypto}...")

        df_raw = get_crypto_data(crypto)
        df_raw.to_csv(f"data/raw/{crypto}_raw.csv", index=False)

        
        df_cleaned = clean_crypto_data(df_raw)

       
        df_processed = transform_crypto_data(df_cleaned)
        df_processed.to_csv(f"data/processed/{crypto}_processed.csv", index=False)

      
        metrics = calculate_metrics(df_processed)
        all_metrics[crypto] = metrics

    df_results = pd.DataFrame(all_metrics).T
    df_results.to_csv("data/results/crypto_metrics.csv")

    print("\nPipeline finalizado com sucesso")

if __name__ == "__main__":
    cryptos = ["bitcoin", "ethereum", "solana"]
    run_pipeline(cryptos)
