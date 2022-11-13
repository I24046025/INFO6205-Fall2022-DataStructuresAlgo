from collections import Counter

def sortedArray(arr, val):
    output = []

    for k in val:
        i = 0
        for j in arr:
            if k == j:
                output.append(i)
                break
            
            # if cannot find it in the original given arr
            if(i==len(arr)-1 and k!=j):
                output.append(-1)
            i+=1
    return output


# test case
arr = [0,0,0,0,0,1,1,1,1,2,2,5,5,5,8,9,10,11]
values = [1,4,5,10]

# run
sortedArray(arr, values)