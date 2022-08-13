class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hash_map = dict()
        for i in range(len(nums)):
            if nums[i] in hash_map:
                hash_map[nums[i]].append(i)
            else:
                hash_map[nums[i]] = [i]
            
        for num in hash_map:
            if target - num in hash_map:
                if target - num == num:
                    if len(hash_map[num]) > 1:
                        return [hash_map[num][0], hash_map[num][1]]
                else:
                    return [hash_map[num][0], hash_map[target-num][0]]
        
        return False
        
