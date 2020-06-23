"""

link: https://leetcode-cn.com/problems/flatten-a-multilevel-doubly-linked-list

problem: 展开多级链表

solution: 深度优先递归拼接

"""
"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        k = head
        while k:
            if k.child is None:
                k = k.next
                continue
            t = self.flatten(k.child)
            tf = t
            while tf.next: tf = tf.next
            k.child = None
            if k.next:
                k.next.prev = tf
                tf.next = k.next
            t.prev = k
            k.next = t
            k = tf.next
        return head

