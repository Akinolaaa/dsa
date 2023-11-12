# leetcode 134- Gas station
class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        if sum(gas) < sum(cost):
            return 0
        total = 0
        start = 0
        for i in range(len(cost)):
            total += gas[i] - cost[i]

            if(total < 0):
                total = 0
                start = i + 1
        return start

    # failed- passed 35/40 test cases :(
    def canCompleteCircuit2(self, gas: list[int], cost: list[int]) -> int:
        N = len(cost)

        for i in range(N):
            currGas = gas[i] - cost[i]
            start = i
            j = (i + 1) % N
            while currGas >= 0:
                currGas += gas[j] - cost[j]
                j = (j + 1) % N
                if currGas >= 0 and j == start:
                    return start
                if currGas == 0:
                    break
        return -1

    # failed- completed 30/40 test cases
    def canCompleteCircuit1(self, gas: list[int], cost: list[int]) -> int:
        start, N = 0, len(gas)

        # Find the station with the most gas you can start from
        maxGas = gas[0] - cost[0]
        for i in range(N):
            diff = gas[i] - cost[i]
            if diff > maxGas:
                maxGas = diff
                start = i

        if maxGas <= 0:
            return -1

        myGas = 0
        for j in range(start, start + N + 1):
            myGas += gas[j % N] - cost[j % N]
            print(j % N, myGas)
            if myGas < 0:
                return -1

        if myGas <= 0:
            return -1
        return start


gas, cost = [1, 2, 3, 4, 5], [3, 4, 5, 1, 2]
gas1, cost1 = [2, 3, 4], [3, 4, 3]
gas2, cost2 = [5, 8, 2, 8], [6, 5, 6, 6]


print(Solution().canCompleteCircuit(gas2, cost2))
