import sys

# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

INF = int(1e9)
n = int(input().rstrip())
m = int(input().rstrip())
dist = [[INF if i != j else 0 for j in range(0, n + 1)] for i in range(0, n + 1)]
for _ in range(m):
    a, b, c = map(int, input().rstrip().split())
    dist[a][b] = c if c < dist[a][b] else dist[a][b]


def floyd_warshall():
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])


floyd_warshall()
for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(dist[i][j] if dist[i][j] != INF else 0, end=" ")
    print()
