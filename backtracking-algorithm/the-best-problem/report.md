# Backtracking Algorithm the Best Problem Report

### 2019311801 이균서

## Execution Environment

### OS

```zsh
Distributor ID: Ubuntu
Description:    Ubuntu 22.04.3 LTS
Release:        22.04
Codename:       jammy
```

### `Python` Runtime

Python 3.11.6

### External Libraries

There is no external libraries used in the following source code.

`Pipfile`:

```
[[source]]
[[source]]
url = "https://pypi.org/simple"
verify_ssl = true
name = "pypi"

[packages]

[dev-packages]
cloudinary = "*"

[requires]
python_version = "3.11"
python_full_version = "3.11.6"
```

## 문제 input, output 설정

내가 결혼하고자 하는 사람의 이름은 번호를 입력받습니다. 그리고 그 사람과 결혼 가능한지 여부를 출력합니다.
input으로는 가계도를 입력받습니다. 가계도는 다음과 같은 형식으로 입력받습니다.

```
1 marry 18
1 child 2
```

1과 18은 결혼  
1과 2는 부모 자식 관계

## Source Code

```python
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
```

## Execution Result

### How to run `main.py`:

```zsh
pipenv run python3 main.py < input_0.txt
pipenv run python3 main.py < input_1.txt
```

or

```zsh
python3 main.py < input_0.txt
python3 main.py < input_1.txt
```

- 실행이 안되면 <https://github.com/gyunseo/oakgorithms.git>을 `git clone` 하여, root directory에서 `pipenv install`을 하시고 `backtracking-algorithm/the-best-problem/`로 이동하셔서 `pipenv run python3 main.py < input_0.txt`를 하시면 됩니다.

### Input

`input_0.txt`:

```
1 18
19
4 child 1
4 child 2
4 child 3
4 marry 5
6 child 5
6 marry 7
6 child 8
8 marry 9
8 child 10
10 marry 11
10 child 12
12 marry 13
12 child 14
14 marry 15
14 child 16
16 marry 17
16 child 18
18 marry 19
18 child 20
```

`input_1.txt`:

```
1 20
19
4 child 1
4 child 2
4 child 3
4 marry 5
6 child 5
6 marry 7
6 child 8
8 marry 9
8 child 10
10 marry 11
10 child 12
12 marry 13
12 child 14
14 marry 15
14 child 16
16 marry 17
16 child 18
18 marry 19
18 child 20
```

### Output

```
18과 결혼 불가능
```

```
20과 결혼 가능
```

## Execution Image

![Alt text](image.png)
