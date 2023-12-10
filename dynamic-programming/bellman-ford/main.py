import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
INF = int(1e9)
N, M = map(int, input().rstrip().split())
dist = [INF] * (N + 1)
edges = []
for _ in range(M):
    edges.append(tuple(map(int, input().rstrip().split())))


def bellman_ford(start):
    dist[start] = 0
    for i in range(1, N):
        for edge in edges:
            src, dest, weight = edge
            if dist[src] == INF:
                continue
            if dist[dest] > dist[src] + weight:
                dist[dest] = dist[src] + weight

    for edge in edges:
        src, dest, weight = edge
        if dist[src] == INF:
            continue
        if dist[dest] > dist[src] + weight:
            return False

    return True


if bellman_ford(1) == False:
    print(-1)
else:
    for i in range(2, N + 1):
        print(dist[i] if dist[i] != INF else -1)
