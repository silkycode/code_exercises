"""
This problem was asked by Amazon.
Given a N by M matrix of numbers, print out the matrix in a clockwise spiral.
For example, given the following matrix:

[[1,  2,  3,  4,  5],
 [6,  7,  8,  9,  10],
 [11, 12, 13, 14, 15],
 [16, 17, 18, 19, 20]]
You should print out the following:

1
2
3
4
5
10
15
20
19
18
17
16
11
6
7
8
9
14
13
12 
"""

from typing import List

matrix_1 = [[1,  2,  3,  4,  5],
            [6,  7,  8,  9,  10],
            [11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20]]

matrix_2 = [[ 1,  2,  3,  4],
            [12, 13, 14,  5],
            [11, 16, 15,  6],
            [10,  9,  8,  7]]

def clockwise_print(matrix: List[List[int]]):

    top = 0
    bottom = len(matrix) - 1
    left = 0
    right = len(matrix[0]) - 1

    # don't let boundaries cross over
    while top <= bottom and left <= right:

        # left to right, push top down
        for col in range(left, right + 1):
            print(matrix[top][col])
        top += 1

        # top to bottom, push right left
        for row in range(top, bottom + 1):
            print(matrix[row][right])
        right -= 1

        # right to left, push bottom up
        if top <= bottom:
            for col in range(right, left - 1, -1):
                print(matrix[bottom][col])
            bottom -= 1

        # bottom to top, push left right
        if left <= right:
            for row in range(bottom, top - 1, -1):   
                print(matrix[row][left])   
            left += 1  

clockwise_print(matrix_1)
clockwise_print(matrix_2)

# index nightmare, maze traversal
# understanding constraints of movement for iteration over a data structure