#URL : https://leetcode.com/problems/push-dominoes/description/?envType=daily-question&envId=2025-05-02
#[Medium] [838] 
#Title: [Push Dominoes]
#Author: Kartik Bhatnagar
#Date : 2025-05-02 (YYYY-MM-DD)
class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        dom = [[0,0] for i in range(len(dominoes))] #this will store the effect of force on each domino, ind 1 force wrt to right force and ind 0 force wrt to left force
        count =0
        r_activated = False
        #keeping the effect of right force; moving from left most domino to right most
        for f in range(len(dominoes)):
            if dominoes[f]=="R":
                r_activated = True 
                count=0               
            elif dominoes[f]=="L":
                count=0
                r_activated = False
            if r_activated:
                count+=1
                dom[f][1] = count
        #keeping the effect of left force; moving from right most domino to left most
        l_activated = False
        count =0
        for f in range(-1,(len(dominoes)*-1)-1,-1):
            if dominoes[f]=="L":
                l_activated = True 
                count=0               
            elif dominoes[f]=="R":
                count=0
                l_activated = False
            if l_activated:
                count+=1
                dom[f][0] = count
        result =""
        for d in dom:
            if d[0] == d[1]:
                result +="."
            elif d[0] == 0 and d[1] >0 :
                result +="R"
            elif d[1] == 0 and d[0] >0:
                result +="L"
            else:#both are non zero values #which ever is the lowest the net efect will be of that
                if d[0] < d[1]:
                    result +="L"
                else:
                    result +="R"
        return result
        
            

        
if __name__ == "__main__":
    s=Solution()
