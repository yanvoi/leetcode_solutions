class Solution:
    def filterRestaurants(self, restaurants: List[List[int]], veganFriendly: int, maxPrice: int, maxDistance: int) -> List[int]:
        return [attr[0] for attr in sorted([r for r in restaurants if ((veganFriendly and r[2]) or not veganFriendly) and r[3] <= maxPrice and r[4] <= maxDistance], key = lambda x: (-x[1], -x[0]))]
