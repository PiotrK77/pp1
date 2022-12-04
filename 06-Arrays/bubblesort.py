
def bubbleSort(array):

    length = len(array)

    swapped = False

    for i in range(length):

        for j in range(0, length - i - 1):

            if array[j] > array[j + 1]:
                swapped = True
                array[j], array[j + 1] = array[j + 1], array[j]
            
        if not swapped:
            return





arr = [4, 78, 1, 5, 7, 5, 3, 2]
bubbleSort(arr)
print(arr)
        


