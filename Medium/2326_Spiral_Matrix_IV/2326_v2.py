#URL : https://leetcode.com/problems/spiral-matrix-iv/description/?envType=daily-question&envId=2024-09-09
#[Medium] [2326] 
#Title: [Spiral Matrix IV]
#Author: Kartik Bhatnagar
#Date : 2024-09-09 (YYYY-MM-DD)


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def next_dir(self,r,c,di):
        if di == "E":
            if c+1<self.max_cols :
                return "E"
            else:   
                #incrment the lower limit of the row
                self.min_rows = r+1             
                return "S"#change direction to south
        if di == "S":
            if r+1<self.max_rows  :
                return "S"
            else:
                self.max_cols = c+1-1 
                return "W"                
        if di == "W" :
            if c-1>=self.min_cols:
                return "W"
            else:
                self.max_rows = r+1-1 
                return "N"
        if di == "N":
            if r-1>=self.min_rows :
                return "N"
            else:
                self.min_cols = c+1 
                return "E"
    def next_cord(self,r,c,di):
        if di == "E":
            return (r,c+1)
        if di == "S":
            return (r+1,c)
        if di == "W":
            return (r,c-1)
        if di == "N":
            return (r-1,c)
            
        
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        self.head = head
        self.min_rows,self.min_cols=0,0
        self.max_rows,self.max_cols = m,n
        self.dirs =["E","S","W","N"]
        cur_dir =self.dirs[0] #in starting the elements will fill in eastward direction
        result = [[-1 for i in range(n)] for j in range(m)]
        print(result)
        i,j=0,-1 #for tracking the position of matrix  
        # self.visited =set()       
        while self.head:            
            cur_dir = self.next_dir(i,j,cur_dir)
            (i,j) = self.next_cord(i,j,cur_dir)
            # print(i,j,cur_dir)
            result[i][j] = self.head.val
            self.head = self.head.next
            # self.visited.add((i,j))
        return result