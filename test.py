from src.analysis import analyze_multiple_cryptos, generate_ranking

cryptos = ["bitcoin", "ethereum", "solana"]

metrics = analyze_multiple_cryptos(cryptos)

metrics_df, ranking_sharpe, ranking_return, ranking_vol = generate_ranking(metrics)

print("Tabela Consolidada:")
print(metrics_df)

print("\nRanking por Sharpe:")
print(ranking_sharpe)

print("\nRanking por Retorno:")
print(ranking_return)

print("\nRanking por Volatilidade:")
print(ranking_vol)
