import sys

input = sys.stdin.readline

sys.setrecursionlimit(10**9)


def get_heap_sorted_list(unsorted_list, heap_type):
    """
    heap 정렬을 이용하여 리스트를 정렬한다.
    >>> get_heap_sorted_list([31, 30, 23, 2, 33, 61, 87, 58, 53, 32, 68, 29, 38, 34, 66, 42, 8, 21, 125, 341, 221, 648, 62, 1, 921], "max")
    [1, 2, 8, 21, 23, 29, 30, 31, 32, 33, 34, 38, 42, 53, 58, 61, 62, 66, 68, 87, 125, 221, 341, 648, 921]

    >>> get_heap_sorted_list([31, 30, 23, 2, 33, 61, 87, 58, 53, 32, 68, 29, 38, 34, 66, 42, 8, 21, 125, 341, 221, 648, 62, 1, 921], "min")
    [921, 648, 341, 221, 125, 87, 68, 66, 62, 61, 58, 53, 42, 38, 34, 33, 32, 31, 30, 29, 23, 21, 8, 2, 1]
    """

    sorted_list = [*unsorted_list]
    list_len = len(sorted_list)

    def heapify(root_idx, heap_size):
        next_idx = root_idx
        left_child_idx = 2 * root_idx + 1
        right_child_idx = 2 * root_idx + 2

        def is_next_idx_updatable_to_left_child_idx():
            if left_child_idx >= heap_size:
                return False
            return True

        def is_next_idx_updatable_to_right_child_idx():
            if right_child_idx >= heap_size:
                return False
            return True

        def update_next_idx_to_left_child_idx():
            nonlocal next_idx
            if is_next_idx_updatable_to_left_child_idx() == False:
                return
            if heap_type == "max":
                # 왼쪽 sub-tree의 루트가 지금 루트보다 크면, 가장 큰 값의 인덱스 업데이트.
                if sorted_list[left_child_idx] > sorted_list[next_idx]:
                    next_idx = left_child_idx
            elif heap_type == "min":
                # 왼쪽 sub-tree의 루트가 지금 루트보다 작으면, 가장 작은 값의 인덱스 업데이트.
                if sorted_list[left_child_idx] < sorted_list[next_idx]:
                    next_idx = left_child_idx

        def update_next_idx_to_right_child_idx():
            nonlocal next_idx
            if is_next_idx_updatable_to_right_child_idx() == False:
                return
            if heap_type == "max":
                # 오른쪽 sub-tree의 루트가 지금 루트보다 크면, 가장 큰 값의 인덱스 업데이트.
                if sorted_list[right_child_idx] > sorted_list[next_idx]:
                    next_idx = right_child_idx
            elif heap_type == "min":
                # 오른쪽 sub-tree의 루트가 지금 루트보다 작으면, 가장 작은 값의 인덱스 업데이트.
                if sorted_list[right_child_idx] < sorted_list[next_idx]:
                    next_idx = right_child_idx

        update_next_idx_to_left_child_idx()
        update_next_idx_to_right_child_idx()
        # 다음 인덱스가 루트의 인덱스와 같으면, 종료한다.
        # 더 이상, sub-tree에 대해 heapify를 호출할 필요가 없다.
        if next_idx == root_idx:
            return

        sorted_list[next_idx], sorted_list[root_idx] = (
            sorted_list[root_idx],
            sorted_list[next_idx],
        )
        heapify(next_idx, heap_size)

    # 힙 트리를 구성한다.
    # 힙 트리의 leap node는 자식 노드가 없으므로, heapify를 호출할 필요가 없다.
    # 그래서, 힙 트리의 non-leap node부터 heapify를 호출한다. (list_len // 2 - 1)
    # 작은 힙 트리부터 heapify를 호출하여, 점점 위로 올라간다.
    for i in range(list_len // 2 - 1, -1, -1):
        heapify(i, list_len)
    # 힙 트리의 root node와 마지막 node를 교환한다.
    # 가장 작거나 큰 값이 마지막 node에 위치하게 된다.
    # 그러면 마지막으로 교환된 node는 정렬이 완료된 것이므로, heapify를 호출할 필요가 없다.
    # 그래서, 힙 트리의 root node부터 heapify를 호출한다.
    # 대신, 정렬돼서 미리 빼 놓은 마지막 node는 heapify의 범위에서 제외한다.

    for i in range(list_len - 1, 0, -1):
        sorted_list[0], sorted_list[i] = sorted_list[i], sorted_list[0]
        heapify(0, i)
    return sorted_list


if __name__ == "__main__":
    heap_type = input().rstrip()
    unsorted_list = list(map(int, input().rstrip().split(",")))
    print(get_heap_sorted_list(unsorted_list, heap_type))
