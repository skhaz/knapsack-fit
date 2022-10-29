from pandas import Series

from app.knapsack import knapsack


def test_knapsack() -> None:
    latencies = Series([10, 70, 20])
    amounts = Series([200, 1000, 300])
    limit = 80

    assert len(latencies) == len(amounts)  # nosec B101
    assert knapsack(limit, latencies, amounts) == 1200  # nosec B101
