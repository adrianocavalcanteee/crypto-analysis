from src.main import run_pipeline

def test_full_pipeline():
    cryptos = ["bitcoin"]

    run_pipeline(cryptos)

    print("Pipeline rodou sem erros!")
