#URL : https://leetcode.com/problems/count-prefix-and-suffix-pairs-i/submissions/1501523597/?envType=daily-question&envId=2025-01-08
#[Easy] [3042] 
#Title: [Count Prefix and Suffix Pairs I]
#Author: Kartik Bhatnagar
#Date : 2025-01-08 (YYYY-MM-DD)

class Solution:
    def isPrefixAndSuffix(self,w1,w2):
        if len(w2) < len(w1):
            return False
        return w1 == w2[:len(w1)] and w1 == w2[len(w2)-len(w1):]
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        result =0
        for i in range(len(words)):
            for j in range(i+1,len(words)):
                result += 1 if self.isPrefixAndSuffix(words[i],words[j]) else 0
        return result

if __name__ == "__main__":
    s=Solution()
