#URL : https://leetcode.com/problems/construct-the-minimum-bitwise-array-i/description/?envType=daily-question&envId=2026-01-20
#[Easy] [3314] 
#Title: [Construct the Minimum Bitwise Array I]
#Author: Kartik Bhatnagar
#Date : 2026-01-20 (YYYY-MM-DD)
class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        def OR(dnum1,dnum2):
            bnum1 = dec_to_bin(dnum1)
            bnum2=dec_to_bin(dnum2)
            mlen = max(len(bnum1),len(bnum2))
            bnum1 = ("0"*(mlen-len(bnum1))) + (bnum1)
            bnum2 = ("0"*(mlen-len(bnum2))) + (bnum2)
            ans=""
            for i in range(mlen):
                if bnum1[i] == "1" or bnum2[i]=="1":
                    ans+="1"
                else:
                    ans+="0"
            return bin_to_dec(ans)

        def dec_to_bin(dnum):
            bnum=""
            while dnum >1:
                r = dnum%2
                dnum = dnum//2
                bnum = str(r)+bnum
            bnum = str(dnum)+bnum
            return bnum
        def bin_to_dec(bnum):
            ans=0
            mult=1
            for b in bnum[::-1]:
                ans += mult *int(b)
                mult = mult*2
            return ans

        result =[]
        for num in nums:
            found = False
            for n in range(num):
                # if OR(n,n+1) == num:
                if (n | (n+1)) == num:
                    result.append(n)
                    found = True
                    break
            if not found:
                result.append(-1)
        return result
                
        #     b = dec_to_bin(num)
        #     print(b)
        # ans = OR(14,34)
        # print(ans)


if __name__ == "__main__":
    s=Solution()
