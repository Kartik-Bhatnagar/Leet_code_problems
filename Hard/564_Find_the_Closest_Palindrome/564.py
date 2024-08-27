#URL : https://leetcode.com/problems/find-the-closest-palindrome/?envType=daily-question&envId=2024-08-24
#[Hard] [564] 
#Title: [Find the Closest Palindrome]
#Author: Kartik Bhatnagar
#Date : 2024-08-24 (YYYY-MM-DD)
class Solution:
    def nearestPalindromic(self, n: str) -> str:        
           #the n is of even length
        
        if len(n)%2 ==0:
            mid = (len(n)//2)
            mid_ele = int(n[len(n)//2-1])
            first_half = n[:mid-1]#excluding mid element; it will be added for all 3 cases seperately
            if mid_ele !=0 and mid_ele != 9:
                #mid is in the range 1 to 8 
                obtained_nos =[] #all palindrom from case 1, 2, 3               
                c1_half = first_half+str(mid_ele-1)
                if c1_half =="0":
                    obtained_nos.append(9)
                else:
                    obtained_nos.append(int(c1_half+c1_half[::-1]))
                c2_half =  first_half+str(mid_ele)
                c3_half = first_half+str(mid_ele+1)
                # print(c1_half,c2_half,c3_half)               
                
                obtained_nos.append(int(c2_half+c2_half[::-1]))
                obtained_nos.append(int(c3_half+c3_half[::-1]))
                # print(obtained_nos)
                                
            elif mid_ele == 0:
                full_first_half = int(first_half+str(mid_ele))-1
                obtained_nos=[]
                if len(str(full_first_half)) == mid:
                    c1_half = str(full_first_half)
                    obtained_nos.append(int(c1_half+c1_half[::-1]))
                else: 
                    #it means the result length will reduce by 1
                    obtained_nos.append(int("9"*((len(n))-1)))
                c2_half =  first_half+str(mid_ele)
                c3_half = first_half+str(mid_ele+1)
                obtained_nos.append(int(c2_half+c2_half[::-1]))
                obtained_nos.append(int(c3_half+c3_half[::-1]))
            else:
                #mid_ele is 9
                c1_half = first_half+str(mid_ele-1)
                c2_half =  first_half+str(mid_ele)
                # print(c1_half,c2_half,c3_half)
                obtained_nos =[] #all palindrom from case 1, 2
                obtained_nos.append(int(c1_half+c1_half[::-1]))
                obtained_nos.append(int(c2_half+c2_half[::-1]))

                full_first_half = int(first_half+str(mid_ele))+1
                if len(str(full_first_half)) == mid:
                    c3_half = str(full_first_half)
                    obtained_nos.append(int(c3_half+c3_half[::-1]))
                else: 
                    #it means the result length will increaed by 1
                    obtained_nos.append(int("1"+("0"*(len(n)-1))+"1"))

            
           
        else:
            #length of n is odd
            if len(n) ==1:
                if int(n) ==0:
                    return n
                return str(int(n)-1)
            mid = (len(n)//2)+1
            mid_ele = int(n[mid-1])
            first_half = n[:mid-1]#excluding mid element;
            rev_first_half =first_half[::-1]
            obtained_nos =[]
            if mid_ele != 0 and mid_ele != 9:
                #mid_ele is in range 1 to 8
                obtained_nos.append(first_half+str(mid_ele-1)+rev_first_half)
                obtained_nos.append(first_half+str(mid_ele)+rev_first_half)                
                obtained_nos.append(first_half+str(mid_ele+1)+rev_first_half)
            elif mid_ele == 0:
                full_first_half = int(first_half+str(mid_ele))-1
                if len(str(full_first_half)) == mid:
                    c1_half = str(full_first_half)
                    obtained_nos.append(int(c1_half+c1_half[::-1][1:]))
                else: 
                    #it means the result length will reduce by 1
                    obtained_nos.append(int("9"*((len(n))-1)))
                obtained_nos.append(first_half+str(mid_ele)+rev_first_half)                
                obtained_nos.append(first_half+str(mid_ele+1)+rev_first_half)
            else:
                #mid_ele is 9
                obtained_nos.append(first_half+str(mid_ele-1)+rev_first_half)
                obtained_nos.append(first_half+str(mid_ele)+rev_first_half)
                full_first_half = int(first_half+str(mid_ele))+1
                if len(str(full_first_half)) == mid:
                    c1_half = str(full_first_half)
                    obtained_nos.append(int(c1_half+c1_half[::-1][1:]))
                else: 
                    #it means the result length will increaed by 1
                    obtained_nos.append(int("1"+("0"*(len(n)-1))+"1"))    
            obtained_nos = [int(p) for p in obtained_nos]
        #common steps for all n 
        min_abs_diff=float("inf")
        
        for pali in obtained_nos:
            if pali != int(n):
                # print("++",min_abs_diff,pali)
                if abs(pali-int(n)) < min_abs_diff:
                    min_abs_diff = abs(pali-int(n))
                    min_pali = pali
        print(obtained_nos)
        return str(min_pali)
                

                







            
if __name__ == "__main__":
    s=Solution()
    nums=["297792","8627879812345678","10878786","123456789012","29792","862789812345678","1878786","12346789012","3","408"]
    # for n in nums:
    #     print(f"results for {n} : {s.nearestPalindromic(n)}")
    odd_nums=["100000000001","9999999","76278","18701","862787912345678","18781","1000001","1000002"]
    for n in odd_nums:
        print(f"results for {n} : {s.nearestPalindromic(n)}")
