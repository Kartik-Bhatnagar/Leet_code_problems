#URL : https://leetcode.com/problems/shifting-letters-ii/description/?envType=daily-question&envId=2025-01-04
#[Medium] [2381] 
#Title: [Shifting Letters II]
#Author: Kartik Bhatnagar
#Date : 2025-01-05 (YYYY-MM-DD)

#https://www.youtube.com/watch?v=eEUjVY7wK3k
class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        # count =0
        # chars_indx,indx_chars ={},{}
        # for c in ("abcdefghijklmnopqrstuvwxyz"):
        #     chars_indx[c]  = count
        #     indx_chars[count] =c
        #     count+=1
        # # print(chars_indx)
        # for shift in shifts:
        #     new_chars =[]
        #     if shift[2] == 0:#shift 1 indx backwards
        #         for j in range(shift[0],shift[1]+1):
        #             new_pos = (chars_indx[s[j]]-1)%26
        #             new_chars.append(indx_chars[new_pos])
        #     else: #shift 1 indx forward
        #         for j in range(shift[0],shift[1]+1):
        #             new_pos = (chars_indx[s[j]]+1)%26
        #             new_chars.append(indx_chars[new_pos])
        #     s = s[:shift[0]]+"".join(new_chars)+s[shift[1]+1:]
        # return s

        #apporach 2
        #for each index in s calculate the final net resultant postion after caluclating all shift changes
        # s_index = {}
        # for shift in shifts:
        #     if shift[2] ==0: #backward
        #         for j in range(shift[0],shift[1]+1):
        #             s_index[j] = s_index.get(j,0)-1
        #     else:
        #         for j in range(shift[0],shift[1]+1):
        #             s_index[j] = s_index.get(j,0)+1
        # print(s_index)

        #apporach 3
        count =0
        chars_indx,indx_chars ={},{}
        for c in ("abcdefghijklmnopqrstuvwxyz"):
            chars_indx[c]  = count
            indx_chars[count] =c
            count+=1
        prefix_diff = [0]*(len(s)+1)
        for left,right,d in shifts:
            if d == 0: #backward
                prefix_diff[right+1] -= 1
                prefix_diff[left] +=1
            else:#forward
                prefix_diff[right+1] +=1
                prefix_diff[left] -=1
        diff = prefix_diff[-1]
        new_pos = (chars_indx[s[-1]] + diff)%26
        result =[indx_chars[new_pos]]
        # print(prefix_diff)
        for i in range(2,len(prefix_diff)):
            #result is from  backwards
            diff += prefix_diff[-1*i]
            new_pos = (chars_indx[s[-1*i]] + diff)%26
            result.append(indx_chars[new_pos])
        return "".join(result[::-1])


if __name__ == "__main__":
    s=Solution()
