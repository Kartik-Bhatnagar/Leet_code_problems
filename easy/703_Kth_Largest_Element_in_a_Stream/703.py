#[703. Easy ]Kth Largest Element in a Stream
#Author : Kartik Bhatnagar
#Date 12/08/2024

class KthLargest:

    def __init__(self, k: int, nums: list[int]):
        self.k =k
        self.nums = sorted(nums)
        # self.kth_largest  = nums[-self.k]

    def add(self, val: int) -> int:
        self.nums.append(val)
        self.nums = sorted(self.nums)
        return self.nums[-self.k]

        
if __name__ == "__main__":
    k1=3
    nums1=[4, 5, 8, 2]
    vals1=[3,5,10,9,4]#it will be individual values but here will use the list
    obj1 = KthLargest(k1,nums1)
    for val in vals1:
        print(obj1.add(val))

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)