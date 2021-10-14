def search(unordered_list, term):  
    unordered_list_size = len(unordered_list)  
    for i in range(unordered_list_size):  
        if term == unordered_list[i]:  
            return i  
    return None  
  
list = [60, 1, 88, 10, 11, 100]

print(search(list, 10))

print(search(list, 103))
  
