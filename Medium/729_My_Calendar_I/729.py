#URL : https://leetcode.com/problems/my-calendar-i/?envType=daily-question&envId=2024-09-26
#[Medium] [729] 
#Title: [My Calendar I]
#Author: Kartik Bhatnagar
#Date : 2024-09-26 (YYYY-MM-DD)

class MyCalendar:

    def __init__(self):
        # self.time_frame =[False for i in range(49)]
        self.calendar =set()

    def book(self, start: int, end: int) -> bool:
        booking = True
        for l,h in self.calendar:
            if not((start < l and end <= l) or (start >=h and end >h)):
                booking = False
                break
        if(booking):
            self.calendar.add((start,end))
        return booking

        # count =0
        # # print(start,end,self.time_frame)
        # for i in range(start,end):
        #     if self.time_frame[i]:
        #         break
        #     count+=1
        # if count == (end-start):
        #     #add event to calendar
        #     for i in range(start,end):
        #         self.time_frame[i]=True
        #     return True
        # else:
        #     return False
            


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)



if __name__ == "__main__":
    s=Solution()
