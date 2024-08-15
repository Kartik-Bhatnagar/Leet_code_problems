#URL : https://leetcode.com/problems/lemonade-change/
#[Easy] [860] 
#Title: [Lemonade Change]
#Author: Kartik Bhatnagar
#Date : 2024-08-15 (YYYY-MM-DD)
class Solution:
    def lemonadeChange(self, bills: list[int]) -> bool:
        #maintain a count of $5 at given point of time
        five,ten=0,0
        for bill in bills:
            if bill == 5:
                five += 1
            else:
                if bill == 10:
                    ten +=1                                       
                    five -= 1                    
                else: #bill is 20
                    if ten <1:#no $10 note is there 
                        five -=3
                    else:#aleast 1 $10 is there
                        ten-=1
                        five-=1
                if five <0: #if through out the logic we dont't have sufficient $5 then will return false
                        return False  
        return True
               
                
                


if __name__ == "__main__":
    s= Solution()
    bills = [5,5,5,10,20]
    print(s.lemonadeChange(bills))
    bills = [5,5,10,10,20]
    print(s.lemonadeChange(bills))