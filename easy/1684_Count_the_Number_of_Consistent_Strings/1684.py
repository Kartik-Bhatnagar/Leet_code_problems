#URL : https://leetcode.com/problems/count-the-number-of-consistent-strings/description/?envType=daily-question&envId=2024-09-12
#[Easy] [1684] 
#Title: [Count the Number of Consistent Strings]
#Author: Kartik Bhatnagar
#Date : 2024-09-12 (YYYY-MM-DD)

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed =set(allowed)
        count=0
        for word in words:
            for w in (word):
                not_cons =True  
                if w not in allowed:
                    not_cons =False 
                    print(w,word)                   
                    break
            if not_cons: count+=1
        return count
                    

        

if __name__ == "__main__":
    s=Solution()
