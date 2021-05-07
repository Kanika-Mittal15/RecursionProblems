def product(arr):
    if len(arr)==0:
        return 0
    elif len(arr)==1:
        return arr[0]
    else:
        return arr[len(arr)-1]*product(arr[:len(arr)-1])



# number of elemetns as input
n = int(input("Enter number of elements : "))

arr = list(map(int,input().split()))[:n]
print(product(arr))