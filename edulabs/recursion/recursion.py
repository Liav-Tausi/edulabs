# Implement a function sum_digits(n) that receives an integer number n and returns the sum of its digits using recursion.

def sum_digits(n):
    if n < 10:
        return n
    return n % 10 + sum_digits(n // 10)


#
# print(sum_digits(111))


# Implement a function harmonic_sum(n) that receives an integer number n and returns the sum of its digits using recursion. Harmonic sum of 5 is:
# 1 + ½ +⅓ +¼ +⅕

def harmonic_sum(n):
    if n == 1:
        return 1
    else:
        return 1 / n + harmonic_sum(n - 1)


# print(harmonic_sum(5))


# Write a recursive function that receives a number n and prints two triangles with basis of n stars as follows (n=5):

def two_triangles(n):
    if n == 1:
        return two_triangles(n + 1)
    print("*\t" * n, )
    return two_triangles(n - 1)


print(two_triangles(5))