array = [4,2,8,4,7,9,5]
minmaxArr = [None, None]

def minmax(array):
    for i in array:
        if minmaxArr[1] == None:
            minmaxArr[1] = i
        elif minmaxArr[0] == None and i < minmaxArr[1]:
            minmaxArr[0] = i
        elif i > minmaxArr[1]:
            minmaxArr[1] = i
        elif i < minmaxArr[0]:
            minmaxArr[0] = i
            
minmax(array)
print(minmaxArr)