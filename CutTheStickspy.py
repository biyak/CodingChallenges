#Author: Biya Kazmi


def cutSticks(lengths): #lengths is an integer array
    lengthArray = [len(lengths)]
    lengthOfList = len(lengths)
    minimum = min(lengths)
    
    while lengthOfList > 0:
        lengths = recursiveCut(lengths, minimum) #getting rid of minimum
        lengthOfList = len(lengths) 

        
def recursiveCut(lengths, minimum):
        returnOutput = len(lengths)
        minimum = min(lengths) # Get the minimum value from lengths.

        for i in lengths:
            if i == minimum: lengths.remove(i)
        for i in lengths:
            if i == 0: lengths.remove(i)

        print(lengths)

        #Subtract minimum from list
        for i in range(0,len(lengths)):
            a = lengths[i] - 1
            lengths[i] = a
            
        return lengths

array = [1,2,3,1,1,2,3,1,2,2]

CutTheSticks(array)
