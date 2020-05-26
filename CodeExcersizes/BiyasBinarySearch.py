#Takes a list l and the item to find f 
def binarySearch(l, f):
  print(l)
  #How long is the list
  n = len(l)
  #Base case for recursion
  if n is 0:
    return False
  else:
    #Cut the list in half
    mid = (n//2) #Is the index for the middle
    #If it's the middle character
    if f == l[mid]:
      return True
    else:
      #If the number you're looking for is less than the middle number 
      if f < l[mid]:
        newL = l[:mid]
        #Take all the numbers from the beginning of the list until the middle (excluding the middle)
        #BinarySearch() again with new list we've created and same value we're looking for (duh)
        return binarySearch(newL, f)
      #If the number you're looking for is bigger than the middle number 
      else:# f > l[mid]:
        #Take all the numbers after the middle number until the end
        newL = l[mid+1:]
        #BinarySearch() again
        return binarySearch(newL, f)



theList = [1,2,3,4,5,10,11,20,34,122]
print(binarySearch(theList, 14))

