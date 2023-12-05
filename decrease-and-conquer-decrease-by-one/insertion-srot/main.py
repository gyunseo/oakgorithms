import sys, unittest, time

input = sys.stdin.readline


def get_insertion_sorted(arr):
    arr_size = len(arr)
    for i in range(1, arr_size):
        key_val = arr[i]
        j = i - 1
        while j >= 0 and key_val < arr[j]:
            # key_val 보다 큰 원소들을 오른쪽으로 한 칸씩 이동
            arr[j + 1] = arr[j]
            j -= 1
        # key_val 보다 작은 원소를 찾았으므로 (아니면 j == -1), 그 다음 원소에 key_val 삽입
        arr[j + 1] = key_val
    return arr


if __name__ == "__main__":
    unsorted_list = list(map(int, input().strip("[").strip("]").split(",")))
    sorted_list = get_insertion_sorted(unsorted_list)
    print(f"정렬 전: {unsorted_list}")
    print(f"삽입 정렬 후: {sorted_list}")
