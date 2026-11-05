class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        res = []
        cars = [[p, s] for p, s in zip(position, speed)]
        cars.sort(key=lambda x: x[0])
        for c in cars:
            time = (target - c[0]) / c[1]
            while res and res[-1] <= time:
                res.pop()
            res.append(time)
        return len(res)