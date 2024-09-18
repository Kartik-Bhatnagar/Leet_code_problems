#URL : https://leetcode.com/problems/uncommon-words-from-two-sentences/description/?envType=daily-question&envId=2024-09-17
#[Easy] [884] 
#Title: [Uncommon Words from Two Sentences]
#Author: Kartik Bhatnagar
#Date : 2024-09-17 (YYYY-MM-DD)

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> list[str]:
        def di(s):
            d =dict()
            for word in s.split(" "):
                d[word]= d.get(word,0)+1
            return d
        d1= di(s1)
        d2=di(s2)
        result =[]
        for w,count in d1.items():
            if count == 1 and w not in d2:
                result.append(w)
        for w, count in d2.items():
            if count == 1 and w not in d1:
                result.append(w)
        return result

if __name__ == "__main__":
    s=Solution()
