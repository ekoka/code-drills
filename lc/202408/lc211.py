"""
LC 211: Design Add and Search Word Data Structure

Design a data structure that supports adding new words and finding if a string matches any previously added string.

Implement the WordDictionary class:

- WordDictionary() Initializes the object.
- void addWord(word) Adds word to the data structure, it can be matched later.
- bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.


Example:

Input
["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
Output
[null,null,null,null,false,true,true,true]

Explanation
WordDictionary wordDictionary = new WordDictionary();
wordDictionary.addWord("bad");
wordDictionary.addWord("dad");
wordDictionary.addWord("mad");
wordDictionary.search("pad"); // return False
wordDictionary.search("bad"); // return True
wordDictionary.search(".ad"); // return True
wordDictionary.search("b.."); // return True



Constraints:

    1 <= word.length <= 25
    word in addWord consists of lowercase English letters.
    word in search consist of '.' or lowercase English letters.
    There will be at most 2 dots in word for search queries.
    At most 104 calls will be made to addWord and search.

"""
#09 - 29 -
#06

class WordDictionary:
    def __init__(self):
        self.words = {}

    def addWord(self, word):
        """Adds word to the data structure, it can be matched later."""
        cur = self.words
        for c in word:
            if c in cur:
                cur = cur[c]
            else:
                cur[c] = {}
                cur = cur[c]
        cur['*'] = {}

    def search(self, word) -> bool:
        """
        Returns true if there is any string in the data structure that matches `word`
        or false otherwise. word may contain dots '.' where dots can be matched with
        any letter.
        """
        N = len(word)
        q = [self.words]
        i = 0
        while q:
            if i==N:
                for cur in q:
                    if '*' in cur: return True
                return False
            next_q = []
            c = word[i]
            while q:
                cur = q.pop()
                if c in cur:
                    next_q.append(cur[c])
                elif c=='.':
                    for k,v in cur.items():
                        next_q.append(v)
            i += 1
            q = next_q
        return False

class WordDictionary: 
    def __init__(self):
        self.root = {}
        self.term = '*'

    def addWord(self, word: str):
        i = 0
        node = self.root
        while i < len(word):
            c = word[i]
            if c not in node: break
            node = node[c]
            i += 1
        while i < len(word):
            c = word[i]
            node[c] = {}
            node = node[c]
            i += 1
        node[self.term] = {}

    def search(self, word: str) -> bool: # bfs
        word += self.term
        stack = [self.root]
        i = 0
        while stack:
            next_stack = []
            while stack:
                if i==len(word): 
                    return True
                n = stack.pop()
                c = word[i]
                if c==".":
                    for k,v in n.items():
                        nxt_stack.append(v)
                else:
                    if c in n:
                        nxt_stack.append(n[c])
            stack = nxt_stack
            i += 1
        return False

    def search(self, word: str) -> bool: # dfs
        word += self.term
        N = len(word)
        if not N: return False
        nodes = [self.root]
        def dfs(i): 
            if i==N: return True
            c = word[i]
            curr = nodes[-1]
            if c=='.': 
                nodeset = [n for k, n in curr.items()]
            else:
                nodeset = [curr[c]] if c in curr else []
            for n in nodeset:
                nodes.append(n)
                if dfs(i+1):
                    return True
                nodes.pop()
            return False
        return dfs(0)

    def search(self, word: str) -> bool: # dfs iterative (seems best)
        word += self.term
        N = len(word)
        if not N: return False
        stack = [(0, self.root)]
        while stack:
            i, node = stack.pop()
            if i==N: return True
            c = word[i]
            if c in node:
                stack.append((i+1, node[c]))
            elif c=='.':
                for nxt_n in node.values():
                    stack.append((i+1, nxt_n))
        return False

#["WordDictionary","addWord","addWord","addWord","search","search","search","search"]

wd = WordDictionary()
wd.addWord("bad")
wd.addWord("dad")
wd.addWord("mad")
print(wd.search("pad")) #// return False
print(wd.search("bad")) #// return True
print(wd.search(".ad")) #// return True
print(wd.search("b..")) #// return True

# w[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
# Output [null,null,null,null,false,true,true,true]
