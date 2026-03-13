import pandas as pd
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TRADES_FILE = ROOT / "data" / "trades.csv"

trade = {
    "date": datetime.now(),
    "asset": "XAUUSD",
    "direction": "buy",
    "entry": 5280,
    "stop": 5268,
    "exit": 5305,
    "risk_R": 1,
    "result_R": 2.1,
    "session": "NY",
    "setup": "breakout"
}

df = pd.DataFrame([trade])
df.to_csv(TRADES_FILE, mode="a", header=False, index=False)

print("Trade registrado correctamente")
