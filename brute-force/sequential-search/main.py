import sys, unittest, time

input = sys.stdin.readline


def get_sequential_search_result(data_list, target):
    for i in range(len(data_list)):
        if data_list[i] == target:
            return i
    raise ValueError(f"{target} is not in list")


class SequentialSearchTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        # input.txt 값 읽기
        cls.data = [*map(int, input().strip("]").strip("[").split(","))]
        # print(f"입력 값: {cls.data}")
        print("Sequential Search 테스트 시작")

    @classmethod
    def tearDownClass(cls) -> None:
        print("\nSequential Search 테스트 종료\n")
        for target in [237333, 357001, 317436]:
            try:
                print(
                    f"target: {target}, index: {get_sequential_search_result(cls.data, target)}"
                )
            except ValueError as e:
                print(e)

    def setUp(self) -> None:
        self.start_time = time.time()

    def tearDown(self) -> None:
        self.end_time = time.time()
        print(f"\n테스트 소요 시간: {self.end_time - self.start_time:4f}s")

    def test_sequential_search_target_237333(self):
        self.assertEqual(
            get_sequential_search_result(SequentialSearchTest.data, 237333),
            SequentialSearchTest.data.index(237333),
        )

    def test_sequential_search_target_357001(self):
        with self.assertRaises(ValueError):
            get_sequential_search_result(SequentialSearchTest.data, 357001)

    def test_sequential_search_target_317436(self):
        self.assertEqual(
            get_sequential_search_result(SequentialSearchTest.data, 317436),
            SequentialSearchTest.data.index(317436),
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
