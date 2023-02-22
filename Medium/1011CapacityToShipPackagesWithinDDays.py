# Optimized with binary search
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        left, right = max(weights), sum(weights)

        while left < right:
            cur_days, cur_weight, mid = 1, 0, (left + right) // 2

            for weight in weights:
                if cur_weight + weight > mid:
                    cur_weight = 0
                    cur_days += 1

                cur_weight += weight

            if cur_days > days:
                left = mid + 1
            else:
                right = mid

        return left

      
# First Attempt - Not Optimized but intuitive
# class Solution:
#     def shipWithinDays(self, weights: List[int], days: int) -> int:

#         capacity = max(weights)
#         while True:
#             cur_days, cur_weight = 1, 0
#             for weight in weights:
#                 if cur_weight + weight > capacity:
#                     cur_weight = weight
#                     cur_days += 1
#                 else:
#                     cur_weight += weight

#             if cur_days <= days:
#                 break

#             capacity += 1

#         return capacity
      
