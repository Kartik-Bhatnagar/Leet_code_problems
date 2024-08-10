def find_alone_zero_indx(arr):
    alone=[]
    
    if len(arr)>1:
        if arr[0] != 1 and arr[1] == 1:
            alone.append(0)
        #print(arr[-1] != 1 and arr[-2] == 1,len(arr))    
        if arr[-1] != 1 and arr[-2] == 1:
            alone.append(len(arr)-1)   
        prev_num,prev2_num=-1,-1
        for cur_num_indx in range(len(nums)):
            #print(nums[cur_num_indx],prev_num,prev2_num)
            if nums[cur_num_indx] == 1 and prev_num != 1 and prev2_num == 1:
                alone.append(cur_num_indx-1)
            prev2_num = prev_num    
            prev_num = nums[cur_num_indx]
        
    return sorted(alone)
def find_cont_ones(arr,target_indx): #find the total number of  continous ones, previous and forward to the given index
    ones_size,ones_count ={},0
    for t in range(len(target_indx)):
        
        ones_count=0
        ones_size[target_indx[t]] = ones_count
        #print(arr[(target_indx[t]+1):])
        # further_check_nex = True
        for next_ele in arr[(target_indx[t]+1):]:
            if next_ele != 1 :#and further_check_nex:
                break
            else:
                print(t,"he1")
                ones_count += 1
        #print(max(0,(target_indx[t]-1)):0:-1])  
        
        # further_check_rev =True
        #print(arr[max(1,(target_indx[t]-1)):0:-1] , "+++", (target_indx[t]-1))
        for rev_ele in arr[max(0,(target_indx[t]-1))::-1]:#traversing back
            #print(t,"___",rev_ele,"___",arr[rev_ele])
            if rev_ele != 1:# and further_check_rev:
                # further_check_rev = False
                break
            else:
                print(t,"he2")
                ones_count += 1
        ones_size[target_indx[t]] = ones_count        
    return(ones_size)            

nums = [1,0,0,1,1,1,1,1,0,0,0,0,0,0,1,1,1,0,1,1,1,1,1,0,1,1,1,1,1,1,1,1,0,1,1,0,0,0,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,1,1,1,1,0,1,1]
#nums = [1,1,0,1]
indx = find_alone_zero_indx(nums)
print("Index ", indx)
print(find_cont_ones(nums,indx))
#print((nums[-2]))
ones_dic = find_cont_ones(nums,indx)
ones_dic = sorted(ones_dic.items(),key= lambda kv: kv[1],reverse=True)
if len(ones_dic)>0:
    ans = ones_dic[0][1]
elif nums.count(1) == len(nums):
    ans = len(nums) -1
else:
    print("h4")
    max_ones =0
    temp_one_count= 0
    for i in nums:
        
        if i==1:
            print("i: ,",i)
            temp_one_count += 1
            print(temp_one_count,"@@@@")
        else:
            temp_one_count = 0
    print(temp_one_count,max_ones)                
    if temp_one_count>max_ones:
        max_ones= temp_one_count
    ans= max_ones
print(ans)