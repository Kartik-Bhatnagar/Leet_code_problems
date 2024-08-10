class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        per_list = []  # answer will get store here

        def perm(lis):
            if len(lis) == len(nums):
                per_list.append(lis)
                return True
            for i in nums:
                if i not in lis:
                    # print(lis, i, lis+[i])
                    perm(lis+[i])
            return True

        for num in nums:
            perm([num])
        return per_list


s1 = Solution()
print(s1.permute([2, 3, 4]))


def no_p(n):
    psum = 1
    while (n > 1):
        psum = (psum*n)
        n = n-1
    return (psum)


print(no_p(1))
