#URL : https://leetcode.com/problems/string-matching-in-an-array/description/?envType=daily-question&envId=2025-01-07
#[Easy] [1408] 
#Title: [String Matching in an Array]
#Author: Kartik Bhatnagar
#Date : 2025-01-07 (YYYY-MM-DD)
class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        result = []
        for w1 in range(len(words)):
            for w2 in range(w1+1,len(words)):
                if words[w1] in words[w2]:
                    result.append(words[w1])
                elif words[w2] in words[w1]:
                    result.append(words[w2])
        return list(set(result))
if __name__ == "__main__":
    s=Solution()
