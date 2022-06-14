array = [4,8,3,9,5,7,0,1,2]

def linear_search(array1,key):
    for i in range(0,len(array1)):
        if array1[i] == key:
            break

    print("The element ",key,"was found in position",i)


linear_search(array,4)