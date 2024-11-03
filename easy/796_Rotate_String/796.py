#URL : https://leetcode.com/problems/rotate-string/description/
#[Easy] [796] 
#Title: [Rotate String]
#Author: Kartik Bhatnagar
#Date : 2024-11-03 (YYYY-MM-DD)
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        return s in goal+goal and len(goal) == len(s)
if __name__ == "__main__":
    s=Solution()
