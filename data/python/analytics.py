import pandas as pd

df = pd.read_csv("../data/trades.csv")

total_trades = len(df)

wins = df[df["result_R"] > 0]
losses = df[df["result_R"] < 0]

win_rate = len(wins) / total_trades if total_trades > 0 else 0

avg_win = wins["result_R"].mean() if len(wins) > 0 else 0
avg_loss = abs(losses["result_R"].mean()) if len(losses) > 0 else 0

profit_factor = wins["result_R"].sum() / abs(losses["result_R"].sum()) if len(losses) > 0 else 0

print("Total trades:", total_trades)
print("Win rate:", round(win_rate * 100, 2), "%")
print("Avg win:", round(avg_win,2))
print("Avg loss:", round(avg_loss,2))
print("Profit factor:", round(profit_factor,2))
