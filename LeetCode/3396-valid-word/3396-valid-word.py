class Solution(object):
    def isValid(self, word):
        """
        :type word: str
        :rtype: bool
        """

        vowels = 0
        consonants = 0
        vowelList = {'a', 'e', 'i', 'o', 'u'}
        length = len(word)

        if(length<3):
            return False

        for ch in word:
            if not ch.isalnum():
                return False

            if ch.isalpha():
                if ch.lower() in vowelList:
                    vowels += 1
                else:
                    consonants += 1

        return vowels > 0 and consonants > 0

        