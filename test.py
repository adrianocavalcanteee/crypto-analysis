import pandas as pd
from src.cleaning import clean_crypto_data

# Dados simulados
data = {
    "timestamp": [1, 2, 2, None],
    "price": [100, 200, 200, 300]
}

df = pd.DataFrame(data)

df_clean = clean_crypto_data(df)

print(df_clean)
