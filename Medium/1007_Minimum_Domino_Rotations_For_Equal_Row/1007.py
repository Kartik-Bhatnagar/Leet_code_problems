 c#URL : https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/description/?envType=daily-question&envId=2025-05-03
#[Medium] [1007] 
#Title: [Minimum Domino Rotations For Equal Row]
#Author: Kartik Bhatnagar
#Date : 2025-05-03 (YYYY-MM-DD)
class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        t_dic = {tops.count(i):i for i in range(1,7)}
        max_t = t_dic[max(t_dic)] # max occrance no.
        b_dic = {bottoms.count(i):i for i in range(1,7)}
        max_b = b_dic[max(b_dic)]
        #checking if max_t is achieved on all dominoes
        up=True
        up_rot_count = 0
        # print(f"*{max_t}")
        for i in range(len(tops)):
            # print(tops[i],up_rot_count)
            if tops[i] == max_t:
                continue
            elif tops[i] != max_t and bottoms[i] == max_t:
                up_rot_count +=1
            else:
                up = False
                break
        low = True
        low_rot_count = 0
        # print(f"*{max_b}")
        #checking if max_b is acheived on all dominoes
        for i in range(len(tops)):
            # print(bottoms[i],low_rot_count)
            if bottoms[i] == max_b:
                continue
            elif bottoms[i] != max_b and tops[i] == max_b:
                low_rot_count +=1
            else:
                low = False
                break
        if up and low:
            return min(low_rot_count,up_rot_count)
        if low and not up:
            print(low,up)
            return low_rot_count
        if up and not low:
            print("&&")
            return up_rot_count
        return -1
if __name__ == "__main__":
    s=Solution()
