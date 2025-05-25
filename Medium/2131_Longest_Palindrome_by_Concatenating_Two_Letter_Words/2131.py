#URL : https://leetcode.com/problems/longest-palindrome-by-concatenating-two-letter-words/description/?envType=daily-question&envId=2025-05-22
#[Medium] [2131] 
#Title: [Longest Palindrome by Concatenating Two Letter Words]
#Author: Kartik Bhatnagar
#Date : 2025-05-25 (YYYY-MM-DD)
class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        word_count = {}
        for word in words:
            word_count[word]= word_count.get(word,0)+1
        # print(word_count)
        result =0
        same_extra = False #check if there is a spare double char word , can be use in palid. (it will be instered at exact middle)
        while(len(word_count)>0):
            word = list(word_count.keys())[0]
            # word =next(iter(word_count))
            rev_word = word[::-1]
            if rev_word == word:# same word
                count = word_count[word]
                if count %2 ==1:
                    same_extra = True
                result += ((count//2)*2)*2 #even number (either the same num if it is even or the nearest lowest even num)
                word_count.pop(word) #remove the word from the dict.
            else: # diff chars word
                if rev_word in word_count:
                    result += min(word_count.get(word),word_count.get(rev_word))*4#checking both word and rev word count, the lowest count will be added in result to form the plaindrom
                    word_count.pop(rev_word)
                word_count.pop(word)
            # print(word,result)
        if same_extra:
            result +=2
        return result
if __name__ == "__main__":
    s=Solution()
