""" 
This problem was asked by Uber.

Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division? 
"""

import math

numbers = [1, 2, 3, 4, 5]

def list_product(nums: list[int]) -> list[int]:

    products = []
    product = math.prod(nums)

    for num in nums:
        products.append(product // num)

    return products

print(list_product(numbers))

"""
to solve without division, use a suffix and prefix pass to pre-calculate products stored in separate arrays 
"""