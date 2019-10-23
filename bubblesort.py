

#bubble sort

def bubblesort():
    arr = [1,2,9,1,4,5,2,5]

    i = 0
    j = 1

    swap = 0

    while (i<len(arr)-1 and j < len(arr) ):
        if (arr[i] > arr[j]):
            more = arr[i]
            less = arr[j]

            arr[i] = less
            arr[j] = more
            swap = 1
            print(str(arr[i]) + ", " + str(arr[j]))
            print(arr)
        else: print(str(arr[i]) + ", " + str(arr[j]) + "\n" + str(arr))
    
        if (swap>0 and i == len(arr) -2 and j == len(arr)-1):
            i = 0
            j = 1
        elif (swap==0 and i == len(arr) -2 and j == len(arr)-1):
            break
        else: i = i+1; j = j+1
        swap = 0
bubblesort()
                       
