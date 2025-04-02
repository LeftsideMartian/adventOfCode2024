import copy
class labMap:
    _mapFromFile: list[list[str]]
    _map: list[list[str]]
    _defaultRoute: list[list[int]]
    _numOfMovesForDefaultRoute: int
    _visitedPositions: list[list[int]]
    _initialGuardPosition: tuple[int, int]
    _guardsPosition: tuple[int, int]
    _guardsLastPosition: tuple[int, int]
    _guardDirection: str
    _lastFourPositions: list[tuple[int, int]]
    _numOfDistinctPositions: int
    _numOfPlacesToPutObstacle: int
    _height: int
    _width: int


    def __init__(self, filename):
        map = []
        with open(filename, "r") as f:
            for line in f.read().split("\n"):
                map.append(list(line))
        
        self._mapFromFile = copy.deepcopy(map)
        self._map = copy.deepcopy(map)
        self._numOfDistinctPositions = 0
        self._numOfPlacesToPutObstacle = 0
        self._numOfMovesForDefaultRoute = 0
        self._height = len(self._mapFromFile)
        self._width = len(self._mapFromFile[0])
        self._initialGuardPosition = self.findGuard()
        self._guardsPosition = self._initialGuardPosition
        self._guardsLastPosition = self._initialGuardPosition
        self._guardDirection = "u" #Cycle between u,r,d,l to keep track of direction
        self._visitedPositions = [[0]*self._width for _ in range(self._height)]


    def findGuard(self):
        for y in range(self._height):
            for x in range(self._width):
                if self._map[y][x] in "<^>v":
                    return (y, x)

        return (0, 0)   


    def calculateNumOfDistinctPositions(self):
        #Until guard hits the edge of the map
        while True:
            y, x = self._guardsPosition
            #Is guard at the edge of the map
            if y == 0 or y == self._height - 1 or x == 0 or x == self._width - 1:
                break
            
            self.moveGuard()
            self._numOfMovesForDefaultRoute += 1
        
        self._defaultRoute = copy.deepcopy(self._visitedPositions)


    def moveGuard(self):
        y, x = self._guardsPosition
        self._guardsLastPosition = (y, x)

        if self._visitedPositions[y][x] == 0:
            self._visitedPositions[y][x] = 1
            self._numOfDistinctPositions += 1
        
        self._map[y][x] = "."

        match self._guardDirection:
            case "u":
                for i in range(y, -1, -1):
                    #If we hit the edge
                    if i == 0:
                        self._map[i][x] = "^"
                        self._guardsPosition = (i, x)
                        return

                    #If we find an obstacle
                    if self._map[i - 1][x] == "#":
                        self._guardsPosition = (i, x)
                        self._map[i][x] = ">"
                        self._guardDirection = "r"
                        return

                    self.updateVisitedPositions(i, x)
            case "r":
                for i in range(x, self._width):
                    #If we hit the edge
                    if i == self._width - 1:
                        self._map[y][i] = ">"
                        self._guardsPosition = (y, i)
                        return

                    #If we find an obstacle
                    if self._map[y][i + 1] == "#":
                        self._map[y][i] = "v"
                        self._guardsPosition = (y, i)
                        #Change its direction
                        self._guardDirection = "d"
                        return
                    
                    self.updateVisitedPositions(y, i)
            case "d":
                for i in range(y, self._height):
                    #If we hit the edge
                    if i == self._height - 1:
                        self._map[i][x] = "v"
                        self._guardsPosition = (i, x)
                        return

                    #If we find an obstacle
                    if self._map[i + 1][x] == "#":
                        self._map[i][x] = "<"
                        self._guardsPosition = (i, x)
                        #Change its direction
                        self._guardDirection = "l"
                        return
                    
                    self.updateVisitedPositions(i, x)
            case "l":
                for i in range(x, -1, -1):
                    #If we hit the edge
                    if i == 0:
                        self._map[y][i] = "<"
                        self._guardsPosition = (y, i)
                        return

                    #If we find an obstacle
                    if self._map[y][i - 1] == "#":
                        self._map[y][i] = "^"
                        self._guardsPosition = (y, i)
                        #Change its direction
                        self._guardDirection = "u"
                        return
                    
                    self.updateVisitedPositions(y, i)


    def updateVisitedPositions(self, y, x):
        if self._visitedPositions[y][x] == 0:
            self._visitedPositions[y][x] = 1
            self._numOfDistinctPositions += 1


    def resetMap(self):
        self._map = copy.deepcopy(self._mapFromFile) #Reset map to default file
        self._guardDirection = "u" #Cycle between u,r,d,l to keep track of direction
        self._guardsPosition = self._initialGuardPosition
        self._visitedPositions = [[0]*self._width for _ in range(self._height)]

    
    def isMapLooping(self):
        numOfMoves = 0
        while True:
            y, x = self._guardsPosition

            if numOfMoves >= self._numOfMovesForDefaultRoute * 4:
                return True

            #If the guard lands against an obstacle that its visited before, its in a loop
            #If the guards position is the same as last turn, it was in a corner
            # if self._visitedPositions[y][x] == 1 and self._guardsPosition != self._guardsLastPosition:
            #     return True
            
            if y == 0 or y == self._height - 1 or x == 0 or x == self._width - 1:
                return False

            self.moveGuard()
            numOfMoves += 1


    def calculateNumberOfPlacesToPutObstacle(self):
        for y in range(self._height):
            for x in range(self._width):
                if self._defaultRoute[y][x] == 1 and (y, x) != self._initialGuardPosition:
                    #Reset map to file
                    self.resetMap()

                    #Put an obstacle at (y,x)
                    self._map[y][x] = "#"

                    print((y, x))

                    if self.isMapLooping():
                        self._numOfPlacesToPutObstacle += 1


    def printPart1Answer(self):
        print(f"Part 1: Num of distinct positions is {self._numOfDistinctPositions}")


    def printPart2Answer(self):
        print(f"Part 2: Num of ways to get guard stuck in a loop is {self._numOfPlacesToPutObstacle}")


    def __str__(self):
        string = ""
        for row in self._map:
            string += f"{"".join(char for char in row)}\n"
        
        return string.strip("\n")


myInput = "day6.txt"
testInput = "day6TestInput.txt"

map = labMap(myInput)
map.calculateNumOfDistinctPositions()
map.printPart1Answer()
map.calculateNumberOfPlacesToPutObstacle()
map.printPart2Answer()