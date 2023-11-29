import time, unittest
from itertools import permutations


def get_min_tsp_path(graph, starting_vertex):
    tsp_path_candidates = [*permutations(range(2, 6), 4)]
    min_tsp_weight_sum = 1000000
    min_tsp_path = tsp_path_candidates[0]

    def get_next_vertex_weight_for_cur_vertex(cur_vertex, next_vertex):
        for nv_candidate, w in graph[cur_vertex]:
            if nv_candidate == next_vertex:
                return w

    # 외판원 순회 경로를 순열로 구한 후, 각 경로의 가중치 합을 구한다.
    # 그 중 가장 작은 가중치 합을 구한다.
    for candidate_path in tsp_path_candidates:
        cv = starting_vertex
        tsp_weight_sum = 0
        for nv in candidate_path:
            tsp_weight_sum += get_next_vertex_weight_for_cur_vertex(cv, nv)
            cv = nv
        tsp_weight_sum += get_next_vertex_weight_for_cur_vertex(cv, starting_vertex)
        if tsp_weight_sum < min_tsp_weight_sum:
            min_tsp_weight_sum = tsp_weight_sum
            min_tsp_path = candidate_path

    return ((starting_vertex, *min_tsp_path, starting_vertex), min_tsp_weight_sum)


class TSPTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        # input.txt를 읽기
        cls.graph = [
            [],  # 정점 0은 사용하지 않으며, 1부터 시작한다.
            [(2, 2), (3, 3), (4, 2), (5, 3)],  # 정점 1에서 다른 정점으로 가는 가중치
            [(1, 2), (3, 3), (4, 4), (5, 1)],  # 정점 2에서 다른 정점으로 가는 가중치
            [(1, 3), (2, 3), (4, 2), (5, 4)],  # 정점 3에서 다른 정점으로 가는 가중치
            [(1, 2), (2, 4), (3, 2), (5, 5)],  # 정점 4에서 다른 정점으로 가는 가중치
            [(1, 3), (2, 1), (3, 4), (4, 5)],  # 정점 5에서 다른 정점으로 가는 가중치
        ]
        cls.starting_vertex = 1
        print("Brute Force TSP 테스트 시작")

    @classmethod
    def tearDownClass(cls) -> None:
        print("\nBrute Force TSP 테스트 종료\n")
        print(
            f"최소 비용 외판원 순회 경로: {get_min_tsp_path(TSPTest.graph, TSPTest.starting_vertex)[0]}"
        )
        print(
            f"최소 비용 외판원 순회 경로 가중치 합: {get_min_tsp_path(TSPTest.graph, TSPTest.starting_vertex)[1]}"
        )

    def setUp(self) -> None:
        self.start_time = time.time()

    def tearDown(self) -> None:
        self.end_time = time.time()
        print(
            f"\nget_min_tsp_path 함수 소요 시간: {self.test_function_end_time - self.test_function_start_time:4f}s"
        )
        print(f"테스트 자체의 소요 시간: {self.end_time - self.start_time:4f}s")

    def test_tsp(self):
        self.test_function_start_time = time.time()
        res = get_min_tsp_path(TSPTest.graph, TSPTest.starting_vertex)
        self.test_function_end_time = time.time()
        self.assertEqual(res, ((1, 2, 5, 3, 4, 1), 11))


if __name__ == "__main__":
    unittest.main(verbosity=2)
