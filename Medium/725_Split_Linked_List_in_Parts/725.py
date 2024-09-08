#URL : https://leetcode.com/problems/split-linked-list-in-parts/description/?envType=daily-question&envId=2024-09-08
#[Medium] [725] 
#Title: [Split Linked List in Parts]
#Author: Kartik Bhatnagar
#Date : 2024-09-08 (YYYY-MM-DD)

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def len_link_list(self,h):
        l =0
        while h:
            h =h.next
            l+=1
        return l
    def splitListToParts(self, head: ListNode, k: int) -> list:
        self.head = head
        result =[]
        hd=head
        print(head)
        def splt(h_count,k):
            print("!",h_count,k)
            for i in range(k):
                sv = (h_count//k)+((h_count/k)>h_count//k)
                print("%%",sv)
                k-=1
                h_count -=sv
                # print("@@",result)
                if self.head:
                    start_hd =self.head
                    hd =start_hd
                    if sv == 0:
                        print("#",[])
                        result.append(None)
                    else:
                        rs= ListNode(0,None)
                        rs_hd = rs
                        for j in range(sv-1):                            
                            if hd:
                                # print("^",hd.val)
                                # result.append(hd)
                                rs.next = ListNode(hd.val,None)
                                rs= rs.next
                                hd =hd.next
                            else:
                                # print("[]")
                                break
                        self.head = hd.next
                        hd.next =None
                        rs.next=hd
                        result.append(rs_hd.next)
                else:
                    print("___")
                    result.append(None)
                    
        splt(self.len_link_list(head),k)
        return result
if __name__ == "__main__":
    s=Solution()
