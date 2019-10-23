

# Given a list, find a pair of values that add to 10 in linear time.

def findten(list):
    dicky = {}

    for number in list:
        toFind = 10 - number
        if toFind in dicky:
            #print("(" + number + ", " + toFind + ")" )
            print(toFind)
            print(number)
            return ''
        else: dicky[number] = 1
    print( 'No pairs add to 10')

#findten([1,2,3,4,3,2,5,6])

def stringiterator(s):
    for letter in s:
        print(letter)

def anagramchecker(s1, s2):
    if (len(s1) != len(s2)):
        print("Not an anagram")
        return ""
    dic = {}
    for i in s1:
        if i in dic:
            dic[i] = dic[i] + 1
        else: dic[i] = 1

    for i in s2:
        if i in dic:
            if dic[i] > 0:
                dic[i] = dic[i] -1
            else: print("Not an anagram"); return ""
        print("Anagrams!!")
        return ""
        
anagramchecker("abahgyta", "baatgayh")
