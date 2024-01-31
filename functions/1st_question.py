"""
Create and try out functions that would:
1.1 return the sum of three passed numbers.
1.2 Return the sum of all numbers in a passed list.
1.3 Print the highest number from a passed list.
1.4 Would return a passed string backwards.
1.5 Would return a list only with non-repeating items from a passed list.
1.6 Would return if a passed number is a prime number.
"""


#  1.1 question
def sum_three_num(num1, num2, num3):
    return num1 + num2 + num3


print(sum_three_num(1, 1, 1))


#  1.2 question
def sum_from_list(lst):
    sumz = 0
    for x in lst:
        sumz += x
    return sumz


listt = [1, 1, 1]
print(sum_from_list(listt))


#  1.3 question
def return_highest(*args):
    lst = []
    for x in args:
        lst.append(x)
    lst.sort()
    print(lst[-1])


return_highest(1, 2, 5, 6, 25, 69)


#  1.4 question
def reverse_string(string: str) -> str:
    return string[::-1]


print(reverse_string("Donezo"))


#  1.5 question
def return_non_repeat(string: list):
    return list(set(string))


print(return_non_repeat([1, 2, 3, 3, 3]))


#  1.6 question
def is_prime(num):

    flag = False

    if num == 1:
        print(num, "is not a prime number.")
    elif num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                flag = True
                break
        if flag:
            print(num, "is not a prime number.")
        else:
            print(num, "is a prime number.")


is_prime(2)
