#URL : https://leetcode.com/problems/minimum-equal-sum-of-two-arrays-after-replacing-zeros/description/?envType=daily-question&envId=2025-05-10
#[Medium] [2918] 
#Title: [Minimum Equal Sum of Two Arrays After Replacing Zeros]
#Author: Kartik Bhatnagar
#Date : 2025-05-10 (YYYY-MM-DD)
class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        sums = dict()
        sums[1] = sum(nums1)
        sums[2] = sum(nums2)
        zero_cnt1= nums1.count(0)
        zero_cnt2= nums2.count(0)
        mins_sum = min(sums,key=sums.get)
        if (zero_cnt1 == 0 and zero_cnt2 ==0) :
            if sums[1] != sums[2]:
            #if no zero occurance is there in any array and the sums of both arrays are also not equal
                return -1
            else :
                #both are array sum are equal
                return sums[1]
        #if the array with minimum sum has 0 zero's then we return -1
        if zero_cnt1 == 0:
            if mins_sum ==1:
                return -1
            if sums[2]+zero_cnt2 > sums[1]:
                #if in the first array the count of 0 is zero 
                #and second array has more zero count if replacing all those zero 
                #in the second array with 1 will still exceed the sum greater than array1
                return -1
            #at this point , minimum sum is with second array
            return  sums[1]
        if zero_cnt2 == 0 :
            if mins_sum ==2:
                return -1
            if sums[1]+zero_cnt1 > sums[2]:
                return -1
            #at this point , minimum sum is with first array
            return sums[2]
       
       #if both the array has occurance zero elements
        
        return max(sums[1] +zero_cnt1, sums[2] +zero_cnt2)
if __name__ == "__main__":
    s=Solution()
