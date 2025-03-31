import re

def readMemory(filename):
    with open(filename, "r") as f:
        return f.read()


def getUncorruptedMemory(memory, validChars):
    uncorruptedMemory = ""

    for char in memory:
        if char in validChars:
            uncorruptedMemory += char

    return uncorruptedMemory


def getMulValue(instruction):
    functionInputs = instruction.removesuffix(")").removeprefix("mul(").split(",")
    return int(functionInputs[0]) * int(functionInputs[1])

def part1(memory):
    mulRegexString = r"((mul\()(\d{1,3}),(\d{1,3})\))"

    uncorruptedMemory = getUncorruptedMemory(memory, "mul(,)0123456789")

    instructions = re.split(mulRegexString, uncorruptedMemory, flags=re.MULTILINE)

    sum = 0

    for instruction in instructions:
        if re.match(mulRegexString , instruction) is not None:
            sum += getMulValue(instruction)
    
    return sum


def part2(memory):
    uncorruptedRegexString = r"((mul\()(\d{1,3}),(\d{1,3})\))|(don't\(\))|(do\(\))"
    mulRegexString = r"((mul\()(\d{1,3}),(\d{1,3})\))"
    doRegexString = r"do\(\)"
    dontRegexString = r"don't\(\)"

    uncorruptedMemory = getUncorruptedMemory(memory, "mul(,)0123456789dont'")
    instructions = re.split(uncorruptedRegexString, uncorruptedMemory, flags=re.MULTILINE)

    sum = 0
    doInstruction = True

    for instruction in instructions:
        if instruction is not None:
            if re.match(dontRegexString, instruction) is not None:
                doInstruction = False
            elif re.match(doRegexString, instruction) is not None:
                doInstruction = True
            elif doInstruction and re.match(mulRegexString, instruction) is not None:
                sum += getMulValue(instruction)
    
    return sum


myInput = "day3/day3.txt"
testInput = "day3/day3TestInput.txt"

memory = readMemory(myInput)

print(f"Part 1: Sum is {part1(memory)}")
print(f"Part 2: Sum is {part2(memory)}")