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


class Person:
    def __init__(self, name):
        self.name = name
        self.cur_task = None
        self.cur_task_timer = None
        self.task_history = []


사람마다_걸리는_시간 = {"eunji": {}, "hyeonsang": {}, "seongmin": {}, "jaeseo": {}}
# 처음에는 eunji, hyeonsang, seongmin, jaeseo 순으로 정렬
팀원들 = [Person("eunji"), Person("hyeonsang"), Person("seongmin"), Person("jaeseo")]
# csv로 입력받아서 리스트로 반환
with open("hackathon_task.csv", "r") as file:
    for line in file:
        (
            task_name,
            eunji_time,
            hyeonsang_time,
            seongmin_time,
            jaeseo_time,
        ) = line.strip().split(",")
        if task_name == "task":  # 헤더 라인은 건너뛰기
            continue
        사람마다_걸리는_시간["eunji"][task_name] = int(eunji_time)
        사람마다_걸리는_시간["hyeonsang"][task_name] = int(hyeonsang_time)
        사람마다_걸리는_시간["seongmin"][task_name] = int(seongmin_time)
        사람마다_걸리는_시간["jaeseo"][task_name] = int(jaeseo_time)

# print(f"{사람마다_걸리는_시간}\n")
남은_일 = {"frontend", "backend", "ppt", "ai", "crawling", "기획안작성", "발표준비", "자료조사"}
# 초기 일 할당
for 팀원 in 팀원들:
    # 팀원이 할 수 있는 일 중, 시간이 가장 적게 걸리는 일을 찾는다.\
    # print(팀원.name)
    for 현팀원이_할_일 in sorted(사람마다_걸리는_시간[팀원.name].items(), key=lambda x: x[1]):
        if 현팀원이_할_일[0] in 남은_일:
            # print(f"{팀원.name}은 {현팀원이_할_일[0]}을(를) 할 수 있습니다. 이 일은 {현팀원이_할_일[1]}시간 걸립니다.")
            팀원.cur_task = 현팀원이_할_일[0]
            팀원.cur_task_timer = 현팀원이_할_일[1]
            팀원.task_history.append((현팀원이_할_일[0], 현팀원이_할_일[1]))
            남은_일.remove(현팀원이_할_일[0])
            break
# print(남은_일)
while True:
    # 모든 팀원이 일을 다 끝냈으면 종료
    if len(남은_일) == 0:
        break
    for 팀원 in 팀원들:
        if 팀원.cur_task_timer == 0:
            # print(f"{팀원.name}은 {팀원.cur_task}를 끝냈습니다.")
            # print("남은 일들 중에 할 수 있는 일을 찾습니다.")
            팀원.cur_task = None
            팀원.cur_task_timer = None
            for 현팀원이_할_일 in sorted(사람마다_걸리는_시간[팀원.name].items(), key=lambda x: x[1]):
                if 현팀원이_할_일[0] in 남은_일:
                    # print(
                    #     f"{팀원.name}은 {현팀원이_할_일[0]}을(를) 할 수 있습니다. 이 일은 {현팀원이_할_일[1]}시간 걸립니다."
                    # )
                    팀원.cur_task = 현팀원이_할_일[0]
                    팀원.cur_task_timer = 현팀원이_할_일[1]
                    팀원.task_history.append((현팀원이_할_일[0], 현팀원이_할_일[1]))
                    남은_일.remove(현팀원이_할_일[0])
                    break

        팀원.cur_task_timer -= 1

max_task_time = -1
for 팀원 in 팀원들:
    tmp_task_time_sum = 0
    print(팀원.name, end=": ")
    for i, task in enumerate(팀원.task_history):
        tmp_task_time_sum += task[1]
        if i == len(팀원.task_history) - 1:
            print(f"{task[0]}({task[1]})")
        else:
            print(f"{task[0]}({task[1]})", end="->")
    if tmp_task_time_sum > max_task_time:
        max_task_time = tmp_task_time_sum

print(f"해커톤 1차 결과물 완성시간: {max_task_time}분")
