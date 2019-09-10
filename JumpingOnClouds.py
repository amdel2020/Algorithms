def jumpingOnClouds(c):
    jumps = 0
    i = 0

    while True:
        if i >= len(c)-1:
            break
        if i+1 == len(c)-1:
            i += 1
        elif i+2 == len(c)-1:
            i += 2
        elif c[i+2] == 0:
            i += 2
        else:
            i += 1

        jumps += 1

    return jumps

c = [0,0,1,0,0,1,0]
print(jumpingOnClouds(c))
