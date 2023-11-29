import random, time, unittest


def get_selection_sorted(arr):
    sorted_arr = [*arr]
    for i in range(len(sorted_arr)):
        min_index = i
        for j in range(i + 1, len(sorted_arr)):
            if sorted_arr[min_index] > sorted_arr[j]:
                min_index = j
        sorted_arr[i], sorted_arr[min_index] = sorted_arr[min_index], sorted_arr[i]
    return sorted_arr


class SortingAlgorithmTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print("0~1000까지의 정수 1000개를 랜덤으로 생성합니다.")
        cls.random_numbers = [random.randint(0, 1000) for _ in range(50)]
        cls.sorted_random_numbers = sorted(cls.random_numbers)
        print("Selection Sort Algorithms 테스트 시작")

    @classmethod
    def tearDownClass(cls) -> None:
        print("\nSelection Sort Algorithms 테스트 종료\n")

    def setUp(self) -> None:
        self.start_time = time.time()

    def tearDown(self) -> None:
        self.end_time = time.time()
        print(f"\n테스트 소요 시간: {self.end_time - self.start_time:4f}s")
        print(f"정렬 결과: {get_selection_sorted(SortingAlgorithmTest.random_numbers)}")

    def test_selection_sort(self):
        self.assertEqual(
            get_selection_sorted(SortingAlgorithmTest.random_numbers),
            SortingAlgorithmTest.sorted_random_numbers,
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
