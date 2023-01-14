class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:

        # we build a graph in which each node has a link to a smaller element in the same group
        # by doing so, we can follow the links and find the smallest character in each group

        self.union_find = dict()
        for c1, c2 in zip(s1, s2):
            self.__merge__(c1, c2)

        return ''.join([self.__get_smallest_in_group__(char) for char in baseStr])

    
    # merges two posssibly different groups into one
    def __merge__(self, c1, c2):
        root1 = self.__get_smallest_in_group__(c1)
        root2 = self.__get_smallest_in_group__(c2)

        if root1 > root2:
            self.union_find[root1] = root2
        else:
            self.union_find[root2] = root1

    
    # follows the link up to the smallest character
    def __get_smallest_in_group__(self, char):

        if char not in self.union_find:
            self.union_find[char] = char

        while char != self.union_find[char]:
            char = self.union_find[char]

        return char
