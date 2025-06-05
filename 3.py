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

def serialize(root: Node) -> str:
    result = ""
    return result

def deserialize(s: str) -> Node:
    return Node(val="b")

