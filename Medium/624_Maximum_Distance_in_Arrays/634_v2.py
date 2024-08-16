#URL : https://leetcode.com/problems/maximum-distance-in-arrays/description/?envType=daily-question&envId=2024-08-16
#[Medium] [624] 
#Title: [Maximum Distance in Arrays]
#Author: Kartik Bhatnagar
#Date : 2024-08-16 (YYYY-MM-DD)

#V2: the previous solution was pretty big it can be solved with change in logic
#will find the latest distance as we go through the iteration
class Solution:
    
        
    def maxDistance(self, arrays: list[list[int]]) -> int:
        cur_min,cur_max = arrays[0][0],arrays[0][-1]
        max_dis=0#holds the value of max distance 

        for i in range(1,len(arrays)):
            array_min,array_max=arrays[i][0],arrays[i][-1]
            max_dis = max(
                max_dis,
                array_max - cur_min,
                cur_max - array_min
            )
            cur_max=max(array_max,cur_max)
            cur_min = min(array_min,cur_min)
        return max_dis

        
if __name__ == "__main__":
    s=Solution()
    arrays = [[1,2,3],[4,5],[1,2,3]]
    #print(s.maxDistance(arrays))
    arrays =[[1,2,3],[20,40,60],[1,2,3],[-7,2,800],[-5,1,700],[-50,2,3],[600,700,8000],[8900,9000],[-100,-100,-100],
             [-110,456,9001]]
    # print(s.maxDistance(arrays))
    arrays=[[1,5],[3,4]]
    # print(s.maxDistance(arrays))
    arrays=[[-1,1],[-3,1,4],[-2,-1,0,2]]
    # print(s.maxDistance(arrays))
    arrays=[[-5],[-9,-8,-7,-5,1,1,1,3],[-10,-7,-6,-6,-6,0,1,3,3],[-10,-8,-7,-2,3,3],[-1,4],[-5,-4,-1]]
    print(s.maxDistance(arrays))
              
