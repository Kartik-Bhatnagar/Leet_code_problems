#URL : https://leetcode.com/problems/type-of-triangle/description/?envType=daily-question&envId=2025-05-19
#[Easy] [3024] 
#Title: [Type Of Triangle]
#Author: Kartik Bhatnagar
#Date : 2025-05-19 (YYYY-MM-DD)
class Solution:
    def triangleType(self, nums: List[int]) -> str:
        if nums[0] == nums[1] == nums[2]:
            return "equilateral"
        #check if the sides are forming the triangle
        if nums[0]+nums[1] > nums[2] and nums[0]+nums[2] > nums[1] and nums[1]+nums[2] > nums[0]:
            if (nums[0] == nums[1] and nums[1] !=nums[2]) or (nums[1] == nums[2] and nums[1] !=nums[0]) or  (nums[0] == nums[2] and nums[1] !=nums[2]):
                return "isosceles"
            else:
                return "scalene"
        return "none"
        
if __name__ == "__main__":
    s=Solution()
