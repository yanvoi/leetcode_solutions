class Node:
    def __init__(self, num):
        self.parent = num
        self.descendants = set()
        self.locked = False
        self.locked_by = -1


class LockingTree:

    def __init__(self, parent: List[int]):
        self.nodes = [Node(num) for num in parent]

        leafs = [True] * len(parent)
        for num in parent:
            if num != -1: leafs[num] = False

        # go up the tree from every leaf and update descendants of each node
        for node, val in enumerate(leafs):
            if val:
                root = node
                p = parent[root]
                while p != -1:
                    self.nodes[p].descendants |= self.nodes[root].descendants
                    self.nodes[p].descendants.add(root)
                    p, root = self.nodes[p].parent, p


    def lock(self, num: int, user: int) -> bool:
        if self.nodes[num].locked:
            return False

        self.nodes[num].locked = True
        self.nodes[num].locked_by = user

        return True

    def unlock(self, num: int, user: int) -> bool:

        if not self.nodes[num].locked or self.nodes[num].locked_by != user:
            return False

        self.nodes[num].locked = False
        self.nodes[num].locked_by = -1

        return True
        

    def upgrade(self, num: int, user: int) -> bool:

        # the first condition
        if self.nodes[num].locked: return False

        # the second condition
        if not any(self.nodes[node].locked for node in self.nodes[num].descendants): return False

        # the third condition
        node = self.nodes[num].parent
        while node != -1:
            if self.nodes[node].locked: return False
            node = self.nodes[node].parent

        # actual updating of a node
        self.nodes[num].locked = True
        self.nodes[num].locked_by = user

        for node in self.nodes[num].descendants:
            self.nodes[node].locked = False
            self.nodes[node].locked_by = -1

        return True


# Your LockingTree object will be instantiated and called as such:
# obj = LockingTree(parent)
# param_1 = obj.lock(num,user)
# param_2 = obj.unlock(num,user)
# param_3 = obj.upgrade(num,user)
