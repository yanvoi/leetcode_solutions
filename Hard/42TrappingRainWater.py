class Solution:
    def trap(self, height: List[int]) -> int:
        
        highest_to_left = [0 for _ in range(len(height))]
        highest_to_right = [0 for _ in range(len(height))]

        cur_max = 0
        for i in range(1, len(height)):
            highest_to_left[i] = cur_max = max(cur_max, height[i-1])

        cur_max = 0
        for i in range(len(height) - 2, -1, -1):
            highest_to_right[i] = cur_max = max(cur_max, height[i+1])

        answer = 0
        for i, num in enumerate(height):
            trapped_water = min(highest_to_left[i], highest_to_right[i]) - num
            if trapped_water > 0:
                answer += trapped_water

        return answer
