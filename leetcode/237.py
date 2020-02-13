"""

link: https://leetcode.com/problems/delete-node-in-a-linked-list

problem: 删除链表中的一个节点，不给表头只给该节点

solution: 修改指定节点到其下一跳

"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        node.val = node.next.val
        node.next = node.next.next