#URL : https://leetcode.com/problems/spiral-matrix/description/
#[Medium] [54] 
#Title: [Spiral Matrix]
#Author: Kartik Bhatnagar
#Date : 2024-09-09 (YYYY-MM-DD)

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
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        self.min_rows,self.min_cols=0,0
        self.max_rows,self.max_cols = len(matrix),len(matrix[0])
        tot_rows,tot_cols=len(matrix),len(matrix[0])
        cur_dir="E"
        ro,co=0,-1
        result =[]
        for i in range(tot_rows*tot_cols):
            cur_dir = self.next_dir(ro,co,cur_dir)
            ro,co = self.next_cord(ro,co,cur_dir)
            result.append(matrix[ro][co])
        return result

if __name__ == "__main__":
    s=Solution()
