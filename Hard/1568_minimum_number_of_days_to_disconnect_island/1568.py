#minimum_number_of_days_to_disconnect_island
#url :https://leetcode.com/problems/minimum-number-of-days-to-disconnect-island/description/
#Date : 11/08/2024
#Author : Kartik Bhatnagar
import time
class Solution:
    def noOfIsland(self,grid):
        #returns the number of islands from the grid
        #using dfs we will find out the total number of idependent island
        #start iteration when the element is 1, in one main dfs operation all 1's will be covered
        #total island will be the number of total MAIN dfs operations operated

        def dfs(r,c):
            if grid[r][c] ==0:
                return
            visited.add((r,c))
            neighbours = [(r-1,c),(r+1,c),(r,c-1),(r,c+1)]#  island is a maximal 4-directionally 
            for nr,nc in neighbours:
                if nr>=0 and nr<rows_len and nc>=0 and nc<cols_len and (nr,nc) not in visited:
                    dfs(nr,nc)
        
        visited =set() #notes the island visited #only visit them once
        rows_len = len(grid)
        cols_len =len(grid[0])
        island_count =0
        for r in range(rows_len):
            for c in range(cols_len):
                if grid[r][c] ==1 and (r,c) not in visited:
                    dfs(r,c)
                    island_count+=1
        return island_count    
    def minDays(self, grid: list[list[int]]) -> int:
        if self.noOfIsland(grid) != 1:
            #islands are disconnected
            return 0
        #there will be maximum 2 removal ; the intution is we can always disconnect 
        # one single corner node island from the whole island by disconnecting its 2 neighbouring nodes

        #brute force trying removing 1 land node
        grid_rows=len(grid)
        grid_cols=len(grid[0])
        grid_new = [row[:] for row in grid]
        for r in range(grid_rows):
            if 1 in grid[r]:
                for c in range(grid_cols):
                    if grid[r][c]==1:                        
                        grid_new[r][c]=0
                        island_count = self.noOfIsland(grid_new)
                        if island_count!= 1:#island got disconnected
                            # print(r,c,grid)
                            return 1
                        grid_new[r][c]=1
        #tried disconnected all possible 1 land node at once; but island doesn;t became diconnected now the island should be disconnected with 2 land node removal                
        return 2

        

        pass
if __name__ == "__main__":
    s1=Solution()
    start_time1 = time.time()
    grid1=[[0,1,1,0],[0,1,1,0],[0,0,0,0]]
    print(s1.minDays(grid1))
    end_time1=time.time()#-start_time1
    grid2=[[0,0,0,1],[0,1,1,1],[1,1,1,0]]
    print(s1.minDays(grid2))
    end_time2 =time.time()#-start_time1-end_time1
    grid3=[[1,1]]
    print(s1.minDays(grid3))
    end_time3=time.time()#-start_time1-end_time2
    print(f"{end_time1-start_time1:.9f} : {end_time2-end_time1:.9f} : {end_time3-end_time1:.9f}")
        