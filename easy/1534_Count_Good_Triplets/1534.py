#URL : https://leetcode.com/problems/count-good-triplets/description/?envType=daily-question&envId=2025-04-10
#[Easy] [1534] 
#Title: [Count Good Triplets]
#Author: Kartik Bhatnagar
#Date : 2025-04-14 (YYYY-MM-DD)
class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        def checkTriplet(n1,n2,n3):
            if abs(n1-n2) <=a:
                if abs(n3-n2)<=b:
                    if abs(n1-n3)<=c:                        
                        return True
            return False
        alen = len(arr)
        result =0
        for i in range(0,alen):
            for j in range(i+1,alen):
                for k in range(j+1,alen):
                    if checkTriplet(arr[i],arr[j],arr[k]):
                        result +=1
        return result
        
if __name__ == "__main__":
    s=Solution()
