import numpy as np
import pandas as pd
from scipy.special import logsumexp
from hmmlearn import hmm

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

#Backward Algorithm

def backwardalgo():
  global store_backward
  revsequence = sequence[::-1]
  clast = np.ones_like(a.shape[0])
  store_backward = np.zeros((sequence.shape[0],2))
  for i in revsequence[0:len(revsequence)-1]:
    ctemp = [sum(clast*a[j,:]*b[:,i]) for j in range(a.shape[0])]
    clast = ctemp
    cc = sum(pi*b[:,revsequence[-1]]*clast)
    store_backward[np.where(sequence ==i), :] = pi*b[:,revsequence[-1]]*clast
  store_backward[0:sequence.shape[0]-1,:] = store_backward[1:sequence.shape[0]+1,:]
  store_backward[-1,:] = np.ones_like(a.shape[0])
  print("The calculation matrix is:\n", store_backward.T)
  print("The probability is ",cc)


backwardalgo()