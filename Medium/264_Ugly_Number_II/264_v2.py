import time
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        uglynums =[1]
        index_of_2,index_of_3,index_of_5 = 0,0,0
        next_multiple_2,next_multiple_3,next_multiple_5 = 2,3,5
        for i in range(n-1):
            next_ugly_num = min(next_multiple_2,next_multiple_3,next_multiple_5)
            uglynums.append(next_ugly_num)
            if next_ugly_num == next_multiple_2:
                index_of_2 +=1
                next_multiple_2 = uglynums[index_of_2]*2
            if next_ugly_num == next_multiple_3:
                index_of_3 +=1
                next_multiple_3 =uglynums[index_of_3]*3
            if next_ugly_num == next_multiple_5:#multiple of 5
                index_of_5 += 1
                next_multiple_5 = uglynums[index_of_5]*5
        # print(uglynums)
        return uglynums[-1]
    
if __name__ == "__main__":
    s=Solution()
    n=11
    print(s.nthUglyNumber(n))
    n=1
    print(s.nthUglyNumber(n))
    t1= time.time()
    # n=201
    # print(s.nthUglyNumber(n))
    # t2=time.time()
    # print(f"Time taken : {t2-t1} sec")
    # t1= time.time()
    n=1690
    print(s.nthUglyNumber(n))
    t2=time.time()
    print(f"Time taken : {t2-t1} sec")
