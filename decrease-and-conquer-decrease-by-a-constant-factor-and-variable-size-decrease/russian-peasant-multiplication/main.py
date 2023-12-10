import time


def normal_multiplication(a, b):
    start_at = time.time()
    result = a * b
    end_at = time.time()
    print(f"elapsed time: {end_at - start_at:.10f}s")
    return result


def get_russian_peasant_multiplication(a, b):
    start_at = time.time()
    result = 0
    while a > 0:
        if a & 1:
            result += b
        a = a >> 1
        b = b << 1
    end_at = time.time()
    print(f"elapsed time: {end_at - start_at:.10f}s")
    return result


A = 195342362382473513845003428
B = 399253634579252174384
import time

start_at = time.time()
russian_result = get_russian_peasant_multiplication(A, B)
print("로씨아 농부 곱셈 알고리즘")
print(f"result: {russian_result}, type: {type(russian_result)}")
print()
normal_result = normal_multiplication(A, B)
print("파이썬 곱셈 연산자")
print(f"result: {normal_result}, type: {type(normal_result)}")
