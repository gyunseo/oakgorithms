import time, unittest
from itertools import permutations
import math


def get_min_cost(job_table):
    # 경우의 수는 10!
    jobs_size = len(job_table)
    min_cost = math.inf
    min_queuing_order_for_jobs = None
    # 사람 10 명 중 10 명을 뽑아서, job에 할당한다.
    # job은 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 순으로 흩뜨려져 있다.
    for queuing_order_for_jobs in permutations(range(10), 10):
        tmp_cost = 0
        for i in range(jobs_size):
            tmp_cost += job_table[i][queuing_order_for_jobs[i]]
        if tmp_cost < min_cost:
            # min_cost update
            min_cost = tmp_cost
            min_queuing_order_for_jobs = queuing_order_for_jobs
    return min_cost, min_queuing_order_for_jobs


class JobAssignmentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        # 행 job0, job1, job2, job3, job4, job5, job6, job7, job8, job9
        # 열 worker0, worker1, worker2, worker3, worker4, worker5, worker6, worker7, worker8, worker9
        cls.job_table = [
            [13, 6, 7, 12, 14, 15, 10, 11, 15, 4],
            [8, 14, 11, 9, 6, 14, 7, 9, 16, 12],
            [10, 8, 10, 10, 8, 15, 11, 5, 7, 9],
            [13, 13, 16, 9, 13, 16, 15, 9, 14, 16],
            [11, 4, 9, 14, 12, 11, 5, 16, 8, 14],
            [7, 10, 12, 13, 4, 11, 16, 12, 15, 9],
            [6, 11, 10, 11, 13, 15, 7, 16, 11, 12],
            [7, 15, 5, 10, 4, 16, 12, 4, 10, 16],
            [5, 14, 10, 15, 8, 8, 8, 14, 14, 4],
            [8, 11, 4, 16, 8, 12, 4, 14, 9, 6],
        ]

    print("Brute Force Job Assignment 테스트 시작")

    @classmethod
    def tearDownClass(cls) -> None:
        print("\nBrute Force Job Assignment 테스트 종료\n")
        print(f"job을 모두 수행하는 데에 드는 min cost: {get_min_cost(cls.job_table)[0]}")
        print(f"jobs에 대하여 worker들을 배치한 순서: {get_min_cost(cls.job_table)[1]}")

    def setUp(self) -> None:
        self.start_time = time.time()

    def tearDown(self) -> None:
        self.end_time = time.time()
        print(
            f"\nget_min_cost 함수 소요 시간: {self.test_function_end_time - self.test_function_start_time:4f}s"
        )
        print(f"테스트 자체의 소요 시간: {self.end_time - self.start_time:4f}s")

    def test_tsp(self):
        self.test_function_start_time = time.time()
        res = get_min_cost(JobAssignmentTest.job_table)
        self.test_function_end_time = time.time()
        self.assertEqual(res, (57, (9, 6, 8, 3, 1, 4, 0, 7, 5, 2)))


if __name__ == "__main__":
    unittest.main(verbosity=2)
