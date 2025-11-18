import numpy as np
import pandas as pd

def simulate_year(
    win_rate,
    avg_win,
    avg_loss,
    trades_per_year,
    initial_equity,
    n_sims=5000,
    seed=None
):
    """
    Generic, portfolio-safe Monte Carlo engine.
    Does NOT include any proprietary alpha logic.
    """
    rng = np.random.default_rng(seed)
    results = []

    for _ in range(n_sims):
        equity = initial_equity
        peak = initial_equity
        max_dd = 0

        for _ in range(trades_per_year):
            if rng.random() < win_rate:
                ret = rng.normal(avg_win, abs(avg_win) * 0.4)
            else:
                ret = -abs(rng.normal(avg_loss, abs(avg_loss) * 0.4))

            equity *= (1 + ret)
            peak = max(peak, equity)
            max_dd = max(max_dd, (peak - equity) / peak)

            if equity <= 0:
                break

        results.append([equity, max_dd])

    df = pd.DataFrame(results, columns=["final_equity", "max_drawdown"])
    return df
