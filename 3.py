"""
This problem was asked by Google.

Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.

For example, given the following Node class

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

The following test should pass:

node = Node('root', Node('left', Node('left.left')), Node('right'))
            val = 'root'    left = Node('left", Node('left.left'))  right = Node('right)
                                    val = 'left' left = Node('left.left')
                                                        val = 'left.left'

assert deserialize(serialize(node)).left.left.val == 'left.left' 
"""

from dataclasses import dataclass
from typing import Optional

@dataclass
class Node:
    val: str
    left: Optional['Node'] = None
    right: Optional['Node'] = None

    def has_child(self):
        if self.left or self.right != None:
            return True

def insert(root: Node, s: str):
    if root.left == None:
        root.left = Node(s)
    elif root.right == None:
        root.right = Node(s)
    elif root.right != None:
        left = root.left
        insert(left, s)
    elif root.left != None:
        right = root.right
        insert(right, s)

def serialize(root: Node) -> str:
    result = ""
    return result

def deserialize(s: str) -> Node:

    root = Node(s[0])
    for char in s[1:]:
        insert(root, char)
    return root


tree = deserialize("a super long sentence")
print(tree)
