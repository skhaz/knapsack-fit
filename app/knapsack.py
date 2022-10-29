from pandas import Series


def knapsack(W: int, wt: Series, value: Series) -> int:
    """
    https://www.geeksforgeeks.org/0-1-knapsack-problem-dp-10/
    """
    n = len(wt)
    K = [[0 for _ in range(W + 1)] for _ in range(n + 1)]

    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i - 1] <= w:
                K[i][w] = max(value[i - 1] + K[i - 1][w - wt[i - 1]], K[i - 1][w])
            else:
                K[i][w] = K[i - 1][w]

    return K[n][W]
