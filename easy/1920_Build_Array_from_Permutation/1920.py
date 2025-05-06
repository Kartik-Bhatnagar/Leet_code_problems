#URL : https://leetcode.com/problems/build-array-from-permutation/description/?envType=daily-question&envId=2025-05-04
#[Easy] [1920] 
#Title: [Build Array from Permutation]
#Author: Kartik Bhatnagar
#Date : 2025-05-06 (YYYY-MM-DD)
class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans =[]
        for num in nums:
            ans.append(nums[num])
        return ans

        
if __name__ == "__main__":
    s=Solution()
