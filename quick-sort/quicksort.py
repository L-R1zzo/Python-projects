def quick_sort(integers):

    if len(integers) <= 1:
        return integers

    main_index = 0
    pivot = integers[0]
    minors = []
    equals = []
    majors = []

    while main_index < len(integers):
        if pivot > integers[main_index]:
            minors.append(integers[main_index])
        elif pivot < integers[main_index]:
            majors.append(integers[main_index])
        else:
            equals.append(integers[main_index])
        main_index += 1

    minors = quick_sort(minors)
    majors = quick_sort(majors)
    sorted_list = minors + equals + majors

    return sorted_list

print(quick_sort([20, 3, 14, 1, 5]))























