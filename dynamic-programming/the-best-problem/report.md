---
mainfont: Sarasa Mono K
monofont: Sarasa Mono K
CJKmainfont: Sarasa Mono K
CJKmonofont: Sarasa Mono K
---

# Dynamic Programming the Best Problem Report

### 2019311801 이균서

## Execution Environment

### OS

```zsh
Distributor ID: Ubuntu
Description:    Ubuntu 22.04.3 LTS
Release:        22.04
Codename:       jammy
```

### `Python` Runtime

Python 3.11.6

### External Libraries

There is no external libraries used in the following source code.

`Pipfile`:

```
[[source]]
[[source]]
url = "https://pypi.org/simple"
verify_ssl = true
name = "pypi"

[packages]

[dev-packages]
cloudinary = "*"

[requires]
python_version = "3.11"
python_full_version = "3.11.6"
```

## Source Code

```python
import sys

sys.setrecursionlimit(100000)
input = sys.stdin.readline


def get_decoded_msg(msg):
    """
    >>> get_decoded_msg("25114")
    [['BEAAD', 'BEAN', 'BEKD', 'YAAD', 'YAN', 'YKD']]
    >>> get_decoded_msg("11271518920813")
    [['BHE', 'VE']]
    """
    # 알파벳을 숫자로 매핑
    alpha_to_num_dict = {chr(i + 64): str(i) for i in range(1, 27)}
    # 숫자를 알파벳으로 매핑
    num_to_alpha_dict = {v: k for k, v in alpha_to_num_dict.items()}

    def get_word_interpretation_cases(s):
        if not s:
            return [""]
        if s in memo:
            return memo[s]

        interpretation_cases = []
        for i in range(1, len(s) + 1):
            sliced_word = s[:i]
            if sliced_word in num_to_alpha_dict:
                cur_char = num_to_alpha_dict[sliced_word]
                for unsliced_word in get_word_interpretation_cases(s[i:]):
                    interpretation_cases.append(cur_char + unsliced_word)

        memo[s] = interpretation_cases
        return interpretation_cases

    # 메모이제이션을 위한 딕셔너리
    memo = {}

    # 메시지를 단어별로 분리
    words = msg.split()
    result = []

    # 각 단어에 대해 해독
    for word in words:
        if "." in word:
            word = word.replace(".", "")
            interpretation_cases_list_for_word = get_word_interpretation_cases(word)
            interpretation_cases_list_for_word = [
                case + "." for case in interpretation_cases_list_for_word
            ]
        else:
            interpretation_cases_list_for_word = get_word_interpretation_cases(word)
        result.append(interpretation_cases_list_for_word)
    return result


if __name__ == "__main__":
    interpretation_cases = 1
    interpretation_cases_for_words = get_decoded_msg(input().rstrip())
    for interpretation_cases_for_word in interpretation_cases_for_words:
        interpretation_cases *= len(interpretation_cases_for_word)
    print(interpretation_cases)
    for interpretation_cases_for_word in interpretation_cases_for_words:
        print(", ".join(interpretation_cases_for_word))

"""
THE ALGORITHM LECTURE THIS SEMESTER WAS MEANINGFUL AND INTERESTING. THANK YOU FOR SOLVING THE RANDOM TEAM PROBLEM.
"""

```

## Execution Result

### How to run `main.py`:

```zsh
pipenv run python3 main.py < input.txt > output.txt
```

or

```zsh
python3 main.py < input.txt > output.txt
```

- 실행이 안되면 <https://github.com/gyunseo/oakgorithms.git>을 `git clone` 하여, root directory에서 `pipenv install`을 하시고 `dynamic-programming/the-best-problem/`로 이동하셔서 `pipenv run python3 main.py < input.txt > output.txt`를 하시면 됩니다.

### Input

`input.txt`:

```
2085 11271518920813 12532021185 208919 1951351920518 23119 135114914762112 1144 91420518519209147. 20811411 251521 61518 191512229147 2085 1811441513 205113 161815212513.
```

### Output

`output.txt`:

```
8806025134080000
THE
AABGAEAHITHAC, AABGAEAHITHM, AABGAERITHAC, AABGAERITHM, AABGOAHITHAC, AABGOAHITHM, AABGORITHAC, AABGORITHM, ALGAEAHITHAC, ALGAEAHITHM, ALGAERITHAC, ALGAERITHM, ALGOAHITHAC, ALGOAHITHM, ALGORITHAC, ALGORITHM, KBGAEAHITHAC, KBGAEAHITHM, KBGAERITHAC, KBGAERITHM, KBGOAHITHAC, KBGOAHITHM, KBGORITHAC, KBGORITHM
ABECTBAAHE, ABECTBARE, ABECTBKHE, ABECTUAHE, ABECTURE, AYCTBAAHE, AYCTBARE, AYCTBKHE, AYCTUAHE, AYCTURE, LECTBAAHE, LECTBARE, LECTBKHE, LECTUAHE, LECTURE
THIAI, THIS
AIEACEAITEAH, AIEACEAITER, AIEACESTEAH, AIEACESTER, AIEMEAITEAH, AIEMEAITER, AIEMESTEAH, AIEMESTER, SEACEAITEAH, SEACEAITER, SEACESTEAH, SEACESTER, SEMEAITEAH, SEMEAITER, SEMESTEAH, SEMESTER
BCAAI, BCAS, BCKI, WAAI, WAS, WKI
ACEAADIADGFBAAB, ACEAADIADGFBAL, ACEAADIADGFBKB, ACEAADIADGFUAB, ACEAADIADGFUL, ACEAADINGFBAAB, ACEAADINGFBAL, ACEAADINGFBKB, ACEAADINGFUAB, ACEAADINGFUL, ACEANIADGFBAAB, ACEANIADGFBAL, ACEANIADGFBKB, ACEANIADGFUAB, ACEANIADGFUL, ACEANINGFBAAB, ACEANINGFBAL, ACEANINGFBKB, ACEANINGFUAB, ACEANINGFUL, ACEKDIADGFBAAB, ACEKDIADGFBAL, ACEKDIADGFBKB, ACEKDIADGFUAB, ACEKDIADGFUL, ACEKDINGFBAAB, ACEKDINGFBAL, ACEKDINGFBKB, ACEKDINGFUAB, ACEKDINGFUL, MEAADIADGFBAAB, MEAADIADGFBAL, MEAADIADGFBKB, MEAADIADGFUAB, MEAADIADGFUL, MEAADINGFBAAB, MEAADINGFBAL, MEAADINGFBKB, MEAADINGFUAB, MEAADINGFUL, MEANIADGFBAAB, MEANIADGFBAL, MEANIADGFBKB, MEANIADGFUAB, MEANIADGFUL, MEANINGFBAAB, MEANINGFBAL, MEANINGFBKB, MEANINGFUAB, MEANINGFUL, MEKDIADGFBAAB, MEKDIADGFBAL, MEKDIADGFBKB, MEKDIADGFUAB, MEKDIADGFUL, MEKDINGFBAAB, MEKDINGFBAL, MEKDINGFBKB, MEKDINGFUAB, MEKDINGFUL
AADD, AND, KDD
IADTEAHEAITIADG., IADTEAHEAITING., IADTEAHESTIADG., IADTEAHESTING., IADTEREAITIADG., IADTEREAITING., IADTERESTIADG., IADTERESTING., INTEAHEAITIADG., INTEAHEAITING., INTEAHESTIADG., INTEAHESTING., INTEREAITIADG., INTEREAITING., INTERESTIADG., INTERESTING.
THAADAA, THAADK, THANAA, THANK, THKDAA, THKDK
BEAEBA, BEAEU, BEOBA, BEOU, YAEBA, YAEU, YOBA, YOU
FAEAH, FAER, FOAH, FOR
AIAEABBBIADG, AIAEABBBING, AIAEABVIADG, AIAEABVING, AIAEAVBIADG, AIAEAVBING, AIAELBBIADG, AIAELBBING, AIAELVIADG, AIAELVING, AIOABBBIADG, AIOABBBING, AIOABVIADG, AIOABVING, AIOAVBIADG, AIOAVBING, AIOLBBIADG, AIOLBBING, AIOLVIADG, AIOLVING, SAEABBBIADG, SAEABBBING, SAEABVIADG, SAEABVING, SAEAVBIADG, SAEAVBING, SAELBBIADG, SAELBBING, SAELVIADG, SAELVING, SOABBBIADG, SOABBBING, SOABVIADG, SOABVING, SOAVBIADG, SOAVBING, SOLBBIADG, SOLBBING, SOLVIADG, SOLVING
THE
AHAADDAEAC, AHAADDAEM, AHAADDOAC, AHAADDOM, AHANDAEAC, AHANDAEM, AHANDOAC, AHANDOM, AHKDDAEAC, AHKDDAEM, AHKDDOAC, AHKDDOM, RAADDAEAC, RAADDAEM, RAADDOAC, RAADDOM, RANDAEAC, RANDAEM, RANDOAC, RANDOM, RKDDAEAC, RKDDAEM, RKDDOAC, RKDDOM
TEAAC, TEAM, TEKC
AFAHAEBABEAC., AFAHAEBABEM., AFAHAEBAYAC., AFAHAEBAYM., AFAHAEBLEAC., AFAHAEBLEM., AFAHAEUBEAC., AFAHAEUBEM., AFAHAEUYAC., AFAHAEUYM., AFAHOBABEAC., AFAHOBABEM., AFAHOBAYAC., AFAHOBAYM., AFAHOBLEAC., AFAHOBLEM., AFAHOUBEAC., AFAHOUBEM., AFAHOUYAC., AFAHOUYM., AFRAEBABEAC., AFRAEBABEM., AFRAEBAYAC., AFRAEBAYM., AFRAEBLEAC., AFRAEBLEM., AFRAEUBEAC., AFRAEUBEM., AFRAEUYAC., AFRAEUYM., AFROBABEAC., AFROBABEM., AFROBAYAC., AFROBAYM., AFROBLEAC., AFROBLEM., AFROUBEAC., AFROUBEM., AFROUYAC., AFROUYM., PAHAEBABEAC., PAHAEBABEM., PAHAEBAYAC., PAHAEBAYM., PAHAEBLEAC., PAHAEBLEM., PAHAEUBEAC., PAHAEUBEM., PAHAEUYAC., PAHAEUYM., PAHOBABEAC., PAHOBABEM., PAHOBAYAC., PAHOBAYM., PAHOBLEAC., PAHOBLEM., PAHOUBEAC., PAHOUBEM., PAHOUYAC., PAHOUYM., PRAEBABEAC., PRAEBABEM., PRAEBAYAC., PRAEBAYM., PRAEBLEAC., PRAEBLEM., PRAEUBEAC., PRAEUBEM., PRAEUYAC., PRAEUYM., PROBABEAC., PROBABEM., PROBAYAC., PROBAYM., PROBLEAC., PROBLEM., PROUBEAC., PROUBEM., PROUYAC., PROUYM.
```

## Execution Image

![Alt text](image.png)
![Alt text](image-1.png)
