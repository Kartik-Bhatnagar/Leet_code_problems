#URL : https://leetcode.com/problems/circular-sentence/submissions/1440415635/?envType=daily-question&envId=2024-11-02
#[Easy] [2490] 
#Title: [Circular Sentence]
#Author: Kartik Bhatnagar
#Date : 2024-11-02 (YYYY-MM-DD)
class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        words = sentence.split()
        prev_last_chr = words[0][-1]
        if words[-1][-1] != words[0][0]:
            #last character and first character are not equal
            return False
        # print(words)
        for i in range(1,len(words)):
            if words[i][0] != prev_last_chr:
                # print(words[-i],words[i][-1],prev_last_chr)
                return False
            prev_last_chr = words[i][-1]
            
        return True


        
if __name__ == "__main__":
    s=Solution()
