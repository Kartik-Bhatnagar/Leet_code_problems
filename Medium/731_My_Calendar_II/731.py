#URL : https://leetcode.com/problems/my-calendar-ii/description/?envType=daily-question&envId=2024-09-27
#[Medium] [731] 
#Title: [My Calendar II]
#Author: Kartik Bhatnagar
#Date : 2024-09-27 (YYYY-MM-DD)

class MyCalendarTwo:

    def __init__(self):
        self.calendar =set()
        self.calendar_2 = set()

    def book(self, start: int, end: int) -> bool:
        booking = True
        overlap=set()
        for l,h in self.calendar:
            if not((start < l and end <= l) or (start >=h and end >h)):
                booking = False
                overlap.add((l,h))
        
        if(not booking):
            #first booking is filled
            booking_2 =True
            s,e = l ,h
            for l,h in self.calendar_2:
                if not((start < l and end <= l) or (start >=h and end >h)):
                    booking_2 = False
                    break
            if booking_2:
                #second booking will be done
                self.calendar.add((start,end))
                for s2,e2 in overlap:
                    overlap_time = (max(start,s2),min(end,e2))
                    print("@",self.calendar_2,start,end,s2,e2)
                    self.calendar_2.add(overlap_time)
                return True
            else:
                return False
        else:
            #FIRST booking is possible
            self.calendar.add((start,end))
            return booking
            
# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
if __name__ == "__main__":
    s=Solution()
