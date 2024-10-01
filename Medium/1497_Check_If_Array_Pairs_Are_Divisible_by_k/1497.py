#URL : https://leetcode.com/problems/check-if-array-pairs-are-divisible-by-k/submissions/1407722092/?envType=daily-question&envId=2024-10-01
#[Medium] [1497] 
#Title: [Check If Array Pairs Are Divisible by k]
#Author: Kartik Bhatnagar
#Date : 2024-10-01 (YYYY-MM-DD)

class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        # We need to find the remainder of each number in arr with k.
        # Then, we need to find if the sum of two numbers' remainders is divisible by k.
        # Specifically, for each number with remainder r, we need to find a corresponding number with remainder k - r.
        # If r == 0, we need an even count of numbers with remainder 0, as they can only pair among themselves.

        all_remainders ={}
        for i in range(len(arr)):
            rem = arr[i]%k
            all_remainders[rem] = all_remainders.get(rem,0)+1
        print(all_remainders)
        for r in all_remainders.keys():
            if r==0:
                if all_remainders[r]%2 != 0:
                    return False
            else:
                if  all_remainders.get(r,0) != all_remainders.get(k-r,0):
                    return False
        return True




        #  # pairs =[]
        # pairs_indx =set()
        # arr_len =len(arr)
        # for i in range(arr_len):
        #     if i not in pairs_indx:
        #         for j in range(i+1,arr_len):
        #             if j not in pairs_indx:
        #                 if (arr[i]+arr[j])%k == 0:
        #                     pairs_indx.add(i)
        #                     pairs_indx.add(j)
        #                     # pairs.append((arr[i],arr[j]))
        #                     break
        # # print(pairs)
        # # print(pairs_indx)
        # if len(pairs_indx) == arr_len:
        #     return True
        # else:
        #     return False
if __name__ == "__main__":
    s=Solution()
