import numpy as np

# data
X = np.array([[66, 5, 15, 2, 500], 
              [21, 3, 50, 1, 100], 
              [120, 15, 5, 2, 1200]])
y = np.array([250000, 60000, 525000])

# alternative sets of coefficient values
c = np.array([[3000, 200 , -50, 5000, 100], 
              [2000, -250, -100, 150, 250], 
              [3000, -100, -150, 0, 150]])   

def find_best(X, y, c):
    smallest_error = np.Inf
    best_index = -1
    i = 0
    for coeff in c:
        error = sum((y - X@coeff)**2) # sum of squared errors
        if error < smallest_error:
            smallest_error = error 
            best_index = i  
        i += 1
    print("the best set is set %d" % best_index)


find_best(X, y, c)
