# Copyright 2023 gyunseo
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import sys

# method aliasing
input = sys.stdin.readline
print = sys.stdout.write


# csv 파일 읽기
data = []
with open("foods.csv", "r") as file:
    for line in file:
        food, protein = line.strip().split(",")
        if food == "food":  # 헤더 라인은 건너뛰기
            continue
        data.append((food, float(protein)))

sorted_data = sorted(data, key=lambda x: x[1])
# print(f"{sorted_data}\n")
protein_target = float(input())

# interpolation search to find the  index of element that is equal to the protein_target

low = 0
high = len(sorted_data) - 1

while low <= high:
    if sorted_data[low][1] == sorted_data[high][1]:
        break

    # 이분 탐색과 구분되는 보간 탐색의 핵심 로직
    mid = low + int(
        (high - low)
        * (protein_target - sorted_data[low][1])
        / (sorted_data[high][1] - sorted_data[low][1])
    )

    if sorted_data[mid][1] == protein_target:
        low = mid
        break
    elif sorted_data[mid][1] < protein_target:
        low = mid + 1
    else:
        high = mid - 1

# output 포맷에 맞게 설정
print(f"{sorted_data[low][0]} {sorted_data[low][1]}g\n")
