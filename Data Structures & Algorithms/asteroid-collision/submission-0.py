class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        stack = []
        for a in asteroids:
            keep = True
            while stack and stack[-1] > 0 and a < 0:
                # check magnitudes (abs)
                if stack[-1] > -a:
                    # a dies and nothing is appended
                    keep = False
                    break
                elif stack[-1] == -a:
                    stack.pop()
                    keep = False
                    break
                else:
                    # less than, clear to keep popping
                    stack.pop()
            if keep:
                stack.append(a)
        return stack