class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        res = []
        
        def dfs(i, cur):
            if len(cur) == len(digits):
                print(len(cur), len(digits))
                res.append(cur)
                return
            if len(cur) > len(digits):
                return 
            chars = digitToChar[digits[i]]

            for c in chars:
                cur += c
                dfs(i + 1, cur)
                cur = cur[:-1]

        dfs(0, "")
        return res