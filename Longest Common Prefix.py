class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""

        baza = strs[0]
        for i in range(len(baza)):
            for word in strs[1:]:
                if i == len(word) or word[i] != baza[i]:
                    return baza[0:i]
        return baza
# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".
# examle:
# Input: strs = ["flower","flow","flight"]
# Output: "fl"
