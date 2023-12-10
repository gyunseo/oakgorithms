import sys

input = sys.stdin.readline

input_word = input().rstrip()
word1, word2 = "tophat", "tomato"
len_input_word, len1, len2 = len(input_word), len(word1), len(word2)
dp_matrix1 = [[0] * (len_input_word + 1) for _ in range(len1 + 1)]
dp_matrix2 = [[0] * (len_input_word + 1) for _ in range(len2 + 1)]
for i in range(1, len_input_word + 1):
    for j in range(1, len1 + 1):
        if input_word[i - 1] == word1[j - 1]:
            dp_matrix1[i][j] = dp_matrix1[i - 1][j - 1] + 1
        else:
            dp_matrix1[i][j] = max(dp_matrix1[i][j - 1], dp_matrix1[i - 1][j])
print(dp_matrix1[-1][-1])

for i in range(1, len_input_word + 1):
    for j in range(1, len2 + 1):
        if input_word[i - 1] == word2[j - 1]:
            dp_matrix2[i][j] = dp_matrix2[i - 1][j - 1] + 1
        else:
            dp_matrix2[i][j] = max(dp_matrix2[i][j - 1], dp_matrix2[i - 1][j])

print(dp_matrix2[-1][-1])

if dp_matrix1[-1][-1] == dp_matrix2[-1][-1]:
    print(f"{word1}, {word2} 모두 대치 가능")
elif dp_matrix1[-1][-1] > dp_matrix2[-1][-1]:
    print(f"{word1} 대치 가능")
else:
    print(f"{word2} 대치 가능")
