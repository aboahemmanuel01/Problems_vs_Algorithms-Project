def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    len_of_input_list = len(input_list)
    first = len_of_input_list
    last = 0
    pivot = 0

    while last <= first:
        pivot = (last + first) // 2

        if input_list[0] < input_list[len_of_input_list - 1] or pivot == len_of_input_list - 1:
            pivot = 0
            break

        if input_list[pivot -1] > input_list[pivot]:
            break

        elif input_list[0] < input_list[pivot]:
            last = pivot

        elif input_list[0] > input_list[pivot]:
            first = pivot

    if input_list[pivot] <= number <= input_list[len_of_input_list - 1]:
        last = pivot
        first = len_of_input_list

    else:
        first = pivot
        last = 0

    while last <= first:
        pivot = (last + first) // 2

        if input_list[pivot] == number:
            return pivot

        elif input_list[pivot] < number:
            last = pivot + 1
        else:
            first = pivot - 1
    return -1



def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[1, 2, 3, 4, 6, 7, 8], 10])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])


# Edge cases
test_function([[8], -1])
test_function([[1], 1])
test_function([[1], 0])