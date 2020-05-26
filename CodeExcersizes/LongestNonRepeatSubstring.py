
def longestNonRepeatSub(s):
    if len(s) == 1:
            return 1
    visited = {}
    maxlen = 0
    letter = 0
    
    for start in range(len(s)):
        for stop in range(start+1, len(s)+1):
            #get a substring
            checkRepeat = {}
            substring = s[start:stop]
            print("substring: " + substring)
            #print(visited)
            if substring in visited or len(substring) <= maxlen:
#                print("uh")
                continue
            else: #Has not been visited before
                visited[substring] = 1
                #print(maxlen)
                for i in substring: #for every letter in substring
                    if i not in checkRepeat: #check for repeated letter in this substring                                           
                        letter = letter + 1 #non repeated letters
#                        print(i)
                        
                        checkRepeat[i] = 1; #no repeats so far
#                        print(checkRepeat)
                    else: #found a repeat.
                        if letter > maxlen:
                            maxlen = letter
                            letter = 0
                            checkRepeat = {}
                            break
                        else:
                            letter = 0
                            checkRepeat = {}
                            break
    print(maxlen)
longestNonRepeatSub("au")
