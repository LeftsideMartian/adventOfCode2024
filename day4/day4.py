def readWordSearch(filename):
    wordSearch = []
    with open(filename, "r") as f:
        for line in f:
            wordSearch.append(list(line.strip("\n")))
    return wordSearch

def checkWordSearchInAllDirections(wordSearch, targetWord):
    wordCount = 0
    width = len(wordSearch)
    height = len(wordSearch[0])
    targetLength = len(targetWord)

    #i moves us vertically
    for i in range(width):
        #j moves us horizontally
        for j in range(height):
            #Check right
            if width - j >= targetLength:
                word = "".join(wordSearch[i][k] for k in range(j, j + targetLength))
                if word == targetWord:
                    wordCount += 1
            #Check left
            if j >= targetLength - 1:
                word = "".join(wordSearch[i][k] for k in range(j, j - targetLength, -1))
                if word == targetWord:
                    wordCount += 1
            #Check down
            if height - i >= targetLength:
                word = "".join(wordSearch[k][j] for k in range(i, i + targetLength))
                if word == targetWord:
                    wordCount += 1
            #Check up
            if i >= targetLength - 1:
                word = "".join(wordSearch[k][j] for k in range(i, i - targetLength, -1))
                if word == targetWord:
                    wordCount += 1
            #Check UL
            if i >= targetLength - 1 and j >= targetLength - 1:  
                word = "".join(wordSearch[i - k][j - k] for k in range(0, targetLength))
                if word == targetWord:
                    wordCount += 1
            #Check UR
            if i >= targetLength - 1 and width - j >= targetLength:
                word = "".join(wordSearch[i - k][j + k] for k in range(0, targetLength))
                if word == targetWord:
                    wordCount += 1
            #Check DL
            if height - i >= targetLength and j >= targetLength - 1:
                word = "".join(wordSearch[i + k][j - k] for k in range(0, targetLength))
                if word == targetWord:
                    wordCount += 1
            #Check DR
            if height - i >= targetLength and width - j >= targetLength:
                word = "".join(wordSearch[i + k][j + k] for k in range(0, targetLength))
                if word == targetWord:
                    wordCount += 1
    
    return wordCount

def checkWordSearchDiagonals(wordSearch, targetWord):
    wordCount = 0
    width = len(wordSearch)
    height = len(wordSearch[0])
    lengthOfBranch = len(targetWord) // 2

    #i moves us vertically
    for i in range(width):
        # Keeping track of the number of diagonal words we've found. If it is 2 at the end (there are two crossed words), we've found a match
        numOfBranchWords = 0

        #j moves us horizontally
        for j in range(height):
            numOfBranchWords = 0
            #Check UL direction
            if i >= lengthOfBranch and j >= lengthOfBranch:
                if i < height - 1 and j < width - 1 : 
                    word = "".join(wordSearch[i + k][j + k] for k in range(1, -2, -1))
                    if word == targetWord or word[::-1] == targetWord:
                        numOfBranchWords += 1
            #Check UR
            if i >= lengthOfBranch and j < width - 1:
                if i < height - 1 and j >= lengthOfBranch:
                    word = "".join(wordSearch[i + 1 - k][j - 1 + k] for k in range(0, 3))
                    if word == targetWord or word[::-1] == targetWord:
                        numOfBranchWords += 1
            
            if numOfBranchWords == 2:
                wordCount += 1

    return wordCount


myInput = "day4/day4.txt"
testInput = "day4/day4TestInput.txt"

wordSearch = readWordSearch(myInput)

targetWord1 = "XMAS"
print(f"Part 1: Num of XMAS words in word search is {checkWordSearchInAllDirections(wordSearch, targetWord1)}")

targetWord2 = "MAS"
print(f"Part 2: Num of X-MAS in the word search is {checkWordSearchDiagonals(wordSearch, targetWord2)}")