import sys, unittest, time

sys.setrecursionlimit(10**9)


def get_gcd(a, b):
    if b == 0:
        return a
    return get_gcd(b, a % b)


def get_lcm(a, b):
    return a * b // get_gcd(a, b)


class LCMTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print("LCM(Least Common Multiple) 테스트 시작\n")

    @classmethod
    def tearDownClass(cls) -> None:
        print("\nLCM(Least Common Multiple) 테스트 종료\n")
        print(f"1071과 1029의 최소공배수: {get_lcm(1071, 1029)}")

    def setUp(self) -> None:
        self.start_time = time.time()

    def tearDown(self) -> None:
        self.end_time = time.time()
        print(f"\n테스트 소요 시간: {self.end_time - self.start_time:4f}s")

    def test_lcm(self):
        """
        1071과 1029의 최소공배수를 구하는 테스트
        """
        self.assertEqual(get_lcm(1071, 1029), 52479)


if __name__ == "__main__":
    unittest.main(verbosity=2)
