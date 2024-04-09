class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        mySentence = list(set(sentence)) # it will split the sentence into list
        mySentence.sort() # it will sort in the form of list
        return "".join(mySentence)==alphabet # will convert list into string
