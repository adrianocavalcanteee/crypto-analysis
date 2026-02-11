from src.api_collector import get_crypto_data
from src.transform import transform_crypto_data

df = get_crypto_data("bitcoin", 365)
df = transform_crypto_data(df)

print(df.head())
