class Solution:
    def isPalindrome(self, s: str) -> bool:
        parsedStr = ''.join(char.lower() for char in s if char.isalnum())
        lp, rp = 0, len(parsedStr) -1

        while lp < rp:
            if not parsedStr[rp] == parsedStr[lp]:
                return False
            rp -= 1
            lp += 1

        return True
            