import pickle
import math

def otherPlayerComparison(score):
    with open('scores.pk', 'rb') as scoresFile:
        scores = pickle.load(scoresFile)
    total = 0
    highest = 0
    beatenScores = []
    place = 1
    for i in scores:
        total += i
        if highest < i:
            highest = i
        if i <= score:
            beatenScores.append(i)
        else:
            place += 1
    avg = total/len(scores)
    playerCount = len(scores)+1
    percentageBeaten = 100 - math.floor(((len(beatenScores)/len(scores))*100)-0.0000001)
    scores.append(score)
    with open('scores.pk', 'wb') as scoresFile:
        pickle.dump(scores, scoresFile)
    return percentageBeaten, place, highest, total, avg, playerCount