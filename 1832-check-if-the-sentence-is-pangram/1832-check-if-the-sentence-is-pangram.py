class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        for char in alpha:
          if char in sentence:
            continue
          else:
            return False
        return True