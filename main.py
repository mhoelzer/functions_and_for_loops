"""takes 2 arguments, and returns the sum"""


def add(num1, num2):
    return num1 + num2


"""
takes 2 arguments, and returns the product
no builtin arithmetic operators or functions
need to use the add function from above
"""


def multiply(num1, num2):
    product = 0
    for _ in range(num2):  # using range(0, num2) also works here
        product = add(product, num1)
    return product


"""
takes a number and raises it to w/e power
exponent stuff
no builtin arithmetic operators or functions
need to use the add/multiply functions from above
"""


def power(num_to_raise, nth_power):
    product = 1
    for _ in range(nth_power):
        product = multiply(product, num_to_raise)
    return product


"""
takes a number and gets its factorial
no builtin arithmetic operators or functions
need to use functions from above
"""


def factorial(factorial_num):
    # FOR
    running_num = 1
    for factorial_num_start in range(1, factorial_num + 1):
        # need the + 1 b/c of range will not include 4
        # fns starts at 1 because of the range/factorials dont include 0
        running_num = multiply(running_num, factorial_num_start)
    return running_num

    # WHILE
    # running_num = 1
    # factorial_num_start = 1
    # while factorial_num_start <= factorial_num:
    #     running_num = multiply(running_num, factorial_num_start)
    #     factorial_num_start += 1
    # return running_num


"""
takes an argument and returns the nth of it in fibonacci
no builtin arithmetic operators or functions
need to use functions from above
"""


def fibonacci(num):
    # WAY 1
    # fibonacci_list = []
    # for _ in range(num):
    #     if not fibonacci_list:  # aka if fibonacci_list == []
    #         fibonacci_list.append(0)
    #     elif fibonacci_list == [0]:
    #         fibonacci_list.append(1)
    #     else:
    #         fibonacci_list.append(add(fibonacci_list[-1], fibonacci_list[-2]))
    # return fibonacci_list[-1]

    # WAY 2
    fibonacci_list = [0, 1]  # baseline/starter nums; simplifies above
    for _ in range(num - 2):  # need the -2 b/c have the 2 spots taken in f_l
        fibonacci_list.append(add(fibonacci_list[-1], fibonacci_list[-2]))
        # this adds the last 2 numbers in the f_l to make next num
    return fibonacci_list[-1]  # want the specific number


print(add(2, 4))
print(multiply(6, 8))
print(power(2, 8))
print(factorial(4))
print(fibonacci(8))
