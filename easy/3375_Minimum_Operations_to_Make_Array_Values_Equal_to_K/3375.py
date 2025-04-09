#URL : https://leetcode.com/problems/minimum-operations-to-make-array-values-equal-to-k/submissions/1601901301/?envType=daily-question&envId=2025-04-09
#[Easy] [3375] 
#Title: [Minimum Operations to Make Array Values Equal to K]
#Author: Kartik Bhatnagar
#Date : 2025-04-09 (YYYY-MM-DD)
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        unique_num = set()
        for num in nums:
            if num > k:
                unique_num.add(num)
            if num <k:
                return -1
if __name__ == "__main__":
    s=Solution()
