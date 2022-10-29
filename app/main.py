import json

import pandas as pd

from app.knapsack import knapsack

with open("data/latencies.json") as f:
    latencies = json.load(f)

df = pd.read_csv("data/transactions.csv")
df["latency"] = df["bank_country_code"].map(latencies)

limits = [50, 60, 90, 1000]

for limit in limits:
    print(f"{limit}ms ${knapsack(limit, df['latency'], df['amount'])}")
