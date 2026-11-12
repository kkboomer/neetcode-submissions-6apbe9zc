class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        top = -1
        for a in asteroids:
            keep = True
            while top >=0 and asteroids[top] > 0 and a < 0:
                if asteroids[top] > -a:
                    # a dies and nothing
                    keep = False
                    break
                elif asteroids[top] == -a:
                    top -= 1
                    keep = False
                    break
                else:
                    top -= 1
            if keep:
                top +=1
                asteroids[top] = a
        return asteroids[:top + 1]