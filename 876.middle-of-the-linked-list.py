#
# @lc app=leetcode id=876 lang=python3
#
# [876] Middle of the Linked List
#
# https://leetcode.com/problems/middle-of-the-linked-list/description/
#
# algorithms
# Easy (63.20%)
# Total Accepted:    47.4K
# Total Submissions: 74.9K
# Testcase Example:  '[1,2,3,4,5]'
#
# Given a non-empty, singly linked list with head node head, return a middle
# node of linked list.
# 
# If there are two middle nodes, return the second middle node.
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: [1,2,3,4,5]
# Output: Node 3 from this list (Serialization: [3,4,5])
# The returned node has value 3.  (The judge's serialization of this node is
# [3,4,5]).
# Note that we returned a ListNode object ans, such that:
# ans.val = 3, ans.next.val = 4, ans.next.next.val = 5, and ans.next.next.next
# = NULL.
# 
# 
# 
# Example 2:
# 
# 
# Input: [1,2,3,4,5,6]
# Output: Node 4 from this list (Serialization: [4,5,6])
# Since the list has two middle nodes with values 3 and 4, we return the second
# one.
# 
# 
# 
# 
# Note:
# 
# 
# The number of nodes in the given list will be between 1 and 100.
# 
# 
# 
# 
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#Two pointers

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            #the speed of fast point is faster than slow point twice
        
        return slow


#[1,2,3,4]  length is even slow = 3 fast = 4
#[1,2,3,4,5]  length is odd slow = 3 fast = 5

#run the whole linked list and obtain the length of the list

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        #[1,2,3,4]
        list_val = []
        cnt = 1
        while head.next != None:
            list_val += [head.val]
            head = head.next
            cnt +=1
        list_val += [head.val]
        index = cnt // 2
        res=[]
        for i in range(index,len(list_val)):
            res += [list_val[i]]
            
        return res