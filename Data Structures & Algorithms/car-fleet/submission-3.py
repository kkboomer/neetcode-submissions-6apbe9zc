class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        res = 0
        cars = [[p, s] for p, s in zip(position, speed)]
        cars.sort(key=lambda x: x[0])
        max_time = 0
        for i in range(len(cars)-1, -1, -1):
            time = (target - cars[i][0]) / cars[i][1]
            if time > max_time:
                res += 1
                max_time = max(time, max_time)
        return res