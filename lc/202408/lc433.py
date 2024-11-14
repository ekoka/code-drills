"""
LC 433: Minimum Genetic Mutation

A gene string can be represented by an 8-character long string, with choices from 'A', 'C', 'G', and 'T'.

Suppose we need to investigate a mutation from a gene string `startGene` to a gene string `endGene` where one mutation is defined as one single character changed in the gene string.

    For example, "AACCGGTT" --> "AACCGGTA" is one mutation.

There is also a gene bank `bank` that records all the valid gene mutations. A gene must be in `bank` to make it a valid gene string.

Given the two gene strings `startGene` and `endGene` and the gene bank `bank`, return the minimum number of mutations needed to mutate from `startGene` to `endGene`. If there is no such a mutation, return `-1`.

Note that the starting point is assumed to be valid, so it might not be included in the bank.

Example 1:

Input: startGene = "AACCGGTT", endGene = "AACCGGTA", bank = ["AACCGGTA"]
Output: 1

Example 2:

Input: startGene = "AACCGGTT", endGene = "AAACGGTA", bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]
Output: 2

Constraints:

    0 <= bank.length <= 10
    startGene.length == endGene.length == bank[i].length == 8
    startGene, endGene, and bank[i] consist of only the characters ['A', 'C', 'G', 'T'].
"""
# 46
def minmutation(start, end, bank):
    q = [start]
    discovered = {start:0}
    while q:
        new_q = []
        while q:
            g = q.pop()
            for m in valid_mutations(g, bank, discovered):
                if m==end: return discovered[g] + 1
                discovered[m] = discovered[g] + 1
                new_q.append(m)
        q = new_q
    return -1

def valid_mutations(gene, bank, discovered):
    rv = []
    for mutation in bank:
        if mutation in discovered: continue
        diff = 0
        for i in range(8):
            if mutation[i]!=gene[i]:
                diff += 1
                if diff>1: break
        if diff==1:
            rv.append(mutation)
    return rv

def minmutation(start, end, bank):
    # more optimal
    q = [(start, 0)]
    bank = set(bank)
    while q:
        new_q = []
        while q:
            g, mc = q.pop() # gene, mutation_count
            for m in list(bank):
                diff = 0
                for i in range(8):
                    if m[i]!=g[i]:
                        diff += 1
                        if diff>1: break
                if diff!=1: continue
                bank.remove(m)
                if m==end: return mc+1
                new_q.append((m, mc+1))
        q = new_q
    return -1

from collections import deque
def minmutation(start, end, bank):
    # slightly less optimal because of deque
    q = deque([(start, 0)])
    bank = set(bank)
    while q:
        g, mc = q.popleft() # gene, mutation_count
        for m in list(bank):
            diff = 0
            for i in range(8):
                if m[i]!=g[i]:
                    diff += 1
                    if diff>1: break
            if diff!=1: continue
            bank.remove(m)
            if m==end: return mc+1
            q.append((m, mc+1))
    return -1

def minmutation(start, end, bank):
    q = [(start, 0)]
    while q:
        new_q = []
        while q:
            g, mc = q.pop() # gene, mutation_count
            remaining = []
            for m in bank:
                diff = 0
                for i in range(8):
                    if m[i]!=g[i]:
                        diff += 1
                        if diff>1: break
                if diff!=1:
                    remaining.append(m)
                    continue
                if m==end: return mc+1
                new_q.append((m, mc+1))
            bank = remaining
        q = new_q
    return -1

def minmutation(startGene, endGene, bank):
    def valid_mutation(g1, g2):
        n = len(g1)
        if n!=len(g2): return False
        for i in range(n):
            if g1[i]!=g2[i]:
                n -= 1
                if n < len(g1)-1: 
                    return False
        return True
    stack = [startGene]
    discovered = {startGene}
    mutations = 0
    while stack:
        nxt_stack = []
        while stack:
            g = stack.pop()
            if g==endGene:
                return mutations
            for m in bank:
                if m in discovered: continue
                if not valid_mutation(g,m): continue
                discovered.add(m)
                nxt_stack.append(m)
        stack = nxt_stack
        mutations += 1
    return -1

startGene = "AACCGGTT"
endGene = "AACCGGTA"
bank = ["AACCGGTA"]
print(minmutation(startGene, endGene, bank))
# Output: 1

startGene = "AACCGGTT"
endGene = "AAACGGTA"
bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]
print(minmutation(startGene, endGene, bank))
#Output: 2
