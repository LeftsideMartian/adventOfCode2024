def getPageDetails(filename) -> tuple[list[str], list[str]]:
    pageOrderRules = []
    pagesToUpdate = []
    with open(filename, "r") as f:
        content = f.read().split("\n")
        blankLineIndex = content.index("")

        pageOrderRules = content[0:blankLineIndex]
        pagesToUpdate = content[blankLineIndex + 1:]

    return (pageOrderRules, pagesToUpdate)

def mapPageOrderRulesToDict(pageOrderRules):
    #For a rule X|Y, pageX must be printed before pageY
    dict = {}

    for rule in pageOrderRules:
        splitRule = rule.split("|")
        pageX = int(splitRule[0])
        pageY = int(splitRule[1])
        if pageX not in dict:
            dict[pageX] = [pageY]
        else:
            dict[pageX].append(pageY)

    return dict

def isUpdateValid(rulesDict, pages: list[int]):
    for i in range(1, len(pages)):
        previousPages = pages[0:i]
        rulesForThisPage = rulesDict.get(pages[i])
        if rulesForThisPage is None:
            continue
        for page in previousPages:
            if page in rulesForThisPage:
                return False

    return True

def filterUpdatesForCorrectness(rulesDict, updates):
    correctUpdates = []
    incorrectUpdates = []

    for update in updates:
        pages = list(map(int, update.split(",")))
        if isUpdateValid(rulesDict, pages):
            correctUpdates.append(pages)
        else:
            incorrectUpdates.append(pages)

    return (correctUpdates, incorrectUpdates)

def getSumOfMiddlePagesForCorrectUpdates(pages):
    sum = 0
    for update in pages:
        sum += update[len(update) // 2]
            
    return sum

def fixUpdateOrdering(rulesDict, update):
    newUpdate = update.copy()

    for i in range(1, len(newUpdate)):
        previousPages = newUpdate[0:i]
        rulesForThisPage = rulesDict.get(newUpdate[i])
        if rulesForThisPage is None:
            continue
        for j in range(len(previousPages)):
            if previousPages[j] in rulesForThisPage:
                temp = newUpdate[j]
                newUpdate[j] = newUpdate[i]
                newUpdate[i] = temp

    return newUpdate

def getSumOfMiddlePagesForIncorrectUpdates(rulesDict, updates):
    sum = 0

    for update in updates:
        newUpdate = fixUpdateOrdering(rulesDict, update)
        sum += newUpdate[len(newUpdate) // 2]

    return sum


myInput = "day5/day5.txt"
testInput = "day5/day5TestInput.txt"

pageOrderRules, pagesToUpdate = getPageDetails(myInput)

rulesDict = mapPageOrderRulesToDict(pageOrderRules)
correctUpdates, incorrectUpdates = filterUpdatesForCorrectness(rulesDict, pagesToUpdate)
correctPagesSum = getSumOfMiddlePagesForCorrectUpdates(correctUpdates)
incorrectPagesSum = getSumOfMiddlePagesForIncorrectUpdates(rulesDict, incorrectUpdates)

print(f"Part 1: Sum of middle page numbers for correct updates is {correctPagesSum}")
print(f"Part 2: Sum of middle page numbers for corrected incorrect updates is {incorrectPagesSum}")