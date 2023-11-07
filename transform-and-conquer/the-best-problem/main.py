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

# trie code 참고 https://m.blog.naver.com/cjsencks/221740232900


class Node:
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.children = {}


class Trie:
    def __init__(self):
        self.head = Node(None)

    def insert(self, string):
        cur_node = self.head

        for ch in string:
            if ch not in cur_node.children:
                cur_node.children[ch] = Node(ch)
            cur_node = cur_node.children[ch]
        cur_node.data = string

    def search(self, string):
        current_node = self.head

        for ch in string:
            if ch in current_node.children:
                current_node = current_node.children[ch]
            else:
                return False

        if current_node.data:
            return True
        else:
            return False

    def starts_with(self, prefix):
        current_node = self.head
        words = []

        for p in prefix:
            if p in current_node.children:
                current_node = current_node.children[p]
            else:
                return None

        current_node = [current_node]
        next_node = []
        while True:
            for node in current_node:
                if node.data:
                    words.append(node.data)
                next_node.extend(list(node.children.values()))
            if len(next_node) != 0:
                current_node = next_node
                next_node = []
            else:
                break

        return words


import sys

trie = Trie()
input = sys.stdin.readline
print = sys.stdout.write

target_word = input().rstrip()
word_list = []
with open("google-10000-english.txt", "r") as f:
    for line in f.readlines():
        word_list.append(line.rstrip())
for word in word_list:
    trie.insert(word)

if not trie.search(target_word):
    print("NONE\n")
else:
    print(" ".join(trie.starts_with(target_word)))
    print("\n")
