import time, random, unittest


def get_quick_sorted(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        left = [*filter(lambda x: x <= pivot, arr[1:])]
        right = [*filter(lambda x: x > pivot, arr[1:])]
        partial_sorted = get_quick_sorted(left) + [pivot] + get_quick_sorted(right)
        QuickSortTest.과정.append(partial_sorted)
        return partial_sorted


class QuickSortTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print("0~1000까지의 정수 100개를 랜덤으로 생성합니다.")
        cls.random_numbers = [random.randint(0, 1000) for _ in range(100)]
        cls.sorted_random_numbers = sorted(cls.random_numbers)
        cls.과정 = []
        print("Quick Sort 테스트 시작")

    @classmethod
    def tearDownClass(cls) -> None:
        print("\nQuick Sort 테스트 종료\n")

        print("Quick Sort 과정을 출력합니다.")
        for i, 과정_리스트 in enumerate(cls.과정):
            print(f"{i + 1}번째 과정: {과정_리스트}")

    def setUp(self) -> None:
        self.start_time = time.time()

    def tearDown(self) -> None:
        self.end_time = time.time()
        print(f"\n테스트 소요 시간: {self.end_time - self.start_time:4f}s")

    def test_quick_sort(self):
        self.assertEqual(
            get_quick_sorted(QuickSortTest.random_numbers),
            QuickSortTest.sorted_random_numbers,
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
