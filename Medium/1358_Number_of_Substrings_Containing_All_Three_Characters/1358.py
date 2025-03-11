#URL : https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/?envType=daily-question&envId=2025-03-11
#[Medium] [1358] 
#Title: [Number of Substrings Containing All Three Characters]
#Author: Kartik Bhatnagar
#Date : 2025-03-11 (YYYY-MM-DD)

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        start =0
        end = 3 #given len of s is atleast 3 
        st = s[start:end]
        abc_dic = {"a":st.count("a"),"b":st.count("b"),"c":st.count("c")}
        result = 0#number of substr containing atleast one occurance of abc
        try:
            hig_indx = max(s.index("a"),s.index("b"),s.index("c"))
        except:
            return 0 #if any "a", "b" or "c" is missing
        # print(hig_indx)
        for start in range(0,len(s)-2):
            for end in range(max(start+3,hig_indx),len(s)+1):
                substr = s[start:end]
                if "a"in substr and "b" in substr  and "c" in substr:
                    result += (len(s)-end)+1
                    break
                
                # if "a" in substr and "b" in substr and "c" in substr:
                #     result +=1
        return result

        
if __name__ == "__main__":
    s=Solution()
