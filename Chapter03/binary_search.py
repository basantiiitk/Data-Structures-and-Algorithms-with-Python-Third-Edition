def binary_search(arr, start, end, key):
    while start <= end:  
        mid = int(start + int((end - start)/2))
        if arr[mid] == key:  
            return mid  
        elif arr[mid] < key:  
            start = mid + 1  
        else:  
            end = mid - 1  
    return -1  



arr = [ 2, 3, 4, 2, 10, 40] 
x = 10 
result = binary_search(arr, 0, len(arr)-1, x)  
print(result) 
