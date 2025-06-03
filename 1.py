""" This problem was recently asked by Google.

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass? """

import random

numbers = random.sample(range(1, 10), 5)
k = random.randint(1, 20)

def any_sum(numbers: list[int], k: int) -> bool:

    complements = set()

    for num in numbers:
        complement = k - num
        if complement in complements:
            print(f"complement found in set: {complement}, current value: {num}")
            return True
        else:
            complements.add(num)

    return False

print(k)
print(numbers)
print(any_sum(numbers, k))