class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        N = len(A)/2
        
        dic = {}
        for i in A:
            if i not in dic:
                dic[i] = 1
            else:
                dic [i] = dic[i] + 1
                if dic[i] == N:
                    return i
