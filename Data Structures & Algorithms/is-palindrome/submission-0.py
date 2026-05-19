class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_string = ""
        for word in s:
            if word.isalnum():
                new_string += word.lower()
        return new_string[::-1] == new_string
