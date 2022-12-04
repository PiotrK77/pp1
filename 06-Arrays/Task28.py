array1 = [1,0,9,4,6]
array2 = [6,8,3,1,0,5,7]

def median(array):
    if len(array) % 2 == 1:
        for i in array:
            bigger = 0
            smaller = 0
            for j in array:
                if j > i:
                    bigger += 1
                elif j < i:
                    smaller +=1
            if smaller == bigger:
                print(i)
    if len(array) % 2 == 0:
        centerNumber1 = None
        centerNumber2 = None
        for i in array:
            bigger = 0
            smaller = 0
            for j in array:
                if j > i:
                    bigger += 1
                elif j < i:
                    smaller +=1
            if smaller == bigger - 1 or smaller - 1 == bigger:
                if centerNumber1 == None:
                    centerNumber1 = i
                elif centerNumber2 == None:
                    centerNumber2 = i
                if centerNumber1 != None and centerNumber2 != None:
                    print((centerNumber1 + centerNumber2) / 2)

median(array1)