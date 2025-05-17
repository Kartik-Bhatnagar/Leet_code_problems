#URL : https://leetcode.com/problems/sort-colors/description/?envType=daily-question&envId=2025-05-16
#[Medium] [75] 
#Title: [Sort Colors]
#Author: Kartik Bhatnagar
#Date : 2025-05-17 (YYYY-MM-DD)
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        #given there are only three possiblecolours, we will create a dict 
        #keys will be the integer 0 , 1 and 2
        #values will be the occuraces of 0 1 nd 2 resp.
        
        #SOLUTION 1
        #nums.sort()

        #Solution 2
        occur = {0:0,1:0,2:0}
        for num in nums:
            occur[num] = occur[num] +1
        result =[]
        for k,v in occur.items():
            print(k,v)
            result.extend([k]*v)
            print(result)
        # given we no need to send the result instead we need to modify nums variable
        nums[:] = result
if __name__ == "__main__":
    s=Solution()
