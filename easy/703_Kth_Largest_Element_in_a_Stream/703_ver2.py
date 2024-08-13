#[703. Easy ]Kth Largest Element in a Stream
#Author : Kartik Bhatnagar
#Date 12/08/2024

class KthLargest:
    def binary_search_insert(self,v):
        if len(self.nums) ==0:
            self.nums.append(v)
            return
        #returns the nums list after inserting the v element in list with the correct ascending order
        def bs(lis):
            
            mid = len(lis)//2
            # print(v,mid,self.nums)
            if mid!=0:
                if v < lis[mid]:
                    bs(lis[:mid])
                elif v > lis[mid]:
                    bs(lis[mid:])
                else: #v == lis[mid] #the v is equal to the element in the mid, we need to insert the v element here
                    indx= self.nums.index(lis[mid])
                    self.nums.insert(indx,v)
                    return
            else:#v will be inserted either left or right of the elementwiht index mid
                
                if v < lis[mid]:
                    indx= self.nums.index(lis[mid])
                    self.nums.insert(indx,v)
                else:
                    # we must find the last index of common occuring element , when we are inserting element greater than lis(mid) element
                    last_indx=len(self.nums) -1 - self.nums[::-1].index(lis[mid]) 
                    # indx= self.nums.index(lis[mid])
                    self.nums.insert(last_indx+1,v)                
        bs(self.nums)


    def __init__(self, k: int, nums: list[int]):
        self.k =k
        self.nums = sorted(nums)
        # self.kth_largest  = nums[-self.k]

    def add(self, val: int) -> int:
        # self.nums.append(val)
        # self.nums = sorted(self.nums)
        # print("______________",val)
        self.binary_search_insert(val)
        # print(self.nums)
        return self.nums[-self.k]

        
if __name__ == "__main__":
    k1=3
    nums1=[4, 5, 8, 2]
    vals1=[3,5,10,9,4]#it will be individual values but here will use the list
    obj1 = KthLargest(k1,nums1)
    # for val in vals1:
    #     print(obj1.add(val))
    k2=1
    nums2=[]
    vals2=[-3,-2,-4,0,4]#it will be individual values but here will use the list
    obj2 = KthLargest(k2,nums2)
    # for val in vals2:
    #     print(obj2.add(val))
    
    k3=3
    nums3=[1,1,1,1]
    vals3=[1,1,3,3,3,4,4,4]#it will be individual values but here will use the list
    obj3 = KthLargest(k3,nums3)
    for val in vals3:
        print(obj3.add(val))#it will be individual values but here will use the list
    

    
       

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)