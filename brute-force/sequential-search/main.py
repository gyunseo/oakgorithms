import sys, unittest

input = sys.stdin.readline
if __name__ == "__main__":
    # input.txt 값 읽기
    data = [*map(int, input().strip("]").strip("[").split(","))]
    print(data)
