from collections import deque
import sys

input = sys.stdin.readline
n, k = map(int, input().rstrip().split())
people: deque[int] = deque(i for i in range(1, n + 1))
ans: list[int] = []

while people:
    for _ in range(k - 1):
        people.append(people.popleft())
    ans.append(people.popleft())

print("<", end="")
print(", ".join(map(str, ans)), end="")
print(">")
