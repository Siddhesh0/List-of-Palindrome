                                   # PALINDROMIFY THE LIST


# You have given the list which contain some numbers. you have to print a list of next palindrome
# only if the number is grater than 10 otherwise you will print that number.

# INPUT:
# [1, 5, 44, 58]

# OUTPUT:
# [1, 5, 45, 59]


"""
Author: Siddhesh
Date: 21 Nov 2021
Purpose: Practice problem
"""


def next_palindrome(n):
    n = n+1
    while not is_palindrome(n):
        n +=1
    return n

def is_palindrome(n):
    return str(n) == str(n)[::-1]

if __name__ == '__main__':
    size = int(input("Enter the size of your list\n"))
    num_list = []

    for i in range(size):
        num_list.append(int(input("Enter a number for a list\n")))
    print(f"You have entered {num_list}")

    print(f"The Output List is:{[num_list[i] if num_list[i] < 10 else next_palindrome(num_list[i]) for i in range(size)]}")
    # new_list = []
    # for element in num_list:
    #     if element > 10:
    #         n = next_palindrome(element)
    #         new_list.append(n)
    #     else:
    #         new_list.append(element)
    # print(f"The Output List is:{new_list}")
