class Solution:
    def isValid(self, s: str) -> bool:
      stack = []
      cm = {'[':']','(':')','{':'}'}
      for i in s:
        if i in cm:
            stack.append(cm[i])
        elif not stack or i != stack.pop():
            return False
      return not stack
