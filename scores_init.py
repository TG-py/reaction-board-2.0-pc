import pickle

with open('scores.pk', 'wb') as scoresFile:
    pickle.dump([], scoresFile)