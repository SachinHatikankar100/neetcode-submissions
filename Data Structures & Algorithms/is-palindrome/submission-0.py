class Solution:
    def isPalindrome(self, s: str) -> bool:
        ans = "".join(char for char in s if char.isalnum())
        if ans.lower() == ans[::-1].lower():
            return True
        else: 
            return False
        