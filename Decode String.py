class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for char in s:
            if char != "]":
                stack.append(char)
            else:
                curr = ""
                while stack and stack[-1] != "[":
                    curr = stack.pop() + curr
                stack.pop()
                num = ""
                while stack and stack[-1].isdigit():
                    num = stack.pop() + num
                stack.append(curr * int(num))
        return "".join(stack)
# Example 1:
# Input: s = "3[a]2[bc]"
# Output: "aaabcbc"
        
# Example 2:
# Input: s = "3[a2[c]]"
# Output: "accaccacc"
        
# Example 3:
# Input: s = "2[abc]3[cd]ef"
# Output: "abcabccdcdcdef"
