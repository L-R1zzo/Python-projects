def selection_sort(integers):
    if len(integers) <= 1:
        return integers

    n = len(integers)
    for index in range(n):
        minimum_index = index

        for check_index in range(index+1, n):
            if integers[minimum_index] > integers[check_index]:
                minimum_index = check_index

        if minimum_index != index:
            integers[index], integers[minimum_index] = integers[minimum_index], integers[index]

            
    return integers
