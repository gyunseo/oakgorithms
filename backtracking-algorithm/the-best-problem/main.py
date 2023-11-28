import sys

input = sys.stdin.readline

graph = [[] for _ in range(100)]
ans = False

is_visited = [False for _ in range(100)]


def dfs(cur_node, kinship):
    if cur_node == target:
        global ans

        if kinship > 8:
            ans = True
            return
        ans = False
        return
    is_visited[cur_node] = True
    for next_node, weight in graph[cur_node]:
        if is_visited[next_node]:
            continue
        dfs(next_node, kinship + weight)


if __name__ == "__main__":
    me, target = map(int, input().rstrip().split())
    n = int(input().rstrip())
    for _ in range(n):
        a, relationship, b = input().rstrip().split()
        a = int(a)
        b = int(b)
        if relationship == "child":
            graph[a].append((b, 1))
            graph[b].append((a, 1))
        elif relationship == "marry":
            graph[a].append((b, 0))
            graph[b].append((a, 0))
    dfs(me, 0)
    if ans:
        print(f"{target}과 결혼 가능")
    else:
        print(f"{target}과 결혼 불가능")
