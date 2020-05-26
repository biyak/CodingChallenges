'''
Author Biya Kazmi

rotating a list but k amount of steps to the right.
ie if a list [1,2,3,4] is rotated two steps to the right, every element moves
two indices.
ans: [3,4,1,2]
'''

def rotate(list, step):
    #Takes a list of numbers and how many steps you wish to move it.
    
    length = len(list)
    #length of the list

    newList = [0] * length
    #Want a new list that is going to be our rotated list. 

    newIndex = 0
    #For when we need to rotate our list with the elements that would
    #normally go out of bounds
    
    for index in range(length - (step)):
        #For the first part of the list that can just be moved over
        newList[index+step] = list[index]
    
    for index in range(length - step, length):
        #The second part of the list will go out of bounds if moved over
        newList[newIndex] = list[index]
        #So we start putting the numbers into the beginning of the list
        #keep going until we get to the already rotated numbers. 
        newIndex = newIndex+1

    return newList
    #Ta da!


x = [1,2,3,4,5,6,7]; rotate(x, 3); 
