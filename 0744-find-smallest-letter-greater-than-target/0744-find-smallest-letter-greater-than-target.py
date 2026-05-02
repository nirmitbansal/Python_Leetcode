class Solution:
    def nextGreatestLetter(self, letters, target):
        return next(c for c in letters if c > target) if any(c > target for c in letters) else letters[0]