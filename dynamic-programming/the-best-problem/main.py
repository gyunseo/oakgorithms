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
