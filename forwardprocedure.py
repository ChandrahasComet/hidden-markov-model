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

#Forward Algorithm
def forwardalgo():
    global store_forward
    store_forward = np.zeros((sequence.shape[0],2))
    c1 = pi.T*b[:,sequence[0]]
    store_forward[0, :] =c1
    for i in sequence[1:]:
        ctemp = [sum(c1*a[:,j]) for j in range(a.shape[0])]
        c2 = ctemp*b[:,i]
        c1 = c2
        store_forward[np.where(sequence==1), :] = c1
        cp = sum(c1)
    
    print("The calculation matrix is:\n", store_forward.T)
    print("The probability is ",cp)

forwardalgo()