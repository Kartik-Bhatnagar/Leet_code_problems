#URL : https://leetcode.com/problems/strange-printer/?envType=daily-question&envId=2024-08-21
#[Hard] [664] 
#Title: [Strange Printer]
#Author: Kartik Bhatnagar
#Date : 2024-08-21 (YYYY-MM-DD)


#timeLimit excedded
import time
class Solution:
    def strangePrinter(self, s: str) -> int:
        # using dfs approach, find the minimum from all possible ways in which we can print
        def dfs(current,print_done):     
            # print_done =['a','b']
            # current='c'
            print(current,print_done)
            start_char =False
            count_current = 0
            for char in s:
                # print(char,current,start_char)
                if start_char:
                    if char in print_done:
                        start_char =False
                        count_current +=1
                else:
                    if char == current:
                        start_char =True
            if start_char:
                count_current+=1
            print_done.append(current)
            rem_chars = [rc for rc in list(set(s)) if rc not in print_done]
            rem_count =0
            if len(rem_chars)!=0:
                rem_count = min([dfs(rm,print_done.copy()) for rm in rem_chars])
            return count_current+rem_count

        # cal prints for all possible starting points; adding 1 to the returned result for min of all dfs for a particular starting point
        min_tot_count =float("inf")
        for start_c in set(s):
            s_print_done =[start_c]
            rem_list = list(set(s)).copy()
            rem_list.remove(start_c)
            # print("**",rem_list,start_c)
            if len(rem_list)!=0:
                rem_count = min([dfs(rem_ele,s_print_done.copy()) for rem_ele in rem_list])
            else:
                rem_count =0
            # print(f"Start : {start_c} rem_Count: {rem_count}")
            tot_count = rem_count+1
            if tot_count < min_tot_count:
                min_tot_count = tot_count

        return min_tot_count



if __name__ == "__main__":
    sol=Solution()
    s='aaabbccbcab'
    print(f"result {sol.strangePrinter(s)}")
    s="abcdaabccbdabcb"
    print(sol.strangePrinter(s))
    s="aaabbb"
    print(sol.strangePrinter(s))
    s="aba"
    print(sol.strangePrinter(s))
    s="abababbb"
    print(sol.strangePrinter(s))
    s="aaeabbbcccddd"
    print(sol.strangePrinter(s))
    s="aaabbbcdecde"
    print(sol.strangePrinter(s))
    s="abcdefabcdefaa"
    print(sol.strangePrinter(s))
    s="aaaaa"
    print(sol.strangePrinter(s))
    t1=time.time()
    s="abcdefghijklmn"
    print(sol.strangePrinter(s))
    t2=time.time()
    print(f"Time taken : {t2-t1} sec")

