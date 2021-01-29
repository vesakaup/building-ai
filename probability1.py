import numpy as np

def generate(p1):
    # change this so that it generates 10000 random zeros and ones
    # where the probability of one is p1
    seq = np.random.choice([0, 1], size=(10000,), p=[1-p1, p1])
    
    return seq

def count(seq):
    # insert code to return the number of occurrences of 11111 in the sequence
    n = 0
    for i in range(len(seq)-1):
        if sum(seq[i:i+5])==5:
            n += 1
    return n
    

def main(p1):
    seq = generate(p1)
    return count(seq)

print(main(2/3))
