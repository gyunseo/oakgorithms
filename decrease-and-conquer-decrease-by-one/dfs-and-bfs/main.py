import sys
from typing import List, Final, Optional
from collections import deque

# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
MAX_VERTEX_SIZE: Final[int] = 1_000
MAX_EDGE_SIZE: Final[int] = 10_000
N: Optional[int] = None
M: Optional[int] = None
V: Optional[int] = None
adjacent_lists: List[List[int]] = [[] for _ in range(MAX_VERTEX_SIZE + 1)]
is_visited: List[bool] = [False for _ in range(MAX_VERTEX_SIZE + 1)]


def init_is_visited() -> None:
    for i in range(1, MAX_VERTEX_SIZE + 1):
        is_visited[i] = False


def read_console_input() -> None:
    global N, M, V
    N, M, V = map(int, input().rstrip().split())
    for _ in range(M):
        u, v = map(int, input().rstrip().split())
        adjacent_lists[u].append(v)
        adjacent_lists[v].append(u)


def solve() -> None:
    def dfs(start: int) -> None:
        stack: List[int] = []
        stack.append(start)
        while stack:
            cv: int = stack.pop()
            if is_visited[cv]:
                continue
            is_visited[cv] = True
            print(cv, end=" ")
            if cv == V:
                print(f"found {V} return!")
                return
            for nv in adjacent_lists[cv]:
                if not is_visited[nv]:
                    stack.append(nv)

    def bfs(start: int) -> None:
        queue: deque[int] = deque()
        queue.append(start)
        while queue:
            cv: int = queue.popleft()
            if is_visited[cv]:
                continue
            is_visited[cv] = True
            print(cv, end=" ")
            if cv == V:
                print(f"found {V} return!")
                return
            for nv in adjacent_lists[cv]:
                if not is_visited[nv]:
                    queue.append(nv)

    print(f"DFS와 BFS로 {V}를 찾아봅시다!")
    init_is_visited()
    dfs(1)
    print()
    init_is_visited()
    bfs(1)
    print()


if __name__ == "__main__":
    read_console_input()
    solve()
