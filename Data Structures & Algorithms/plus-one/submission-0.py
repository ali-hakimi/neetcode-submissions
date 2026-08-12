class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if len(digits) == 0:
            return [1]
        car = 0
        for i in range(len(digits) - 1, -1, -1):
            temp = digits[i] + car
            if i == len(digits) - 1:
                temp += 1
            digits[i] = temp % 10
            car = temp // 10
        if car:
            digits.insert(0, car)
        return digits