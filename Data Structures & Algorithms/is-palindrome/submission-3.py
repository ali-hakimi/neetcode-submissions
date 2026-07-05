class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        print(s)
        i = 0
        j = len(s) - 1

        while i < j:
            while i < j and not self.isalphaNum(s[i]):
                i += 1
            while i < j and not self.isalphaNum(s[j]):
                j -= 1
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True
    
    def isalphaNum(self, c):
                return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9')) 
        