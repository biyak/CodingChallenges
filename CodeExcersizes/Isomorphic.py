'''
Isomorphic words
Words are isomorphic if you can replace all the occurances of the same letter
with another letter.
For example, you replace all the a's with d's and so on.
The letter does not HAVE to be replaced in the new string, but if it is replaced
in one instance in the new string, it has to replace all the instances.
The order of the occurance matters, where ever a shows up in the first word, d
must show up in the same place

We're going to hash map the characters so every time an a shows up,
the hash knows a d should be in the other words

'''

def iso(s, t):
    # s and t are the two strings being compared

    # if the length isnt the same they already cannot be isomorphic
    if len(s) != len(t):
        return False

    hashMap = {}

    #for each character in string s and t 
    for i in range(len(s)):
        char1 = s[i]
        char2 = t[i]

        if char1 in hashMap:
            if hashMap.get(char1) != char2:
                return False
        else:
            if char2 in hashMap:
                return False
            hashMap[char1] = char2

    print(hashMap)       
        

iso("hellos", "bagger")

