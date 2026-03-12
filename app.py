import streamlit as st
import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize

st.title("Portfolio Optimization App")

stocks = st.text_input("Enter stock symbols (comma separated)", "AAPL,MSFT,GOOGL")
start = st.date_input("Start Date")
end = st.date_input("End Date")

if st.button("Optimize Portfolio"):

    symbols = [s.strip() for s in stocks.split(",")]

    data = yf.download(symbols, start=start, end=end)["Adj Close"]

    returns = data.pct_change().dropna()

    mean_returns = returns.mean()
    cov_matrix = returns.cov()

    num_assets = len(symbols)

    def portfolio_volatility(weights):
        return np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights)))

    constraints = {"type": "eq", "fun": lambda x: np.sum(x) - 1}
    bounds = tuple((0,1) for _ in range(num_assets))

    init_guess = num_assets * [1./num_assets]

    result = minimize(portfolio_volatility,
                      init_guess,
                      method="SLSQP",
                      bounds=bounds,
                      constraints=constraints)

    weights = result.x

    st.subheader("Optimal Portfolio Weights")

    for i in range(num_assets):
        st.write(symbols[i], ":", round(weights[i],3))

    portfolio_returns = (returns * weights).sum(axis=1)

    st.subheader("Portfolio Performance")

    fig, ax = plt.subplots()
    portfolio_returns.cumsum().plot(ax=ax)
    st.pyplot(fig)
