import sys
import random
from typing import List, Final

input = sys.stdin.readline
LIST_SIZE: Final[int] = 1_000
random_numbers: List[int] = sorted(random.randint(0, 100) for _ in range(LIST_SIZE))


def binary_search(target: int) -> int:
    s: int = 0
    e: int = len(random_numbers) - 1
    while s <= e:
        mid: int = (s + e) // 2
        if random_numbers[mid] == target:
            return mid
        if random_numbers[mid] < target:
            s = mid + 1
            continue
        if random_numbers[mid] > target:
            e = mid - 1
            continue
    return -1


if __name__ == "__main__":
    iteration_trigger: bool = True
    while iteration_trigger:
        user_input = input().rstrip()
        if user_input == "q" or user_input == "Q":
            iteration_trigger = False
            continue
        target_num: int = int(user_input)
        print(f"{target_num}의 index: {binary_search(target_num)} (-1이면 해당 숫자가 없음)")
