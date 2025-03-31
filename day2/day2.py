def getReports(fileName):
    reports = []

    with open(fileName, "r") as f:
        for line in f:
            reports.append(line.strip("\n").split(" "))
        f.close()

    return reports

def isReportSafe(report):
    isAscending = True
    isDescending = True

    for i in range(1, len(report)):
        thisItem = int(report[i])
        lastItem = int(report[i-1])
        itemDistance = abs(thisItem - lastItem)

        if isAscending and lastItem >= thisItem:
            isAscending = False
        if isDescending and lastItem <= thisItem:
            isDescending = False
        if itemDistance < 1 or itemDistance > 3:
            return False
        if not isAscending and not isDescending:
            return False
    
    return True

def part1(reports):
    numOfSafeReports = 0
    unsafeReports = []

    for report in reports:
        if isReportSafe(report):
            numOfSafeReports += 1
        else:
            unsafeReports.append(report)
    
    return (unsafeReports, numOfSafeReports)

def part2(reports):
    numOfSafeReports = 0

    for report in reports:
        for i in range(len(report)):
            newReport = report.copy()
            newReport.pop(i)
            if isReportSafe(newReport):
                numOfSafeReports += 1
                break

    return numOfSafeReports

myInput = "day2/day2.txt"
testInput = "day2/day2TestInput.txt"

reports = getReports(myInput)

unsafeReports, safeReports = part1(reports)
print(f"Part 1: Number of safe reports is {safeReports}")

safeReports += part2(unsafeReports)
print(f"Part 2: Number of safe reports is {safeReports}")
