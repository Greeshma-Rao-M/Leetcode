class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(curr):
            if len(curr) == len(nums):
                ans.append(curr[:])
                return

            for num in nums:
                if num not in curr:
                    curr.append(num)
                    backtrack(curr)
                    curr.pop()

        ans = []
        backtrack([])
        return ans

    def permute2(self, nums: List[int]) -> List[List[int]]:
        if len(nums)==1:
            return [nums]
        permutes = []
        for i, num in enumerate(nums):
            for comb in self.permute(nums[:i]+nums[i+1:]):
                permutes.append([num]+comb)
        return permutes
