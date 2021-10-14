def search_ordered(ordered_list, term):  
    ordered_list_size = len(ordered_list)  
    for i in range(ordered_list_size):  
        if term == ordered_list[i]:  
            return i  
        elif ordered_list[i] > term:  
            return None  
    return None  
  
list1 = [1, 3, 6, 11, 88, 100, 110, 150]

print(search_ordered(list, 11))

print(search_ordered(list, 101))
