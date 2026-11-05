class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        res = 1
        cars = sorted(zip(position, speed))
        max_position, max_speed = cars[-1]
        for i in range(len(cars)-2, -1, -1):
            p, s = cars[i]
            if max_speed * (target - p) > s * (target - max_position):
                res += 1
                max_speed , max_position = s, p        
        return res