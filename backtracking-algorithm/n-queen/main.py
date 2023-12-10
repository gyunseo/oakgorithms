import sys

n = int(sys.stdin.readline())
col = [0] * n  # 각 row마다 퀸이 놓인 col의 index를 저장하는 리스트
count = 0


# 현재 row에 퀸을 놓을 수 있는지 체크하는 함수
def is_available(row):
    for i in range(row):
        # 같은 col에 놓인 퀸이 있는 경우
        if col[i] == col[row]:
            return False
        # 대각선에 놓인 퀸이 있는 경우
        if abs(col[i] - col[row]) == row - i:
            return False
    return True


# DFS 알고리즘으로 모든 경우의 수 탐색
def dfs(row):
    global count
    if row == n:
        count += 1
    else:
        for i in range(n):
            col[row] = i
            if is_available(row):
                dfs(row + 1)


dfs(0)
print(count)
