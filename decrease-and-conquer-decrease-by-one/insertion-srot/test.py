import time, unittest
from main import get_insertion_sorted


def save_sort_procedure(fn):
    def wrapper(arr):
        arr_size = len(arr)
        for i in range(1, arr_size):
            key_val = arr[i]
            j = i - 1
            while j >= 0 and key_val < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key_val
            InsertionSortTest.sort_procedure.append(arr[:])
        return arr

    return wrapper


@save_sort_procedure
def get_insertion_sorted(arr):
    arr_size = len(arr)
    for i in range(1, arr_size):
        key_val = arr[i]
        j = i - 1
        while j >= 0 and key_val < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key_val
    return arr


class InsertionSortTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.random_numbers = list(map(int, input().strip("[").strip("]").split(",")))
        cls.sorted_random_numbers = sorted(cls.random_numbers)
        cls.sort_procedure = []
        print("Insertion Sort 테스트 시작")

    @classmethod
    def tearDownClass(cls) -> None:
        print("\nInsertion Sort 테스트 종료\n")

        print("Insertion Sort 과정을 출력합니다.")
        # for i, procedure in enumerate(cls.sort_procedure):
        #     print(f"{i + 1}번째 과정: {procedure}")
        print(f"{cls.sort_procedure[-8]}")
        print(f"{cls.sort_procedure[-7]}")

    def setUp(self) -> None:
        self.start_time = time.time()

    def tearDown(self) -> None:
        self.end_time = time.time()
        print(
            f"\nget_insertion_sorted 함수 소요 시간: {self.test_function_end_time - self.test_function_start_time:4f}s"
        )
        print(f"\n테스트 소요 시간: {self.end_time - self.start_time:4f}s")

    def test_insertion_sort(self):
        self.test_function_start_time = time.time()
        res = get_insertion_sorted(InsertionSortTest.random_numbers)
        self.test_function_end_time = time.time()
        self.assertEqual(
            res,
            InsertionSortTest.sorted_random_numbers,
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
