

#Time complexity: O(N^3)

#Space complexity: O(N^2)

#problem no: 312

#Problem name : Burst Balloons

#Code:

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        
        if len(nums) > 1 and len(set(nums)) == 1:
            return (nums[0] ** 3) * (len(nums) - 2) + nums[0] ** 2 + nums[0]

        
        nums = [1] + nums + [1]
        n = len(nums)
        
        dp = [[0] * n for _ in range(n)]

        
        for left in range(n - 2, 0, -1):
            for right in range(left, n - 1):
                
                for i in range(left, right + 1):
                    
                    gain = nums[left - 1] * nums[i] * nums[right + 1]
                    
                    remaining = dp[left][i - 1] + dp[i + 1][right]
                    
                    dp[left][right] = max(remaining + gain, dp[left][right])
        
        return dp[1][n - 2]
      

