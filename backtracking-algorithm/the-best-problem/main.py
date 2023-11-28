import sys

input = sys.stdin.readline

# 그래프를 담은 리스트
graph = [[] for _ in range(100)]
ans = False

# dfs 방문 체크를 위한 변수
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
        # 이미 방문했으면 그 노드는 건너 띈다.
        if is_visited[next_node]:
            continue
        dfs(next_node, kinship + weight)


if __name__ == "__main__":
    # 내 이름과 결혼할 타겟의 이름
    me, target = map(int, input().rstrip().split())
    n = int(input().rstrip())
    # 그래프 생성
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
    # dfs로 그래프 탐색
    dfs(me, 0)
    if ans:
        print(f"{target}과 결혼 가능")
    else:
        print(f"{target}과 결혼 불가능")
