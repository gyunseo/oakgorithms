# 주제: 카드 선택을 통한 최대 효율을 찾는 Branch and Bound 기반의 프로그램

## 누구에게 도움이 되는가? (Contribution)

이 프로그램은 소비자들이 다양한 카드 중에서 가장 효율적인 카드를 선택하는 데 도움을 줍니다. 또한, 카드 회사나 금융 기관은 고객들에게 최적의 혜택을 제공하여 경쟁력을 확보할 수 있습니다.

## 왜 Branch and Bound에 해당하는가? (Strategy)

Branch and Bound은 가능한 해를 효율적으로 탐색하는 데 사용되는 전략 중 하나입니다. 카드 선택 문제는 다양한 카드 중에서 최적의 조합을 찾는 문제로, 이를 부분 문제로 나누고 탐색하여 최적의 해를 찾는 데에 Branch and Bound 전략이 적합합니다.

## 알고리즘 정의 (IOP)

### INPUT

결제할 가격

### OUTPUT

효율적인 카드 추천

### PROCESS

- 문제 정의 (Problem Definition): 카드의 정보인 [최소 결제 금액, 할인 퍼센트, 최대 할인 가능 금액]을 고려하여 최대 효율을 내는 카드 선택.

- 하한치 계산 (Calculation of Lower Bound): 각 부분 문제에 대해 현재까지 선택된 카드들의 혜택을 계산하고, 이를 이용하여 남은 카드들의 최대 예상 혜택을 추정하는 하한치를 계산.

- Branching: 현재 선택된 카드와 선택되지 않은 카드로 나누어 두 가지 경우로 분기. 이때, 가능한 조합을 탐색하면서 가지치기를 수행하여 탐색 공간을 효과적으로 축소.

탐색을 반복하면서 최적의 카드 조합을 찾아나감. 각 분기에서 계산된 혜택을 비교하여 가장 효율적인 조합을 찾음.

```plaintext
                                 [카드]
                                /        \
                [카드 선택 O]               [카드 선택 X]
                   /    \                       /   \

[다음 카드 선택 O] [다음 카드 선택 X] [다음 카드 선택 x] [다음 카드 선택 X]
/ \ | / \ |
[...] [최적 조합] [...] [...] [최적 조합]
```
