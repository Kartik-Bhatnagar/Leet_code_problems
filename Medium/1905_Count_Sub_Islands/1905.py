#URL : https://leetcode.com/problems/count-sub-islands/?envType=daily-question&envId=2024-08-28
#[Medium] [1905] 
#Title: [Count Sub Islands]
#Author: Kartik Bhatnagar
#Date : 2024-08-28 (YYYY-MM-DD)
import time
class Solution:
    def countSubIslands(self, grid1: list[list[int]], grid2: list[list[int]]) -> int:

        def dfs(i,j,grid,island):
            if (i,j) in visited:
                return island
            visited.add((i,j))
            if grid[i][j] == 1:
                island.add((i,j))
            neighbours = [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]
            for ne in neighbours:
                if ne not in visited and ne[0]>=0 and ne[1] >=0 and ne[0]<len(grid) and ne[1]<len(grid[0]):
                    print(ne)
                    print(ne[1]<len(grid))
                    if grid[ne[0]][ne[1]] == 1:
                        # print("**")
                        island = dfs(ne[0],ne[1],grid,island)
            return island
        visited =set()
        islands1 =[]
        for i in range(len(grid1)):
            for j in range(len(grid1[0])):
                if((i,j)) not in visited and grid1[i][j] == 1:
                    island =set()
                    # print(i,j)
                    island = dfs(i,j,grid1,island)
                    islands1.append(island)
                    # print(f"Island {island}")
        print(islands1)
        islands2=[]
        visited =set()
        for i in range(len(grid2)):
            for j in range(len(grid2[0])):
                if((i,j)) not in visited and grid2[i][j] == 1:
                    island =set()
                    # print(i,j)
                    island = dfs(i,j,grid2,island)
                    islands2.append(island)
                    # print(f"Island {island}")

        print("&&",islands2)
        result=0
        for is2 in islands2:
            for is1 in islands1:
                if is2.issubset(is1):
                    print(is2)
                    result +=1
                    break
            
        return result
    
if __name__ == "__main__":
    grid1 = [[1,1,1,0,0],[0,1,1,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,1,1]]
    grid2 = [[1,1,1,0,0],[0,0,1,1,1],[0,1,0,0,0],[1,0,1,1,0],[0,1,0,1,0]]
    s=Solution()
    # print(s.countSubIslands( grid1,grid2))
    grid1=[[1,1,1,1,0,0],[1,1,0,1,0,0],[1,0,0,1,1,1],[1,1,1,0,0,1],[1,1,1,1,1,0],[1,0,1,0,1,0],[0,1,1,1,0,1],[1,0,0,0,1,1],[1,0,0,0,1,0],[1,1,1,1,1,0]]
    grid2=[[1,1,1,1,0,1],[0,0,1,0,1,0],[1,1,1,1,1,1],[0,1,1,1,1,1],[1,1,1,0,1,0],[0,1,1,1,1,1],[1,1,0,1,1,1],[1,0,0,1,0,1],[1,1,1,1,1,1],[1,0,0,1,0,0]]
    print(s.countSubIslands( grid1,grid2))
    t1=time.time()
    with open("Data/grid1_54.txt","r")as r:
        grid1 = eval(r.read())
    with open("Data/grid2_54.txt","r")as r:
        grid2 = eval(r.read())
    print(s.countSubIslands( grid1,grid2))
    t2=time.time()
    print(f"Time taken {t2-t1} seconds")