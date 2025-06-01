#URL : https://leetcode.com/problems/distribute-candies-among-children-ii/description/?envType=daily-question&envId=2025-06-01
#[Medium] [2929] 
#Title: [Distribute Candies Among Children II]
#Author: Kartik Bhatnagar
#Date : 2025-06-01 (YYYY-MM-DD)
class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        result =0
        for i in range(min(limit,n),-1,-1):
            #for each i we will find the count of comination left out of candies
            up = min(n-i,limit)
            low = max(n-(i+up),0)
            if low<= limit:
                # print(i,up,low)
                result += (up-low)+1
                # print(result)
        return result
        #____TLE 504/958__________
        """result=0
        for i in range(min(limit,n),-1,-1):
            for j in range(min(n-i,limit),-1,-1):
                k=(n-(i+j))
                # print(i,j,k)
                if k <= limit :
                    result+=1
                    # print(result)
        return result"""


        
if __name__ == "__main__":
    s=Solution()
