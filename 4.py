""" This problem was asked by Stripe.

Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place. """

input = [3, 4, -1, 1] 
input_2 = [1, 2, 0]

# naive approach, using sorting (actually breaks the constraints, first attempt)
def find_missing_int_naive(nums: list[int]) -> int:
    nums.sort()
    for i in range(len(nums) - 1):
        if nums[i] >= 0:
            # because of sort order, can assume ints are in sequence
            expected = nums[i] + 1
            next = nums[i + 1]

            # if next int in sequence is greater than expected, a gap exists
            if next > expected:
                return expected

    # if we reach the end of the sequence without finding a gap, we can assume a perfect sequence
    # so, first missing int is the one immediately after the greatest int in the sequence
    return nums[-1] + 1

# better approach, using in-place index swapping
def find_missing_int(nums: list[int]):
    for i in range(len(nums)):
        # we know we only care about ints that are 1 or greater, and also smaller than the total length of the array
        # also, check that the corresponding index does not hold its corresponding value, i.e. nums[3] != 4
        while (1 <= nums[i] <= len(nums) and nums[nums[i] - 1] != nums[i]):
            correct_index = nums[i] - 1
            nums[i], nums[correct_index] = nums[correct_index], nums[i]                  

    # second walk, just find the first index that doesn't hold its corresponding value, this is the gap
    for i in range(len(nums)):
        if (nums[i] != i + 1):
            return i + 1

print(find_missing_int(input))
print(find_missing_int(input_2))

# poor man's hash table, use the perks of an array's sequential properties to find gaps in integer sequences
# two for loops -> 2n, while loop can never exceed n swaps, o(1) space, o(n) time 

# DONE