class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:

        return [[x^1 for x in reversed(img)] for img in image]

        """
        for img in image:
            img.reverse()
            # for conversion of 0 to 1 and vice versa we will be using XOR operation - ^ 
            # 0 ^ 1 = 1
            # 1 ^ 1 = 0
            # so from above observation, we need to XOR with 1
            for j in range(len(img)):
                img[j] ^= 1 
        return img
        """

        