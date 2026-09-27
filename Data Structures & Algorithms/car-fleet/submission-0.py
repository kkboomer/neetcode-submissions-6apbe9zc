class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [[p,(target - p) / s] for p, s in zip(position, speed)]
        cars.sort(reverse=True)
        res = []
        for c in cars:
            if not res or c[1] > res[-1][1]: 
                res.append(c)
        return len(res)
                