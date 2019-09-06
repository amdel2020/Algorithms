def breakingRecords(scores):
    lowscore = scores[0]
    highscore = scores[0]
    lowrecord = 0
    highrecord = 0

    for i in range(1, len(scores)):
        if scores[i] < lowscore:
            lowrecord += 1
            lowscore = scores[i]
        elif scores[i] > highscore:
            highrecord += 1
            highscore = scores[i]
    
    return [highrecord, lowrecord]

arr = [3,4,21,36,10,]