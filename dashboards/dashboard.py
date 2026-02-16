import streamlit as st
import pandas as pd
import os
import matplotlib.pyplot as plt


st.set_page_config(page_title="Crypto Dashboard", layout="centered")

st.title("Dashboard de Análise de Criptomoedas")
st.caption("Análise quantitativa baseada em retorno, risco e eficiência risco-retorno")



BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
file_path = os.path.join(BASE_DIR, "data", "results", "crypto_metrics.csv")


df = pd.read_csv(file_path, index_col=0)
df = df.reset_index()
df = df.rename(columns={"index": "Criptomoeda"})


df["cumulative_return"] = df["cumulative_return"] * 100
df["volatility"] = df["volatility"] * 100


df = df.rename(columns={
    "cumulative_return": "Retorno Acumulado (%)",
    "volatility": "Volatilidade (%)",
    "sharpe_ratio": "Índice de Sharpe"
})



st.subheader("Tabela de Métricas")
st.dataframe(df)



st.subheader("Ranking de Retorno Acumulado")

df_return = df.sort_values("Retorno Acumulado (%)", ascending=False)

fig1, ax1 = plt.subplots()
ax1.bar(df_return["Criptomoeda"], df_return["Retorno Acumulado (%)"])
ax1.set_ylabel("Retorno (%)")
plt.xticks(rotation=0)

st.pyplot(fig1)


st.subheader("Ranking de Volatilidade")

df_risk = df.sort_values("Volatilidade (%)", ascending=False)

fig2, ax2 = plt.subplots()
ax2.bar(df_risk["Criptomoeda"], df_risk["Volatilidade (%)"])
ax2.set_ylabel("Volatilidade (%)")
plt.xticks(rotation=0)

st.pyplot(fig2)



st.subheader("Risco vs Retorno")

fig3, ax3 = plt.subplots()

ax3.scatter(df["Volatilidade (%)"], df["Retorno Acumulado (%)"])

for i in range(len(df)):
    ax3.annotate(
        df["Criptomoeda"][i],
        (df["Volatilidade (%)"][i],
         df["Retorno Acumulado (%)"][i])
    )

ax3.set_xlabel("Volatilidade (%)")
ax3.set_ylabel("Retorno (%)")

st.pyplot(fig3)
