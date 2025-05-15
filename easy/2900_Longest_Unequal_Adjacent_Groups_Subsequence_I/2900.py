#URL : https://leetcode.com/problems/longest-unequal-adjacent-groups-subsequence-i/?envType=daily-question&envId=2025-05-15
#[Easy] [2900] 
#Title: [ Longest Unequal Adjacent Groups Subsequence I]
#Author: Kartik Bhatnagar
#Date : 2025-05-15 (YYYY-MM-DD)
class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        sub_seq = [words[0]]
        prev = groups[0]
        for i in range(1,len(words)):
            if prev != groups[i]:
                sub_seq.append(words[i])
                prev= groups[i]
        return sub_seq

            
        
if __name__ == "__main__":
    s=Solution()
