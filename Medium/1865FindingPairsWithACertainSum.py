# O(n) space
# let n == len(nums1) && m == len(num2)
class FindSumPairs:

    # O(max(n, m)) time
    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1_count = Counter(nums1)
        self.nums2 = nums2
        self.nums2_count = Counter(nums2)

    # O(1) time
    def add(self, index: int, val: int) -> None:
        self.nums2_count[self.nums2[index]] -= 1
        self.nums2[index] += val
        self.nums2_count[self.nums2[index]] += 1

    # O(n) time
    def count(self, tot: int) -> int:
        return sum(count * self.nums2_count[tot - num] for num, count in self.nums1_count.items() if tot - num in self.nums2_count)

# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)
