class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:

        keys, visited = [0], set()
        while keys:
            room = keys.pop()
            visited.add(room)
            for key in rooms[room]:
                if key not in visited: keys.append(key)

        return len(visited) == len(rooms)
