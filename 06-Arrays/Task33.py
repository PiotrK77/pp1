mainArray = [1, 2, 3, 4, 6, 7, 8, 9]
subsetArray = [2, 5]
subset = False



def ifSubset(subsetArray, mainArray):

    for i in subsetArray:

        length = len(mainArray)
        subset = False

        for j in mainArray:

            length -= 1

            if i == j:
                subset = True
            
            if length == 0 and subset == False:
                return False
    return True
            







print(ifSubset(subsetArray, mainArray))
