def countApplesAndOranges(start, end, appleTree, orangeTree, apples, oranges):
    appleFallPos = []
    orangeFallPos = []
    for apple in apples:
        appleFallPos.append(appleTree + apple)
    for orange in oranges:
        orangeFallPos.append(orangeTree + orange)
    
    applecount = 0
    orangecount = 0
    for apple in appleFallPos:
        if apple >= start and apple <= end:
            applecount += 1
    for orange in orangeFallPos:
        if orange >= start and orange <= end:
            orangecount += 1
    
    print(applecount)
    print(orangecount)

start = 7
end = 11
appleTree = 5
orangeTree = 15
apples = [-2,2,1]
oranges = [5,-6]

countApplesAndOranges(start, end, appleTree, orangeTree, apples, oranges)