def binary_search(search_list, value):
    path_to_target = []
    low = 0
    high = len(search_list) - 1
    
    while low <= high:
        mid = (low + high) // 2
        value_at_middle = search_list[mid]
        path_to_target.append(value_at_middle)
        
        if value == value_at_middle:
            return f"{path_to_target}\n\nValue found at index {mid}"
        elif value > value_at_middle:
            low = mid + 1
        else:
            high = mid - 1
    
    return [], "Value not found"

numbers = list(range(1000001))
print(binary_search(numbers, 656340))
