#URL : https://leetcode.com/problems/rabbits-in-forest/description/?envType=daily-question&envId=2025-04-17
#[Medium] [781] 
#Title: [Rabbits in Forest]
#Author: Kartik Bhatnagar
#Date : 2025-04-20 (YYYY-MM-DD)
class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        result =0
        for nm in set(answers):
            if nm!=0:
                num_count = answers.count(nm)-1
                rab_groups = (num_count //(nm+1))+1 #+1 in the added to truncate
                rabs_count = rab_groups*(nm+1)
                # print(nm,rab_groups,rabs_count)
                result += rabs_count
        zero_count = answers.count(0)
        if zero_count >0:
            result += zero_count
        return result
if __name__ == "__main__":
    s=Solution()
