class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = sorted(list(zip(position,speed)), key=lambda x: x[0])
        t = []
        for x , y in pairs:
            t.append((target - x) / y)
        fleet = 0
        prior = 0
        for time in t[::-1]:
            if time > prior:
                fleet += 1
                prior = time

        return fleet
