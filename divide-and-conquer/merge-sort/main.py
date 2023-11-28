import time, random, unittest


def get_merge_sorted(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_arr = get_merge_sorted(arr[:mid])
    right_arr = get_merge_sorted(arr[mid:])

    def merge(left, right):
        merged_arr = []
        left_idx, right_idx = 0, 0

        while left_idx < len(left) and right_idx < len(right):
            if left[left_idx] < right[right_idx]:
                merged_arr.append(left[left_idx])
                left_idx += 1
            else:
                merged_arr.append(right[right_idx])
                right_idx += 1

        # 여기로 왔다는 말은
        # left, right 둘 중 하나는 끝까지 다 돌았다는 뜻
        # 둘 중 하나만 돌았을 때는 위의 while문에서 이미 merged_arr에 추가가 되었기 때문에
        # 둘 중 하나만 돌았을 때는 그냥 나머지를 다 넣어주면 된다.

        while left_idx < len(left):
            merged_arr.append(left_arr[left_idx])
            left_idx += 1

        while right_idx < len(right):
            merged_arr.append(right_arr[right_idx])
            right_idx += 1

        return merged_arr

    partial_merged_list = merge(left_arr, right_arr)
    MergeSortTest.sort_procedure.append(partial_merged_list)
    return partial_merged_list


class MergeSortTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print("0~1000까지의 정수 50개를 랜덤으로 생성합니다.")
        cls.random_numbers = [random.randint(0, 1000) for _ in range(50)]
        cls.sorted_random_numbers = sorted(cls.random_numbers)
        cls.sort_procedure = []
        print("Merge Sort 테스트 시작")

    @classmethod
    def tearDownClass(cls) -> None:
        print("\nMerge Sort 테스트 종료\n")

        print("Merge Sort 과정을 출력합니다.")
        for i, procedure in enumerate(cls.sort_procedure):
            print(f"{i + 1}번째 과정: {procedure}")

    def setUp(self) -> None:
        self.start_time = time.time()

    def tearDown(self) -> None:
        self.end_time = time.time()
        print(f"\n테스트 소요 시간: {self.end_time - self.start_time:4f}s")

    def test_quick_sort(self):
        self.assertEqual(
            get_merge_sorted(MergeSortTest.random_numbers),
            MergeSortTest.sorted_random_numbers,
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
