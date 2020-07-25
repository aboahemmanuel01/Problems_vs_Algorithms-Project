def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    if not ints:
        return

    answer = [-float('inf'), float('inf')]
    for num in ints:
        if num > answer[0]:
            answer[0] = num
        if num < answer[1]:
            answer[1] = num
    return (answer[1], answer[0])


## Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")
print("Pass" if (None is get_min_max([])) else "Fail") 
print("Pass" if ((0, 0) == get_min_max([0])) else "Fail")  
print("Pass" if ((0, 9) == get_min_max([0])) else "Fail")  
