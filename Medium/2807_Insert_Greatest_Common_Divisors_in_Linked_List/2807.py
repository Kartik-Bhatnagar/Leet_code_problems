#URL : https://leetcode.com/problems/insert-greatest-common-divisors-in-linked-list/description/?envType=daily-question&envId=2024-09-10
#[Medium] [2807] 
#Title: [Insert Greatest Common Divisors in Linked List]
#Author: Kartik Bhatnagar
#Date : 2024-09-10 (YYYY-MM-DD)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def gcd(self,n1,n2):
        #using euclidean alogrithm to find gcd or hcf
        num1 = min(n1,n2)
        num2 = max(n1,n2)
        rem =-1
        while rem !=0:
            rem = num1 % num2
            num1 = num2
            num2 =rem
        return num1
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        result =[]
        res_hd = ListNode()
        hd = res_hd
        while head:            
            if head.next:            
                g=self.gcd(head.val,head.next.val)
                g_li = ListNode(g,None)
                cur_node = ListNode(head.val,g_li)
                head = head.next
                hd.next = cur_node
                hd = g_li
            else:
                hd.next = head
                head =None
        return res_hd.next

        
if __name__ == "__main__":
    s=Solution()
