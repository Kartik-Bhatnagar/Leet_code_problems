#URL : https://leetcode.com/problems/2-keys-keyboard/description/?envType=daily-question&envId=2024-08-19
#[Medium] [650] 
#Title: [2 Keys Keyboard]
#Author: Kartik Bhatnagar
#Date : 2024-08-19 (YYYY-MM-DD)

#Time complexity : O(n^2)
#space complexity ; O(n)
class Solution:
    def minSteps(self, n: int) -> int:
        min_ops = [1000]*(n+1)#intialise each num <= n,with max possible operations
        #since  'A' one time is already initlised 
        min_ops[1]=0 #it will take 0 operations to reach n=1 i.e just A
        for i in range(2,n+1):
            for j in range(1,(i//2)+1): #we will take factors for num i from (1 to i//2) #becz we can paste i's direct factors to m number of times(only upto the half of i) to make 'A'*i
                if i%j == 0: #if j is the factor of i
                    #Here j is  i's factors (1 to half of i)                    
                    #minimum number of operations for a i index will be the minimum of all j's  total  operation. 
                    #for a given j the total operation will be : the number of operations of j + number of times j is to i (that many paste opertion will take place)
                    min_ops[i] = min(min_ops[i], (min_ops[j] + i//j))
        print(f"minimum operation for n = {n} : {min_ops}" )
        return min_ops[n]


if __name__ == "__main__":
    s=Solution()
    n=5
    print(s.minSteps(n))
    n=36
    print(s.minSteps(n))
    n=90
    print(s.minSteps(n))
