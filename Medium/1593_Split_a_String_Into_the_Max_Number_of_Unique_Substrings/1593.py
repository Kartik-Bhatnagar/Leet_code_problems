
##URL : https://leetcode.com/problems/split-a-string-into-the-max-number-of-unique-substrings/description/?envType=daily-question&envId=2024-10-21
#[Medium] [1593] 
#Title: [Split a String Into the Max Number of Unique Substrings]
#Author: Kartik Bhatnagar
#Date : 2024-10-21 (YYYY-MM-DD)
class Solution:
    #https://www.youtube.com/watch?v=fLjeVALxzjg
    def maxUniqueSplit(self, s: str) -> int:
        def dfs(i,cur_set):
            if i == len(s):
                return 0
            res=0
            for j in range(i,len(s)):
                substr = s[i:j+1]
                if substr not in cur_set:
                    cur_set.add(substr)
                    res = max(res,1+dfs(j+1,cur_set))
                    cur_set.remove(substr)
            return res
        return dfs(0,set())
if __name__ == "__main__":
    s=Solution()
