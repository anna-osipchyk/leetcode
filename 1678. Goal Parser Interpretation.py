class Solution:
    def interpret(self, command: str) -> str:
        return command.replace("()", "o").replace("(al)", "al")


ret = Solution().interpret("G()(al)")

# Runtime: 28 ms, faster than 85.08% of Python3 online submissions for Goal Parser Interpretation.
# Memory Usage: 14.1 MB, less than 89.69% of Python3 online submissions for Goal Parser Interpretation.
