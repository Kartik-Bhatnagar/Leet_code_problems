#URL : https://leetcode.com/problems/rank-transform-of-an-array/description/?envType=daily-question&envId=2024-10-02
#[Easy] [1331] 
#Title: [Rank Transform of an Array]
#Author: Kartik Bhatnagar
#Date : 2024-10-02 (YYYY-MM-DD)
class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        arr_sort = sorted(arr)
        print(arr_sort)
        #arr_dic = {arr_sort[i]:i+1 for i in range(len(arr_sort))}
        rank=1
        arr_dic =dict()
        for i in range(len(arr_sort)):
            if arr_sort[i] not in arr_dic:
                arr_dic[arr_sort[i]] = rank
                rank +=1
        result = [arr_dic[arr[i]] for i in range(len(arr))]
        return result
if __name__ == "__main__":
    s=Solution()
