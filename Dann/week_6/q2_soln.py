# non-stack solution
def is_palindrome(my_str):
    ret = False
    if len(my_str) == 0:
        ret = True
    else:
        while my_str != "" and my_str[0] == my_str[-1]:
            my_str = my_str[1:-1]
        ret = my_str == ""
    return ret

# stack solution
def is_palindrome(my_str):
    my_stk = []
    index = 0
    tot_len = len(my_str)

    while index < (tot_len - 1) / 2:
        my_stk.append(my_str[index])
        index = index + 1

    if tot_len % 2 == 1:
        my_str = my_str[:index] + my_str[index + 1:]

    while my_stk != [] and my_stk[-1] == my_str[index]:
        my_stk.pop(-1)
        index = index + 1

    return my_stk == []
