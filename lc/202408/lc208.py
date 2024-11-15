"""
LC 208: Implement Trie (Prefix Tree)

A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

Implement the Trie class:

- Trie() Initializes the trie object.
- void insert(String word) Inserts the string word into the trie.
- boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
- boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.

Example 1:

Input
["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
Output
[null, null, true, false, true, null, true]

Explanation
Trie trie = new Trie();
trie.insert("apple");
trie.search("apple");   // return True
trie.search("app");     // return False
trie.startsWith("app"); // return True
trie.insert("app");
trie.search("app");     // return True



Constraints:

    1 <= word.length, prefix.length <= 2000
    word and prefix consist only of lowercase English letters.
    At most 3 * 104 calls in total will be made to insert, search, and startsWith.
"""

# 12
class Trie:
    def __init__(self):
        self.prefix_dict = {}
        self.word_dict = set()

    def insert(self, word: str) -> None:
        """Inserts the string word into the trie."""
        if word in self.word_dict:
            return
        self.word_dict.add(word)
        j, cur = self.find_prefix_dict(word)
        for i in range(j+1, len(word)):
            cur[word[i]] = {}
            cur = cur[word[i]]

    def search(self, word: str) -> bool:
        """
        Returns true if the string word is in the trie (i.e., was inserted before),
        and false otherwise.
        """
        return word in self.word_dict

    def startsWith(self, prefix: str) -> bool:
        """
        Returns true if there is a previously inserted string word that has the prefix `prefix`,
        and false otherwise.
        """
        j, cur = self.find_prefix_dict(prefix)
        return j+1==len(prefix)

    def find_prefix_dict(self, word: str) -> str:
        cur = self.prefix_dict
        j = -1
        for i, char in enumerate(word):
            if char in cur:
                cur = cur[char]
                j = i
            else:
                break
        return j, cur

class Trie: 
    def __init__(self):
        self.root = {}
        self.termination = '*'

    def insert(self, word: str): 
        node, i = self._traverse(word)
        while i < len(word):
            c = word[i]
            node[c] = {}
            node = node[c]
            i += 1
        node[self.termination] = {}

    def search(self, word: str) -> bool: 
        node, i = self._traverse(word)
        return i==len(word) and self.termination in node

    def startsWith(self, prefix: str) -> bool: 
        node, i = self._traverse(prefix)
        return i==len(prefix)

    def _traverse(self, seq):
        i = 0
        node = self.root
        while i < len(seq):
            c = seq[i]
            if c not in node:
                break
            node = node[c]
            i += 1
        return node, i

class Trie:
    # withouth a set (less optimal)
    def __init__(self):
        self.prefix_dict = {}

    def insert(self, word: str) -> None:
        """Inserts the string word into the trie."""
        j, cur = self.find_prefix_dict(word)
        for i in range(j+1, len(word)):
            cur[word[i]] = {}
            cur = cur[word[i]]
        cur['*'] = {}

    def search(self, word: str) -> bool:
        """
        Returns true if the string word is in the trie (i.e., was inserted before),
        and false otherwise.
        """
        j, cur = self.find_prefix_dict(word)
        return j+1==len(word) and '*' in cur

    def startsWith(self, prefix: str) -> bool:
        """
        Returns true if there is a previously inserted string word that has the prefix `prefix`,
        and false otherwise.
        """
        j, cur = self.find_prefix_dict(prefix)
        return j+1==len(prefix)

    def find_prefix_dict(self, word: str) -> str:
        cur = self.prefix_dict
        j = -1
        for i, char in enumerate(word):
            if char in cur:
                cur = cur[char]
                j = i
            else:
                break
        return j, cur

class Trie:
    # without a set (less optimal)
    # functional style
    def __init__(self):
        self.prefix_dict = {}

    def insert(self, word: str) -> None:
        """Inserts the string word into the trie."""
        def fnc(j, cur):
            for i in range(j+1, len(word)):
                cur[word[i]] = {}
                cur = cur[word[i]]
            cur['*'] = {}
        return self.find_prefix_dict(word, fnc)

    def search(self, word: str) -> bool:
        """
        Returns true if the string word is in the trie (i.e., was inserted before),
        and false otherwise.
        """
        def fnc(j, cur):
            return j+1==len(word) and '*' in cur
        return self.find_prefix_dict(word, fnc)

    def startsWith(self, prefix: str) -> bool:
        """
        Returns true if there is a previously inserted string word that has the prefix `prefix`,
        and false otherwise.
        """
        def fnc(j, cur):
            return j+1==len(prefix)
        return self.find_prefix_dict(prefix, fnc)

    def find_prefix_dict(self, word: str, fnc) -> str:
        cur = self.prefix_dict
        j = -1
        for i, char in enumerate(word):
            if char in cur:
                cur = cur[char]
                j = i
            else:
                break
        return fnc(j, cur)

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

obj = Trie()
rv = [obj.insert("apple"),
obj.search("apple"),
obj.search("app"),
obj.startsWith("app"),
obj.insert("app"),
obj.search("app"),
]
print(rv)
assert rv==[None, True, False, True, None, True]
# Output: [null, true, false, true, null, true]
