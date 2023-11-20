import unittest, time, pdb
from main import get_heap_sorted_list


class HeapSortTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print("heapsort 테스트 시작")

    @classmethod
    def tearDownClass(cls) -> None:
        print("\nheapsort 테스트 종료\n")

    def setUp(self) -> None:
        self.start_time = time.time()

    def tearDown(self) -> None:
        self.end_time = time.time()
        print(f"\n테스트 소요 시간: {self.end_time - self.start_time:4f}s")

    def test_heapsort(self):
        """
        >>> get_heap_sorted_list([31, 30, 23, 2, 33, 61, 87, 58, 53, 32, 68, 29, 38, 34, 66, 42, 8, 21, 125, 341, 221, 648, 62, 1, 921], "min")
        [921, 648, 341, 221, 125, 87, 68, 66, 62, 61, 58, 53, 42, 38, 34, 33, 32, 31, 30, 29, 23, 21, 8, 2, 1]
        """
        pdb.set_trace()
        self.assertEqual(
            get_heap_sorted_list(
                [
                    31,
                    30,
                    23,
                    2,
                    33,
                    61,
                    87,
                    58,
                    53,
                    32,
                    68,
                    29,
                    38,
                    34,
                    66,
                    42,
                    8,
                    21,
                    125,
                    341,
                    221,
                    648,
                    62,
                    1,
                    921,
                ],
                "min",
            ),
            [
                921,
                648,
                341,
                221,
                125,
                87,
                68,
                66,
                62,
                61,
                58,
                53,
                42,
                38,
                34,
                33,
                32,
                31,
                30,
                29,
                23,
                21,
                8,
                2,
                1,
            ],
        )


if __name__ == "__main__":
    unittest.main()
