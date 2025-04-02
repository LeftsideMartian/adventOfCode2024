def getEquations(filename):
    with open(filename, "r") as f:
        return f.read().split("\n")


def printEquations(equations):
    print("\n".join(equation for equation in equations))


def plusTimesRecursive(target, numbers, memo):
    #Check memo
    if str(numbers) in memo:
        return memo[str(numbers)]

    #Base cases
    if len(numbers) == 1:
        if target == numbers[0]:
            return 1
        else:
            return 0

    numOfOperatorCombinations = 0
    #+
    numOfOperatorCombinations += plusTimesRecursive(target, [numbers[0] + numbers[1]] + numbers[2:], memo)
    #x
    numOfOperatorCombinations += plusTimesRecursive(target, [numbers[0] * numbers[1]] + numbers[2:], memo)
    
    memo[str(numbers)] = numOfOperatorCombinations
    return numOfOperatorCombinations


def plusTimesConcatRecursive(target, numbers, memo):
    #Check memo
    if str(numbers) in memo:
        return memo[str(numbers)]

    #Base cases
    if len(numbers) == 1:
        if target == numbers[0]:
            return 1
        else:
            return 0

    numOfOperatorCombinations = 0
    #+
    numOfOperatorCombinations += plusTimesConcatRecursive(target, [numbers[0] + numbers[1]] + numbers[2:], memo)
    #x
    numOfOperatorCombinations += plusTimesConcatRecursive(target, [numbers[0] * numbers[1]] + numbers[2:], memo)
    #||
    numOfOperatorCombinations += plusTimesConcatRecursive(target, [int(str(numbers[0]) + str(numbers[1]))] + numbers[2:], memo)
    
    memo[str(numbers)] = numOfOperatorCombinations
    return numOfOperatorCombinations


def part1(equations):
    totalCalibrationResult = 0

    for equation in equations:
        splitEquation = equation.split(": ")
        target = int(splitEquation[0])
        numbers = list(map(int, splitEquation[1].split(" ")))
        memo = {}

        numOfOperatorCombinations = plusTimesRecursive(target, numbers, memo)

        if numOfOperatorCombinations >= 1:
            totalCalibrationResult += target

    return totalCalibrationResult


def part2(equations):
    totalCalibrationResult = 0

    for equation in equations:
        splitEquation = equation.split(": ")
        target = int(splitEquation[0])
        numbers = list(map(int, splitEquation[1].split(" ")))
        memo = {}

        numOfOperatorCombinations = plusTimesConcatRecursive(target, numbers, memo)

        if numOfOperatorCombinations >= 1:
            totalCalibrationResult += target

    return totalCalibrationResult
    


myInput = "day7.txt"
testInput = "day7TestInput.txt"

equations = getEquations(myInput)

part1CalibrationResult = part1(equations)
print(f"Part 1: Total calibration result of valid equations is {part1CalibrationResult}")

part2CalibrationResult = part2(equations)
print(f"Part 2: Total calibration result of valid equations is {part2CalibrationResult}")
