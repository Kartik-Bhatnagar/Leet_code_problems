"""
Convert a non-negative integer num to its English words representation.

 

Example 1:

Input: num = 123
Output: "One Hundred Twenty Three"
Example 2:

Input: num = 12345
Output: "Twelve Thousand Three Hundred Forty Five"
Example 3:

Input: num = 1234567
Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
 

Constraints:

0 <= num <= 231 - 1"""

class Solution:
    def split_hundred(self,nu) -> list:
        nu = str(nu)
        nu = (3-len(nu))*"0"+nu #add 0 as prefix if the total integers are less than 3
        nu = [int(n) for n in nu]
        return nu

    def hundred_to_word(self,s_num)->str:
        ones =["One","Two","Three","Four","Five","Six","Seven","Eight","Nine"]
        tens =[["Ten","Eleven","Twelve","Thirteen","Fourteen","Fifteen","Sixteen","Seventeen","Eighteen","Nineteen"],"Twenty","Thirty","Forty","Fifty","Sixty","Seventy","Eighty","Ninety"]
        h_num_lis = self.split_hundred(s_num) #hundred number list
        h_str=""
        for i in range(3):
            if h_num_lis[i] != 0:            
                if i == 1:
                    if h_num_lis[i] == 1:
                        h_str += tens[0][h_num_lis[2]]+" "
                        break
                    else:
                        h_str += tens[h_num_lis[i]-1]+" "

                else: #if i is 0 or 2
                    h_str += ones[h_num_lis[i]-1] +" "  
                    if i == 0 :
                        h_str += "Hundred"+ " "
        return h_str
            
    def split_whole_num(self,num):
        #split the whole given number with 3 decimal places
        num_str = str(num)
        num_lis =[]
        while len(num_str)>0:
            num_lis.append(num_str[-3:])
            num_str = num_str[:-3]
        return num_lis

    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        large_num =["","Thousand","Million","Billion"]#above_2_digit
        split_num = self.split_whole_num(num)
        word = ""
        for i in range(len(split_num)-1,-1,-1):
            hund =self.hundred_to_word(split_num[i])
            if len(hund)>0:
                word += hund +  large_num[i]+" "
        return word.rstrip()


if __name__== "__main__":
    s =Solution()
    inputs =[123,12345,1234567,0,7,10,1000000,300000000,2421521,63462432,231,822000003]
    for num in inputs:
        print(f"{num} : {s.numberToWords(num)}")
