n, k = map(int, input().split())
items: list[tuple] = [()]
for _ in range(n):
    items.append(tuple(map(int, input().split())))

dp = [[0 if i == 0 or j == 0 else -1 for j in range(k + 1)] for i in range(n + 1)]


def recursive(i, j):
    if dp[i][j] != -1:
        return dp[i][j]

    else:
        if items[i][0] > j:
            dp[i][j] = recursive(i - 1, j)

        else:
            dp[i][j] = max(
                items[i][1] + recursive(i - 1, j - items[i][0]), recursive(i - 1, j)
            )

        return dp[i][j]


# for i in range(1, n + 1):
#     for j in range(1, k + 1):
#         if items[i][0] > j:
#             dp[i][j] = dp[i - 1][j]
#         else:
#             dp[i][j] = max(items[i][1] + dp[i - 1][j - items[i][0]], dp[i - 1][j])

print(recursive(n, k))
