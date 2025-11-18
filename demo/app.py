import streamlit as st
import numpy as np
from mc.monte_carlo import simulate_year

st.title("Monte Carlo – Yearly Strategy Risk Model (Demo)")
st.write("This demo uses fake example values. No proprietary logic is shown.")

win_rate = st.slider("Win Rate", 0.30, 0.80, 0.52)
avg_win = st.slider("Avg Win (fraction)", 0.005, 0.03, 0.014)
avg_loss = st.slider("Avg Loss (fraction)", 0.005, 0.03, 0.010)
trades_per_year = st.slider("Trades Per Year", 100, 2000, 800)
initial_equity = st.number_input("Initial Equity", 10000, 500000, 100000)
n_sims = st.slider("Simulations", 1000, 20000, 5000)

if st.button("Run Simulation"):
    df = simulate_year(
        win_rate,
        avg_win,
        avg_loss,
        trades_per_year,
        initial_equity,
        n_sims=n_sims,
        seed=42
    )

    st.subheader("Summary (Fake)")
    st.write(df.describe())

    st.subheader("Final Equity Distribution")
    st.bar_chart(df["final_equity"])

    st.subheader("Drawdown Distribution")
    st.bar_chart(df["max_drawdown"])
