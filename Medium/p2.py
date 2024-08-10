class Solution:
    def maximumJumps(self, nums: list[int], target: int) -> int:
        tot_jumps = 0
        i =0
        #i_index =[i]
        for j in range(1,len(nums)):
            if (nums[j]-nums[i]) <= target and (nums[j]-nums[i]) >= (-1*target):
                i = j
                #i_index.append(i)
                tot_jumps +=1
       # print(nums,tot_jumps)        
        if tot_jumps == 0 :
            return -1        
        if  i != j:
            while( i != j and i>0):
                i -= 1
                tot_jumps -= 1
                if (nums[j]-nums[i]) <= target and (nums[j]-nums[i]) >= (-1*target):
                    i = j
                    tot_jumps +=1
        if tot_jumps == 0 or i != j :
            return -1
        else:
            return  tot_jumps
        
class Solution2:
    def maximumJumps(self, nums: list[int], target: int) -> int:
        tot_jumps = 0
        i =0
        i_index =[i]
        for j in range(1,len(nums)):
            if (nums[j]-nums[i]) <= target and (nums[j]-nums[i]) >= (-1*target):
                i = j
                i_index.append(i)
                tot_jumps +=1
       # print(nums,tot_jumps)     
        
        
        if tot_jumps == 0 :
            return -1        
        if  i != j:
            i_index_copy = i_index[:-1]
            #tot_jumps-=1
            print(i_index_copy," tot_jumps: ",tot_jumps)
            while( i != j and len(i_index_copy)>0):
                i = i_index_copy[-1]
                tot_jumps -= 1
                if (nums[j]-nums[i]) <= target and (nums[j]-nums[i]) >= (-1*target):
                    i = j
                    tot_jumps +=1
                    print("Matched"," tot_jumps : ",tot_jumps)
                i_index_copy = i_index_copy[:-1]    
        if tot_jumps == 0 or i != j :
            return -1
        else:
            return  tot_jumps    
            
s1 = Solution()
n=[1,3,6,4,1,2]
n=[1,0,2]
n=[0,2,1,3] #1 -1
t= 1      
#print(s1.maximumJumps(n,t))

s2 = Solution2()
n=[1,3,6,4,1,2]
n=[1,0,2] #1 1
#n=[0,2,1,3] #1 -1
n=[0,2,1,3] #1 -1
n=[1,0,2,3]#1 2
t= 1      
print(s2.maximumJumps(n,t))
