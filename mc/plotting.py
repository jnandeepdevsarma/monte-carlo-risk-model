import matplotlib.pyplot as plt
import numpy as np

def plot_equity_curves(paths):
    plt.figure(figsize=(10,5))
    for p in paths:
        plt.plot(p, alpha=0.3)
    plt.title("Sample Equity Curves (Fake Data)")
    plt.xlabel("Trades")
    plt.ylabel("Equity")
    return plt

def plot_distribution(values):
    plt.figure(figsize=(7,4))
    plt.hist(values, bins=50)
    plt.title("Final Equity Distribution (Fake)")
    plt.xlabel("Equity")
    plt.ylabel("Frequency")
    return plt

def plot_drawdowns(drawdowns):
    plt.figure(figsize=(7,4))
    plt.hist(drawdowns, bins=40)
    plt.title("Max Drawdown Distribution (Fake)")
    plt.xlabel("Drawdown")
    plt.ylabel("Frequency")
    return plt
