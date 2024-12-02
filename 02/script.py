
with open("input.txt") as f:
    reports = f.readlines()

safe_reports = 0
safe_reports_with_dampener = 0


def isSafeReport(levels):

    isAscending = False
    isSafe = True

    for i, level in enumerate(levels[:-1]):
        this_level = level
        next_level = levels[i+1]
        delta = next_level-this_level

        if i == 0:
            if delta > 0:
                isAscending = True
            elif delta < 0:
                isAscending = False
            else:
                isSafe = False
                break

        if isAscending:
            if delta > 3:
                isSafe = False
                break
            elif delta < 1:
                isSafe = False
                break
        else:
            if delta < -3:
                isSafe = False
                break
            elif delta > -1:
                isSafe = False
                break
    return isSafe


def isAdaptedSafe(levels):
    isAdaptedSafe = False
    for i in range(len(levels)):
        adapted_levels = levels.copy()
        adapted_levels.pop(i)
        if isSafeReport(adapted_levels):
            isAdaptedSafe = True
            break
    return isAdaptedSafe


for report in reports:

    levels = report.split(" ")
    for ind, level in enumerate(levels):
        levels[ind] = int(level)

    isSafe = isSafeReport(levels)

    if isSafe:
        safe_reports += 1

    if not isSafe:
        if isAdaptedSafe(levels):
            isSafe = True

    if isSafe:
        safe_reports_with_dampener += 1


print(safe_reports)
print(safe_reports_with_dampener)
