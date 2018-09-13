# def factorial(n):
#     def recurse(n,product):
#         if n==1:
#             return product
#             print(n)
#         else:
#             return recurse(n-1,n*product)
#     recurse(n,1)


def factorial(n,product=1):
    if n==1:
        return product
    else:
        return factorial(n-1,n*product)

print(factorial(5))

import os

os.path.sep