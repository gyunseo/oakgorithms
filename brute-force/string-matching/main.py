import time, unittest, sys, re


def get_string_matching_result(given_str, pattern_str):
    pattern_str_start_indice = []
    given_str_size = len(given_str)
    pattern_str_size = len(pattern_str)
    for i in range(given_str_size - pattern_str_size + 1):
        for j in range(pattern_str_size):
            # given_str의 (i + j)번째 인덱스부터 pattern_str의 j번째 인덱스까지 비교
            # 하나라도 다르면 나가리
            if given_str[i + j] != pattern_str[j]:
                break
            if j == pattern_str_size - 1:
                # pattern_str의 마지막 인덱스까지 비교했는데도 다르지 않다면
                # pattern_str이 given_str에 존재한다는 의미
                pattern_str_start_indice.append(i)
    return pattern_str_start_indice


class StringMatchingTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        # input.txt를 읽기
        cls.str_data = sys.stdin.read()
        cls.pattern_str_start_indice = [
            match.start() for match in re.finditer(r"어린 왕자", cls.str_data)
        ]
        print("String Matching 테스트 시작")

    @classmethod
    def tearDownClass(cls) -> None:
        print("\nString Matching 테스트 종료\n")
        print("pattern string: 어린 왕자")
        print(
            f"'어린 왕자' pattern string start indice: {get_string_matching_result(cls.str_data, '어린 왕자')}"
        )
        print("나타난 횟수: ", len(get_string_matching_result(cls.str_data, "어린 왕자")))

    def setUp(self) -> None:
        self.start_time = time.time()

    def tearDown(self) -> None:
        self.end_time = time.time()
        print(
            f"\nget_string_matching_result 함수 소요 시간: {self.test_function_end_time - self.test_function_start_time:4f}s"
        )
        print(f"테스트 자체의 소요 시간: {self.end_time - self.start_time:4f}s")

    def test_string_matching(self):
        self.test_function_start_time = time.time()
        res = get_string_matching_result(StringMatchingTest.str_data, "어린 왕자")
        self.test_function_end_time = time.time()
        self.assertEqual(
            res,
            StringMatchingTest.pattern_str_start_indice,
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
