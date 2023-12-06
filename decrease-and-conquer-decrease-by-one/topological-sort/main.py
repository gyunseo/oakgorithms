import sys
from typing import List, Final, Optional
from collections import deque

input = sys.stdin.readline
MAX_VERTEX_SIZE: Final[int] = 32_000
MAX_EDGE_SIZE: Final[int] = 100_000
N: Optional[int] = None
M: Optional[int] = None
in_degree: List[int] = [0 for i in range(MAX_VERTEX_SIZE + 1)]
adjacent_lists: List[List[int]] = [[] for _ in range(MAX_VERTEX_SIZE + 1)]


def small_alphabet_to_int(ch: str) -> int:
    return ord(ch) - ord("a") + 1


def int_to_small_alphabet(i: int) -> str:
    return chr(i + ord("a") - 1)


def read_console_input() -> None:
    global N, M
    N, M = map(int, sys.stdin.readline().split())
    for _ in range(M):
        u, v = input().rstrip().split()
        u_ord: int = small_alphabet_to_int(u)
        v_ord: int = small_alphabet_to_int(v)
        in_degree[v_ord] += 1
        adjacent_lists[u_ord].append(v_ord)


def solve() -> None:
    queue: deque = deque()
    if N is None:
        raise ValueError("N is None")
    for i in range(1, N + 1):
        # 위상 정렬 시작 지점을 검색하여, 큐에 넣는다
        if in_degree[i] == 0:
            queue.append(i)
    while queue:
        cv: int = queue.popleft()
        print(int_to_small_alphabet(cv), end=" ")

        for nv in adjacent_lists[cv]:
            # cv와 연결된 정점들의 진입 차수를 1 감소시킨다
            # 진입 차수가 0이 되면 큐에 넣는다
            in_degree[nv] -= 1
            if in_degree[nv] == 0:
                queue.append(nv)


if __name__ == "__main__":
    read_console_input()
    solve()
    print()
