import numpy as np

deck = []
suit = ["C","D","H","S"]

for j in range(4):
    for i in range(1,13):
        deck.append((i,suit[j]))

np.random.shuffle(deck)
hand = [deck[i] for i in range(13)]
hand = sorted(hand, key=lambda element: (element[1],element[0]))

print hand
