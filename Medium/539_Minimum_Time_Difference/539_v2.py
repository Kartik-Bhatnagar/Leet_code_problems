#URL : https://leetcode.com/problems/minimum-time-difference/description/?envType=daily-question&envId=2024-09-16
#[Medium] [539] 
#Title: [Minimum Time Difference]
#Author: Kartik Bhatnagar
#Date : 2024-09-16 (YYYY-MM-DD)
import time

class Solution:
    def findMinDifference(self, timePoints: list[str]) -> int:
        # mins since midnight
        def mins_from_mid(t):
            hr,mins = t.split(":")
            tot_mins = (int(hr)*60) + int(mins)
            return tot_mins
        mins_dic ={}
        def get_mins(t):
            if t not in mins_dic:
                mins =mins_from_mid(t)
                mins_dic[t]=mins_from_mid(t)
                return mins
            else:
                return mins_dic[t]
        # time_mins = [mins_from_mid(t) for t in timePoints]
        result =1441
        for i in range(len(timePoints)):
            for j in range(i+1,len(timePoints)):                
                #cal both clockwise and anticlockwise between two times
                t1,t2=get_mins(timePoints[i]),get_mins(timePoints[j])
                clock =abs(t1-t2)
                anti_clock = 1440 - clock
                result = min(min(clock,anti_clock),result)
            print(i)
        return result


if __name__ == "__main__":
    s=Solution()
    timePoints_a =[["23:59","00:00"],["00:00","23:59","00:00"],["00:00","12:00"],["23:30","00:10"],["00:00","12:00","23:59"],
                   ["02:45","11:15","18:30","23:55"],["00:00","12:34","23:59","03:21","16:45","07:30","20:15","22:22"]] 
    print(f"{[s.findMinDifference(tp) for tp in timePoints_a]}")
    with open("tc_data/one.txt","r") as r:
        tp=eval(r.read())
    t1 = time.time()
    min_t = s.findMinDifference(tp)
    t2 = time.time()
    print(f"TIME TAKEN : {t2-t1} sec")



