class Solution:
    def romanToInt(self, s: str) -> int:
        number = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        total = 0

        for i in range(len(s) - 1):
            currentnumber = number[s[i]]
            nextnumber = number[s[i + 1]]

            if currentnumber < nextnumber:
                total = total - currentnumber
            else:
                total = total + currentnumber

        total = total + number[s[-1]]

        return total 