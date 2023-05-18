# GIVEN GRAPH IS ACYCLIC - OPTIMIZATION CONSIDERING THIS FACT
class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:

        answer = set(range(n))
        for _, destination in edges:
            if destination in answer: answer.remove(destination)

        return list(answer)

# before optimization - will work for non-acyclic graphs as well
# class Solution:
#     def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:

#         answer = set(range(n))
#         connected = defaultdict(list)
#         for source, destination in edges:
#             connected[source].append(destination)

#         for i in range(n):
#             q = collections.deque([i])
#             while q:
#                 node = q.popleft()
#                 if node not in answer:
#                     continue
#                 if node != i:
#                     answer.remove(node)

#                 for adj in connected[node]:
#                     q.append(adj)

#         return list(answer)
