#URL : https://leetcode.com/problems/defuse-the-bomb/description/
#[Easy] [1652] 
#Title: [Defuse the Bomb]
#Author: Kartik Bhatnagar
#Date : 2024-11-02 (YYYY-MM-DD)
class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        
        if k == 0:
            return([0 for k in range(len(code))])
        else:
            code_2 = code[:]+code[:]
            n=len(code)
            ret_lis=[]
            if k>0:                
                for ele in range(len(code)):
                    ret_lis.append(sum(code_2[ele+1:(ele+1+k)])) 
                return(ret_lis)    
            else :
                for ele in range(len(code),len(code_2)):
                    ret_lis.append(sum(code_2[ele+k:ele])) 
                return(ret_lis)


if __name__ == "__main__":
    s=Solution()
