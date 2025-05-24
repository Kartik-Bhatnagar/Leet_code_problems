#URL : https://leetcode.com/problems/find-words-containing-character/?envType=daily-question&envId=2025-05-22
#[Easy] [2942] 
#Title: [Find Words Containing Character]
#Author: Kartik Bhatnagar
#Date : 2025-05-24 (YYYY-MM-DD)
class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        result = []
        for i in range(len(words)):
            # if x in words[i]:
            #     result.append(i)
            for char in words[i]:
                if char == x:
                    result.append(i)
                    break
        return result
            
        
if __name__ == "__main__":
    s=Solution()
