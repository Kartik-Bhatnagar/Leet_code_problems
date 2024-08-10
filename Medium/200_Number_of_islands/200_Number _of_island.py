#https://leetcode.com/problems/number-of-islands/description/
class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        #1 : Land ; 0: Water
        #Approach:-> we will start visiting each land cell with dfs method and cover all the possible neighbour land cells ;cell having value(1) value  ; 
        #the total number of 1's visited in one main dfs search will be considered as 1 main island
        #keep a record of alredy visted land cell (having value 1); do not visit it again
        #iterate through the full grid and find the number of total island
        tot_rows,tot_cols = len(grid),len(grid[0])
        def dfs(r,c):
            if grid[r][c] == "0":
                return
            visited.add((r,c))
            neighbour_land = [(r-1,c),(r+1,c),(r,c-1),(r,c+1)]
            for nr,nc in neighbour_land:
                if (nr >=0 and nr < tot_rows and nc >=0 and nc < tot_cols and (nr,nc) not in visited):
                    dfs(nr,nc)

        visited =set() #keeps the record of (row,column) of already visited 1's cell
        tot_island =0
        for r in range(tot_rows):
            for c in range(tot_cols):
                if grid[r][c] == "1" and (r,c) not in visited:
                    dfs(r,c)
                    tot_island +=1
        return tot_island

if __name__ =="__main__":
    s =  Solution()
    grid1 = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
    grid2 = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
    
    print(s.numIslands(grid1))
    print(s.numIslands(grid2))