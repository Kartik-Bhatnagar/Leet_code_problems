class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if len(digits) < 1:
            return []
        result_lis = []
        dial_pad = {"2": ["a", "b", "c"],
                    "3": ["d", "e", "f"],
                    "4": ["g", "h", "i"],
                    "5": ["j", "k", "l"],
                    "6": ["m", "n", "o"],
                    "7": ["p", "q", "r", "s"],
                    "8": ["t", "u", "v"],
                    "9": ["w", "x", "y", "z"]}

        def letter_comb(temp_lis: list, next_index: int):
            if len(temp_lis) == len(digits):
                result_lis.append("".join(temp_lis))
                return True
            for item in dial_pad[digits[next_index]]:
                letter_comb(temp_lis+[item], next_index+1)
            return True
        for root_ele in dial_pad[digits[0]]:
            letter_comb([root_ele], 1)

        return result_lis


s1 = Solution()
inp = "527845"
print(s1.letterCombinations(inp))
