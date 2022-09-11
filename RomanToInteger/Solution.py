class Solution:
    # @param A : list of integers
    # @return an integer
    # convert roman numerals to integer
    def romanToInt(self, s: str) -> int:

        romanNumerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = 0
        print("The function has received the roman numeral \"" + s + "\" to convert a integer.")
        for i in range(len(s)):
            if i > 0 and romanNumerals[s[i]] > romanNumerals[s[i - 1]]:
                result += romanNumerals[s[i]] - 2 * romanNumerals[s[i - 1]]
            else:
                result += romanNumerals[s[i]]

        return result






if __name__ == '__main__':
    self = Solution()
    s = Solution.romanToInt(self,"III")
    s = Solution.romanToInt(self,"LVIII")
    s = Solution.romanToInt(self,"MCMXCIV")



