from src.api_collector import get_crypto_data

df = get_crypto_data("bitcoin")

print(df.head())
print(df.columns)
print(df.shape)
