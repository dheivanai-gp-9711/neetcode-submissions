class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        currTank=0
        totalTank=0
        i=0
        start=0
        for i in range(len(gas)):
            diff = gas[i] - cost[i]
            currTank+=diff
            totalTank+=diff
            if currTank <0:
                currTank=0
                start=i+1
        return start if totalTank>=0 else -1