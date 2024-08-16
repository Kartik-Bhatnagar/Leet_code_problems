class Solution:
    def finalPositionOfSnake(self, n: int, commands: list[str]) -> int:
        cur_r,cur_c =(0,0)#intital position
        for com in commands:
            if com =="UP":
                cur_r,cur_c = cur_r-1,cur_c
            elif com =="DOWN":
                cur_r,cur_c = cur_r+1,cur_c
            elif com =="RIGHT":
                cur_r,cur_c = cur_r,cur_c+1
            else :#"LEFT"
                cur_r,cur_c = cur_r,cur_c-1
        # print(cur_r,cur_c)
        return ((cur_r*n)+cur_c)
    
if __name__ =="__main__":
    s = Solution()
    n1 = 2
    commands1 = ["RIGHT","DOWN"]
    print(s.finalPositionOfSnake(n1,commands1))
    n2 = 3
    commands2 = ["DOWN","RIGHT","UP"]
    print(s.finalPositionOfSnake(n2,commands2))