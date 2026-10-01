class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # keep shifting the goal to the starting index 0

        goal = len(nums) - 1

        for i in range(len(nums) - 1, -1, -1):

            if i + nums[i] >= goal:
                goal = i
        

        return True if goal == 0 else False












        