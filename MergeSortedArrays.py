def merge(nums1, nums2):
    """
    :type nums1: List[int]
    :type m: int
    :type nums2: List[int]
    :type n: int
    :rtype: None Do not return anything, modify nums1 in-place instead.
    """
    #Create aux array of merged lists
    
    #Go through both lists and compare elements, adding to aux
    
    #Use a while loop so you can keep track of index of nums1 and nums2
    
    aux = []
    
    i = j = 0
    
    while i != len(nums1) and j != len(nums2):
        a = nums1[i]    #just for clarity, we will give them names
        b = nums2[j]

        print(a)
        print(b)
        
        if a == b:
            aux = aux + [a,b]
            i = i + 1
            j = j + 1
            print(aux)
        
        if a > b:
            #If nums1 integer being compared is BIGGER
            #Then it goes after the nums2 integer
            aux = aux + [b]
            j = j + 1
            print(aux)
            
        if a < b:
            aux = aux + [a]
            i = i + 1
            print(aux)
    
    #While loop ended because: i = len or j = len or both
    if i == len(nums1) and j == len(nums2):
        print(aux)
        return aux
            
    if i == len(nums1):
        rest = nums2[j:len(nums2)]
        aux = aux + rest
        print(aux)
        return aux
        
    if j == len(nums2):
        rest = nums1[i:len(nums1)]
        aux = aux + rest
        print(aux)
        return aux

n = [1,3,4,7]

m = [0,3,5]

merge(n, m)

