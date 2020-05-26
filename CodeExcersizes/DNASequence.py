class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        #seperate string into all 10 letter sequence
        #add to dictionary
        
        d = {}
        answer = []
        
        for i in range(0, len(s)-9):
            substring = s[i:i+10]
            print(substring)
            if substring not in d:
                d[substring] = 1
            else:
                d[substring] = d[substring]+1
                if d[substring] == 2:
                    answer.append(substring)
        return answer
        
