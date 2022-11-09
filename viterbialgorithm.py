import numpy as np
from scipy.special import logsumexp

#Initiating transition probability matrix
a = np.array([[0.7,0.3],
              [0.5,0.5]])

#Initiating Emission probability matrix
b = np.array([[0.6,0.1,0.3],
              [0.1,0.7,0.2]])

#pi matrix for initiating alpha values
pi = np.array([1,0])

states = ["CP","IP"]
cola = 0
icedtea = 1
lemon = 2
observations = ["Cola","Icedtea","Lemon"]
sequence = np.array([lemon,icedtea,cola])


# Viterbi Algorithm


def viterbi():
    store = np.zeros((sequence.shape[0],a.shape[0]))
    track = np.zeros((sequence.shape[0], a.shape[0]), 'int')
    store[0, :] = pi * b[:,sequence[0]] #calculating first column
    for t in range(1, sequence.shape[0]): #recursion
        for s2 in range(2):
            for s1 in range(2):
                score = store[t-1, s1] * a[s1, s2] * b[s2, sequence[t]] 
                if score > store[t, s2]: #checking max condition
                    store[t, s2] = score
                    track[t, s2] = s1
    follow = []
    follow.append(np.argmax(store[sequence.shape[0]-1,:]))
    for i in range(sequence.shape[0]-1, 0, -1):
        follow.append(track[i, follow[-1]])
    final=[states[i] for i in list(reversed(follow))]
    print("The calculation matrix is (columwise forward) \n", store.T)
    print("The probability is",max(store[sequence.shape[0]-1,:]))
    print("Optimal sequence:",final)

viterbi()