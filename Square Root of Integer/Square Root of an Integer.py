def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    if number == 0 or number == 1:
    	return number

    first = number
    last = 0

    while last <= first:
    	mid_val = (last + first) // 2

    	if mid_val ** 2 == number or mid_val ** 2 <= number < (mid_val + 1) ** 2:
    		return mid_val

    	elif mid_val ** 2 > number:
    		first = mid_val
    	else:
    		last = mid_val

# All the tests below are supposed to pass 
print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")
print("Pass" if (1 == sqrt(2)) else "Fail")
print("Pass" if (5 == sqrt(27)) else "Fail")

# Edge Cases
print ("Pass" if  (6871 == sqrt(47210641)) else "Fail")
print ("Pass" if  (9999 == sqrt(99999999)) else "Fail")
print ("Pass" if  (None == sqrt(-1)) else "Fail")
