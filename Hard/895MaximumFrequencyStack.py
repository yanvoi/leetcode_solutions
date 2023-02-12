class FreqStack:

    def __init__(self):
        self.frequencies_stacks = defaultdict(list)
        self.frequency = defaultdict(int)
        self.max_frequency = 0


    def push(self, val: int) -> None:
        self.frequency[val] += 1
        self.max_frequency = max(self.max_frequency, self.frequency[val])

        self.frequencies_stacks[self.frequency[val]].append(val)


    def pop(self) -> int:
        val = self.frequencies_stacks[self.max_frequency].pop()
        self.frequency[val] -= 1

        if self.frequencies_stacks[self.max_frequency] == []:
            self.max_frequency -= 1

        return val


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
