from typing import List


class Solution:
    def romanToInt(self, s: str) -> int:
        singles = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        doubles = {
            "IV": 4,
            "IX": 9,
            "XL": 40,
            "XC": 90,
            "CD": 400,
            "CM": 900,
        }

        if len(s) == 0:
            return 0
        if len(s) == 1:
            return singles[s] or 0

        values: List[int] = []
        values.append(singles[s[0]])

        # start from index 1
        for i in range(1, len(s)):
            double = s[i - 1 : i + 1]
            double_val = doubles.get(double)
            single = s[i]
            # purposefully not a .get() so that this errors out upon passing
            # invalid characters
            single_val = singles[single]

            if double_val:
                values.pop()  # remove the prior entry
                values.append(double_val)
            else:
                values.append(single_val)

        return sum(values)
