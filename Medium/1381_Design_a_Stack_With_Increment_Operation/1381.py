#URL : https://leetcode.com/problems/design-a-stack-with-increment-operation/description/?envType=daily-question&envId=2024-09-30
#[Medium] [1381] 
#Title: [Design a Stack With Increment Operation]
#Author: Kartik Bhatnagar
#Date : 2024-09-30 (YYYY-MM-DD)
class CustomStack:

    def __init__(self, maxSize: int):
       self.stack =[] 
       self.max_size =maxSize

    def push(self, x: int) -> None:
        if len(self.stack)< self.max_size:
            self.stack.append(x)

    def pop(self) -> int:
        if len(self.stack) >0:
            return self.stack.pop()
        else:
            return -1

    def increment(self, k: int, val: int) -> None:
        min_incr =min(k,len(self.stack))
        print(min_incr)
        def inc(x):
            if x < min_incr:
                return self.stack[x]+val
            else:
                return self.stack[x]
    
        self.stack = list(map(inc,[i for i in range(len(self.stack))])        )


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
if __name__ == "__main__":
    s=Solution()
