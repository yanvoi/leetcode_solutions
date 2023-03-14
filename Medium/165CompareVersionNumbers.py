class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:

        first, second = version1.split('.'), version2.split('.')
        first, second = first + ['0'] * (len(second) - len(first)), second + ['0'] * (len(first) - len(second))

        for v1, v2 in zip(first, second):
            if int(v1) > int(v2):
                return 1
            if int(v1) < int(v2):
                return -1

        return 0
