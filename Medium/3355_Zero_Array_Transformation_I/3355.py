#URL : https://leetcode.com/problems/zero-array-transformation-i/description/?envType=daily-question&envId=2025-05-19
#[Medium] [3355] 
#Title: [Zero Array Transformation I]
#Author: Kartik Bhatnagar
#Date : 2025-05-20 (YYYY-MM-DD)
class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        #USING Diifernce array
        def update_diff_arr(d_arr,start,end):
            #updates the differnce array according to the query
            d_arr[start] = d_arr[start]-1
            d_arr[end+1] = d_arr[end+1] +1
            return d_arr

        def diff_arr_converter(diff_arr):
            #converts the differnce array to actual array and it finds any postive value it will give false result
            if diff_arr[0] >0 :
                return False
            actual_arr = [diff_arr[0]]
            for i in range(1,len(diff_arr)-1):
                ele = actual_arr[i-1]+diff_arr[i]
                if ele >0 :
                    return False
                actual_arr.append(ele)
            # return actual_arr
            return True

        #creating initial differnce array
        diff_arr =  [nums[0]] #intilising first element of difference array
        for i in range(1,len(nums)):
            diff_arr.append(nums[i]-nums[i-1])
        diff_arr.append(0) #adding a dummy element at last
        # print(diff_arr)

        for q in queries:
            diff_arr = update_diff_arr(diff_arr,q[0],q[1])
        
        # print(diff_arr)
        
        # resul_arr = diff_arr_converter(diff_arr)
        # for r in resul_arr:
        #     if r>0:
        #         return False
        # return True

        return diff_arr_converter(diff_arr)


        #____TLE 660/668____________
        #  num_counts ={i : 0 for i in range(len(nums))} #sum of each occurance of the possible subsets
        #  for q in queries:
        #     for n in range(q[0],q[1]+1):
        #         # print(n)
        #         num_counts[n] = num_counts[n] +1
        # #  print(num_counts)
        #  for i in range(len(nums)):
        #     # print(nums[i],num_counts[i],nums[i] < num_counts[i])
        #     if nums[i] > num_counts[i]:
        #         return False
        #  return True
            
        
if __name__ == "__main__":
    s=Solution()
