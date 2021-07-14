""" 
Daily Coding Problem #2
This problem was asked by Uber.

Given an array of integers, return a new array such that each
element at index i of the new array is the product of all the
numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected 
output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], 
the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?
"""

# Atemmpt to not use division. Complexity: O(N^2) time, O(N) space (for the solution)
def get_products(lst):
    prods = []
    for i, val in enumerate(lst):
        print("Index " + str(i) + ", value=" + str(val))
        prod = 1
        for j, num in enumerate(lst):
            if j != i:
                prod *= num
        prods.append(prod)
    return prods

lst = [1, 2, 3, 4, 5]
prods = get_products(lst)
for prod in prods:
    print("Product: " + str(prod))
