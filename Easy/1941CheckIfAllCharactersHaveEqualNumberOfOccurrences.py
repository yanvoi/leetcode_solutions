class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        def all_equal(arr):
            return all(arr[i] == arr[i + 1] for i in range(len(arr) - 1))

        return all_equal(list(collections.Counter(s).values()))
