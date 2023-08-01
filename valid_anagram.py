"""Description: Given two strings s and t, return true if t is an anagram of s, and false otherwise.
                An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
                typically using all the original letters exactly once.
"""
#code
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        keep_my_word = list(s)
        for i in t:
            if i in keep_my_word:
                keep_my_word.remove(i)
            else:
                return False
        if keep_my_word == []:
            return True
        else:
            return False