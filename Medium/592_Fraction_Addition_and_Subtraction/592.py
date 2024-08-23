#URL : https://leetcode.com/problems/fraction-addition-and-subtraction/description/?envType=daily-question&envId=2024-08-23
#[Medium] [592] 
#Title: [Fraction Addition and Subtraction]
#Author: Kartik Bhatnagar
#Date : 2024-08-23 (YYYY-MM-DD)
class Solution:
    def op_frac_list(self,expression):
        op = []
        
        if expression[0]!="-":#if the first number is poistive
            op.append("+")
        else:
            op.append("-")
            expression = expression[1:]
        fr_num = ""
        frac_nums=[]
        for e in expression:
            if e =="+" or e =="-":
                op.append(e)                
                frac_nums.append(fr_num)
                fr_num=""
            else:
                fr_num+= e
        frac_nums.append(fr_num)
        return op,frac_nums
    
    def get_all_deno(self,flist):
        #returns all denominators from the list of fraction numbers
        return [int(f.split("/")[1]) for f in flist]
    
    def find_lcm(self,frac_nums):
        denominators = self.get_all_deno(frac_nums)
        max_deno = max(denominators)
        mult  = max_deno#this variable will hold the lowest common multiplier
        mult_into_count =1#increment mult by multiplying max_deno * mult_into_count = mult
        #increment mult 
        lcm_find =True
        print(denominators)
        while lcm_find:
            count =0
            for d in denominators:
                # print("**",max_deno)
                if max_deno%d != 0:
                    max_deno = mult * mult_into_count
                    break
                count +=1
            if count == len(frac_nums):
                 lcm_find = False
            else:
                mult_into_count +=1
        return max_deno
    
    def find_hcf(self,num1,num2):
        #using Eucledian algorithm to find the HCF of given two numbers NUM1 and NUM2  
        small_num = abs(min(num1,num2) )
        large_num = abs(max(num1,num2))
        divisor =small_num
        divident =large_num
        print("****",divident,divisor)
        while divident%divisor != 0:
            mod = divident%divisor
            divident = divisor
            divisor = mod 
        return divisor
    
    def calc_fraction(self,ops,fnums,lcm):
        f_num_sum = 0
        for i in range(len(ops)):
            num = int(fnums[i].split("/")[0])
            deno = int(fnums[i].split("/")[1])
            lcm_div = lcm //deno
            exp_sum = num*lcm_div
            if ops[i] == "-":
                f_num_sum -= exp_sum
            else: # addition
                f_num_sum += exp_sum
        if f_num_sum == 0:
            lcm =1
        # print("^^^^^^^^^^^",self.find_hcf(f_num_sum,lcm),f_num_sum,lcm)
        hcf_frac_num_den = self.find_hcf(f_num_sum,lcm)#hcf of resulting fraction numerator and denominator
        #making the resulting fraction irreducible
        f_num_sum = f_num_sum//hcf_frac_num_den
        lcm = lcm//hcf_frac_num_den
        return str(f_num_sum)+"/"+str(lcm)
    def fractionAddition(self, expression: str) -> str:
        operations,frac_nums = self.op_frac_list(expression)
        lcm = self.find_lcm(frac_nums)
        return self.calc_fraction(operations,frac_nums,lcm)
if __name__ == "__main__":
    s=Solution()
    expression = "-1/2+1/3"
    # print(s.fractionAddition(expression))
    expression = "-1/3+8/7-13/15+2/8"
    print(s.fractionAddition(expression))
    expression = "1/2+1/2-99/7+34/87-45/7"
    print(s.fractionAddition(expression))
    expression = "1/2+1/2-99/789+34/8743-45/77"
    print(s.fractionAddition(expression))

