# This is week 2

# integers
my_variable = 58
print(my_variable)
brandon = 20000
print(brandon)
print(type(brandon))

# floats
floating_var = (1 + 5) * 5 / 1
print(type(floating_var))


# booleans
# AND statements
print(True and True)  # True
print(True and False)  # False
print(False and True)  # False
print(False and False)  # False
# OR statements
print(True or True)  # True
print(True or False)  # True
print(False or True)  # True
print(False or False)  # False

# Boolean expressions
print(4 > 3)  # True
print(5 < 1)  # False
print(66 == 66) # True


# If statements
some_variable = 8
if (some_variable > 22):
    print(some_variable)
    some_variable += 1  # some_variable = some_variable + 1
    print(some_variable)
elif (some_variable > 9):
    some_variable += 70
    print(some_variable)
else:
    some_variable = 11
    print(some_variable)

# strings
print("Hello Brandon!")
this_str_variable = "Hello Brandon!"
this_str_variable += "What?"
# a random function with strings:
print(this_str_variable.swapcase())
# indexing

# 0 indexing: Get the "H"
print(this_str_variable[0])
# full-length indexing: Get the question mark
total_length = len(this_str_variable)
print(total_length)
print(this_str_variable[total_length - 1])

# substrings
print(this_str_variable[5:total_length - 5])
# other forms of makings substrings
# n until the end
print(this_str_variable[5:])
# begin until n
print(this_str_variable[:5])
# negative indexing
print(this_str_variable[-2])

# lists
sample_list = [4, 3, "some string", 24 * 2, True, False]
print(sample_list)
# indexing
print(sample_list[1])
print(sample_list[-2])
# concatenating
another_list = [22, 44, 00]
print(sample_list + another_list)
# appending
sample_list.append("wow.")
print(sample_list)
sample_list.reverse()
print(sample_list)
# slicing
my_new_list = sample_list[1:4]
print(my_new_list)


# for loops
for number in range(1, 10, 2):
    print(number)
print("-------------------")
for number in range(10):
    print(number)
print("-------------------")
# negative iterations
for number in range(0, -10, -1):
    print(number)
print("-------------------")


# elemental for loops

# the long way (we did in Java):
my_list = [3, 47, 38]
for index in range(len(my_list)):
    my_element = my_list[index]
    print(index, my_element)
print("-------------------")
# the shorter way:
for element in my_list:
    print(element)

# while loop example: print from 1 to 4
print("-------------------")
iter_number = 1
while iter_number <= 4:
    print(iter_number)
    iter_number += 1  # if you remove this, an infinite loop will occur


# functions:
def func_name(para_1, para_2):
    return para_1

def largest_adj_difference(another_list):
    '''
    ([list of ints]) -> int

    Returns the largest pairwise adjacent difference in the given list

    REQ: another_list must have 2 or more elements

    >>> first_list = [1, 1, 1]
    >>> largest_adj_difference(first_list)
    0
    >>> second_list = [5, 16, 20, 11]
    >>> largest_adj_difference(second_list)
    11
    >>> third_list = [16, 5, 11, 20]
    >>> largest_adj_difference(third_list)
    11
    '''
    # set a varaible to be the highest difference
    highest_difference = 0

    # doing a while loop, we would need an index for a current element
    curr_index = 1
    # at the same time, we want the element before
    chaser = curr_index - 1

    # then we want to iterate through the list to determine what would
    # be the highest difference
    while curr_index < len(another_list):
        # within each iteration, assess the adjacent pairwise elements
        assess = another_list[curr_index] - another_list[chaser]
        # suppose that the assessment is negative
        if assess < 0:
            # then we have to turn this into a positive
            assess = assess * -1
        # check that it is higher than the current highest difference
        if (assess > highest_difference):
            # if it is, then set the highest difference variable to the current
            highest_difference = assess
        # do not go into an infinite while loop
        curr_index += 1
        chaser += 1
    # once completing the iterations, return the highest difference
    return highest_difference

if __name__ == "__main__":
    print("#########################################")
    import doctest
    doctest.testmod()