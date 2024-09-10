#URL : https://leetcode.com/problems/reverse-linked-list/description/
#[Easy] [206] 
#Title: [Reverse Linked List]
#Author: Kartik Bhatnagar
#Date : 2024-09-10 (YYYY-MM-DD)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head) :
        result =ListNode()
        resu = result
        def dfs(hd):
            if hd:
                res = dfs(hd.next) 
                res.next = ListNode(hd.val)
                print(hd.val)    
                return res.next           
                # result.next=ListNode(hd.val)
                # return result.next
            else:
                return resu
        dfs(head)
        return resu.next
        
if __name__ == "__main__":
    s=Solution()
