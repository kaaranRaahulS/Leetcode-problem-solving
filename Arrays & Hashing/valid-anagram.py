class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        arr = [0] * 26
        if(len(s) != len(t)):
            return False
        for i in range(len(s)):
            arr[ord(s[i]) - ord('a')] = 1
            arr[ord(t[i]) - ord('a')] = 0
        for i in arr:
            if(arr[i] != 0):
                return True
        return False
valid_anagram = Solution().isAnagram
print(valid_anagram("anagram", "nagaram"))

#space complexity is O(1) as the Array Size is fixed 
#Time complexity is O(n) as the size of the variable isn't fixed. 