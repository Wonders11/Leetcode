class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        ans_array = [0]
        change = 0
        for i in range(len(gain)):
            change += gain[i]
            ans_array.append(change)

        ans_array.sort()
    
        return ans_array[len(gain)]