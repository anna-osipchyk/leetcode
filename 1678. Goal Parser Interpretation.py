class Solution:
    def interpret(self, command: str) -> str:
        dictionary = {
            "()": "o",
            "(al)": "al"
        }
        for key, value in dictionary.items():
            command = command.replace(key, value)
        return command


ret = Solution().interpret("G()(al)")

# Runtime: 39 ms, faster than 28.90% of Python3 online submissions for Goal Parser Interpretation.
# Memory Usage: 14.1 MB, less than 89.69% of Python3 online submissions for Goal Parser Interpretation.
