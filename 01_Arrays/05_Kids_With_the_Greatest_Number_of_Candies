class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies = max(candies)
        n = len(candies)

        for i in range(n):
            if candies[i] + extraCandies >= max_candies:
                candies[i] = True
            else:
                candies[i] = False

        return candies

