#Problem no: 997
#Problem name: Find the Town Judge


#time  :O(E)

#space :O(N)

#Code  :


def findJudge(self, N: int, trust: List[List[int]]) -> int:

    if len(trust) < N - 1:
        return -1

    trust_scores = [0] * (N + 1)

    for a, b in trust:
        trust_scores[a] -= 1
        trust_scores[b] += 1
    
    for i, score in enumerate(trust_scores[1:], 1):
        if score == N - 1:
            return i
    return -1
