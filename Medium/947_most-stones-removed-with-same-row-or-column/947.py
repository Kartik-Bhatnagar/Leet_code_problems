#URL : https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/description/?envType=daily-question&envId=2024-08-29
#[Medium] [947] 
#Title: [most-stones-removed-with-same-row-or-column]
#Author: Kartik Bhatnagar
#Date : 2024-08-29 (YYYY-MM-DD)
class Solution:
    def removeStones(self, stones: list[list[int]]) -> int:
        #find all connected components;using dfs(go deep for common rows and columns)
        #the total number of stones will be the sum of stones collected in each component
        #in each  connected component ; the sum of stones collected is = the number of stones -1
        def dfs_row_col(i,j):
            visited.add((i,j))            
            stones_copy.remove([i,j])
            stones_copy2 = stones_copy.copy()
            for c in stones_copy2:
                di,dj = c
                if (di,dj) not in visited:
                    if di == i or dj ==j:
                        dfs_row_col(di,dj)

        visited =set()
        stones_copy =stones.copy()
        visit_last_count =0
        tot_stones = 0
        for cord in stones:
            i,j= cord
            if (i,j) not in visited:
                dfs_row_col(i,j)
                tot_stones +=len(visited)-visit_last_count -1
                visit_last_count = len(visited)
                print("***")
        return tot_stones
if __name__ == "__main__":
    s=Solution()
