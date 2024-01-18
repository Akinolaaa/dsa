class Solution:

    # alot better solution
    def multiply(self, num1: str, num2: str) -> str:
        if (num1 == "0" or num2 == "0"): return "0"

        sol = [0] * (len(num1) + len(num2))
        num2 = num2[::-1]
        num1 = num1[::-1]
        for i in range(len(num2)):
            for j in range(len(num1)):
                mul = int(num1[j]) * int(num2[i])
                sol[i + j] += mul
                sol[i + j + 1] += (sol[i + j] // 10)
                sol[i + j] = sol[i + j] % 10
        
        sol = sol[::-1]
        start = 0
        while(sol[start] == 0):
            start += 1
        return "".join([str(i) for i in sol[start:]])
    

    # very shabby solution from me
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        sol = [0] * ((len(num1) + len(num2)) * 3)
        num2 = num2[::-1]
        for i in range(len(num1)):
            num2 += "0"
        num1 = num1[::-1]
        for i in range(len(num2)):
            num1 += "0"

        mulCarry = 0
        addCarry = 0
        for i in range(len(num2)):
            for j in range(len(num1)):
                mul = int(num1[j]) * int(num2[i])
                positionVal = (mul + mulCarry) % 10
                mulCarry = (mul + mulCarry) // 10

                add = sol[i + j] + positionVal + addCarry
                sol[i + j] = add % 10
                addCarry = add // 10

        sol = sol[::-1]
        start = 0
        while sol[start] == 0:
            start += 1
        return "".join([str(i) for i in sol[start:]])
