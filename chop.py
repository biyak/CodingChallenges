#CodeKatas Chop algorithm
#Takes an integer search target and a sorted array of integers.
#It should return the integer index of the target in the array, or
#-1 if the target is not in the array.

def chop(find, list):
    if len(list) == 0:
        return -1
    else:
        mid = len(list)//2
        if list[mid] == find:
            return mid
        else:
            if list[mid] > find:
                

print(chop(2,[2]))
