# 📊 Crypto Analysis

Projeto de análise quantitativa de criptomoedas com pipeline estruturada em Python.  
Inclui coleta de dados via API pública, tratamento, cálculo de métricas e dashboard interativo com Streamlit.

---

## 🧠 Sobre o Projeto

Este projeto coleta dados históricos de preços de criptomoedas (Bitcoin, Ethereum, Solana) usando a API pública do CoinGecko, processa os dados, calcula métricas financeiras e produz visualizações interativas.

As etapas principais da pipeline são:

1. **Coleta de dados via API**
2. **Tratamento e limpeza**
3. **Transformação e cálculo de retorno**
4. **Cálculo de métricas**
5. **Persistência dos resultados**
6. **Dashboard interativo com visualizações**

---

## 🛠️ Tecnologias Utilizadas

- Python 3
- pandas → Manipulação e análise de dados
- requests → Consumo de API REST
- matplotlib → Visualização de dados
- Streamlit → Dashboard interativo
- Jupyter Notebook → Análise exploratória (EDA)
- Git → Versionamento

---

## ▶️ Como Rodar o Projeto
### 1️⃣ Clonar o repositório

```bash
git clone https://github.com/adrianocavalcanteee/crypto-analysis.git
cd crypto-analysis
```
### 2️⃣ Instalar dependências

```bash
pip install -r requirements.txt
```

---

### 3️⃣ Executar a Pipeline

```bash
python -m src.main
```

---

### 4️⃣ Executar o Dashboard

```bash
streamlit run dashboards/dashboard.py
```
