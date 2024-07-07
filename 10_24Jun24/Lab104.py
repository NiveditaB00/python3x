# Filter in Python
# The filter() function in Python is a built-in function
# allows you to filter elements in the list, tuple, set.

numbers=[1,2,3,4,5,6,7,8,9,10]
#Filter on the above ->even
#new_list_even[2,4,6,8,10]

def is_even(n):
    return n%2==0


def is_greater_5(n):
    return n>5

new_number_even = filter(is_even, numbers)
print(list(new_number_even))


new_number_five = filter(is_greater_5, numbers)
print(list(new_number_five))