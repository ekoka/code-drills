"""
LC 017: Letter Combinations of a Phone Number

Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Example 2:

Input: digits = ""
Output: []

Example 3:

Input: digits = "2"
Output: ["a","b","c"]

Constraints:

    0 <= digits.length <= 4
    digits[i] is a digit in the range ['2', '9'].

"""
# 59
mapping = {
    "2": "abc", "3": "def",
    "4": "ghi", "5": "jkl",
    "6": "mno", "7": "pqrs",
    "8": "tuv", "9": "wxyz",
}
def letter_combos(digits):
    # bfs
    if not digits:
        return []
    prefixes = [""]
    for d in digits:
        new_prefixes = []
        for char in mapping[d]:
            for p in prefixes:
                new_prefixes.append("".join((p, char)))
        prefixes = new_prefixes
    return prefixes

def letter_combos(digits):
    # backtracking
    if not digits: return []
    N = len(digits)
    rv = []
    combo = []
    def combinations(start, record):
        if record:
            rv.append("".join(combo))
            return
        if start==N:
            return
        record = len(combo)==N-1
        for i in range(start, N):
            for letter in mapping[digits[i]]:
                combo.append(letter)
                combinations(i+1, record)
                combo.pop()
    combinations(0, False)
    return rv

def letter_combos(digits):
    if not digits: return []
    N = len(digits)
    rv = []
    combo = [""]
    def combinations(start):
        if start==N: return
        rec = len(combo[0])==N-1
        for i in range(start, N):
            for letter in mapping[digits[i]]:
                combo[0] += letter
                if rec:
                    rv.append(combo[0])
                else:
                    combinations(i+1)
                combo[0] = combo[0][:-1]
    combinations(0)
    return rv

def letter_combos(digits):
    if not digits: return []
    N = len(digits)
    rv = []
    combo = [""]
    def record(_):
        rv.append(combo[0])
    def combinations(start):
        if start==N: return
        fnc = record if len(combo[0])==N-1 else combinations
        for i in range(start, N):
            for letter in mapping[digits[i]]:
                combo[0] += letter
                fnc(i+1)
                combo[0] = combo[0][:-1]
    combinations(0)
    return rv

digits = "23"
print(letter_combos(digits))
#Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

digits = ""
print(letter_combos(digits))
# Output: []

digits = "2"
# Output: ["a","b","c"]
print(letter_combos(digits))
