#URL : https://leetcode.com/problems/count-vowel-strings-in-ranges/description/?envType=daily-question&envId=2025-01-02
#[Medium] [2559] 
#Title: [Count Vowel Strings in Ranges]
#Author: Kartik Bhatnagar
#Date : 2025-01-02 (YYYY-MM-DD)
class Solution:
    # def isVowel(self, word):
    #     return word[0] in self.vowels and word[-1] in self.vowels    

    # def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
    #     #lets mark vowel in the list itself
    #     self.vowels = ["a","e","i","o","u"]
    #     # words_v =[self.isVowel(words[i]) for i in range(len(words))]
    #     # result =[]
    #     # for q in queries:
    #     #     result.append(sum(words_v[q[0]:q[1]+1]))
    #     # return result

    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        #calculate the cummulative sum of words starting and ending with vowels
        vowel_count =0
        vowels = {"a","e","i","o","u"}
        word_vowel_sum =[]
        for i in range(len(words)):
            vowel_count = vowel_count + (1 if words[i][0] in vowels and words[i][-1] in vowels else 0)
            word_vowel_sum.append(vowel_count)
        print(word_vowel_sum)
        result =[]
        for q in queries:
            # print(f"{word_vowel_sum[q[1]]} - { word_vowel_sum[q[0]]} +{+ 1 if words[q[0]][0] in vowels and words[q[0]][-1] in vowels else 0}")
            # print(word_vowel_sum[q[1]] - word_vowel_sum[q[0]] + 1 if words[q[0]][0] in vowels and words[q[0]][-1] in vowels else 0)
            result.append(word_vowel_sum[q[1]] - word_vowel_sum[q[0]] +( 1 if words[q[0]][0] in vowels and words[q[0]][-1] in vowels else 0))
            # first-word_is_vowel =  1 if words[q[0]][0] in vowels and words[q[0]][-1] in vowels else 0
        return result
if __name__ == "__main__":
    s=Solution()
