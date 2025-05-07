#URL : https://leetcode.com/problems/find-minimum-time-to-reach-last-room-i/description/?envType=daily-question&envId=2025-05-07
#[Medium] [3341] 
#Title: [Find Minimum Time to Reach Last Room I]
#Author: Kartik Bhatnagar
#Date : 2025-05-07 (YYYY-MM-DD)
class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        #we will solve it with shortest distance algo. dijstras algo
        #starting point will coordinate (0,0) and the end point will be the lowest right corner (n-1,m-1)
        n,m = len(moveTime), len(moveTime[0])
        unvisited = {(i,j):float('inf') for i in range(n) for j in range(m) }
        moveTime[0][0] = 0#starting is always 0 sec
        unvisited[(0,0)] = moveTime[0][0]
        visited = {(0,0) : 0}
        
        # print(visited)
        # print(unvisited)
        # for i in range(n):
        #     for j in range(m):
        #         moveTime[i][j] = moveTime[i][j]+1

        def key_with_min_value():
            #return the (key,value) from the unvisted dic with lowest value
            min_val =  min(unvisited.values())
            m = [k for k,v in unvisited.items() if v == min_val]
            return (m[0],min_val)
        adj_room = [(-1,0),(0,-1),(0,1),(1,0)]
        prev_node ={}
        while(len(unvisited)>0):
            ky,mval = key_with_min_value()
            # print(ky,mval)
            for ad in adj_room:
                x,y =ky[0] + ad[0] , ky[1] + ad[1]  
                # print(x,y)
                if (x >= 0 and x <= n-1) and (y>=0 and y <= m-1): #checking if the postion is valid row wise and colum wise
                    if (x,y) not in visited:
                        # print(x,y)
                        if max(mval , moveTime[x][y]) < unvisited[(x,y)] :
                            prev_node[(x,y)] = (ky)
                            unvisited[(x,y)] = max(mval , moveTime[x][y])+1
                        
            
            visited[ky] = mval
            unvisited.pop(ky)
        print(visited)    
        return visited[(n-1,m-1)]
        # print(unvisited)
        # print(visited)
        # print(prev_node)
        # last_corner = visited[(n-1,m-1)]
        # #traverse back until we reach back to (0,0)
        # reach_node = n-1,m-1
        # count =0
        # while(reach_node != (0,0)):      
        #     count +=1
        #     print(reach_node,moveTime[reach_node[0]][reach_node[1]])
        #     reach_node = prev_node[(reach_node)]

        #     # print(reach_node,count)
        # # print(last_corner)
        # return last_corner+count







        
        return 0
        
if __name__ == "__main__":
    s=Solution()
