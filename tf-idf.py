import numpy as np
import math


text = '''Humpty Dumpty sat on a wall
Humpty Dumpty had a great fall
all the king's horses and all the king's men
couldn't put Humpty together again'''
def find_nearest_pair(data):
    data = np.array(data)
    N = len(data)
    dist = np.empty((N, N), dtype=np.float)
    for i in range(N):
        for j in range(N):
            d = 0
            for n in range(len(data[0])):
                d += abs(data[i][n] - data[j][n])
            dist[i][j] = d
            if d == 0:
                dist[i][j] = np.inf
     

    print(np.unravel_index(np.argmin(dist), dist.shape))           

    

def main(text):
    # tasks your code should perform:

    # 1. split the text into words, and get a list of unique words that appear in it
    # a short one-liner to separate the text into sentences (with words lower-cased to make words equal 
    # despite casing) can be done with 
    # docs = [line.lower().split() for line in text.split('\n')]

    docs = [line.split() for line in text.splitlines()]
    n = len(docs) 
    vocabulary = list(set(text.split())) 

    # 2. go over each unique word and calculate its term frequency, and its document frequency

    tf = {} # term frequency 
    df = {} # document frequency 
    for word in vocabulary: # tf and df score for every word
        tf[word] = [doc.count(word)/len(doc) for doc in docs] 
        df[word] = sum([word in doc for doc in docs])/n  

    # 3. after you have your term frequencies and document frequencies, go over each line in the text and 
    # calculate its TF-IDF representation, which will be a vector
    tfidf = []
    for doc_index, doc in enumerate(docs):
        score_list = []
        for word in vocabulary:
            score = tf[word][doc_index] * math.log(1/df[word],10)
            score_list.append(score)
        tfidf.append(score_list)
    # 4. after you have calculated the TF-IDF representations for each line in the text, you need to
    # calculate the distances between each line to find which are the closest.

    find_nearest_pair(tfidf)
main(text)
