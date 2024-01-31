#time.time()
import numpy as np
import time

def checktick():
    M = 200
    timesfound = np.empty((M,)) #numpy array wide 200 values and not initialized
    for i in range(M):
        t1 =  time.time() # get timestamp from timer
        t2 = time.time() # get timestamp from timer
        while (t2 - t1) < 1e-16: # if zero then we are below clock granularity, retake timing
            t2 = time.time() # get timestamp from timer
        t1 = t2 # this is outside the loop
        timesfound[i] = t1 # record the time stamp
    minDelta = 1000000
    Delta = np.diff(timesfound) # it should be cast to int only when needed. it returns an array that calculates the differences btw consecutive elements of an array
    minDelta = Delta.min() #returns the smallest value in the array
    return minDelta

if __name__ == "__main__":
    for i in range(100):
        minDelta = checktick()
        print("Clock granularity: {:e}".format(minDelta))


#timer()
import numpy as np
from timeit import default_timer as timer

def checktick():
    M = 200
    timesfound = np.empty((M,)) #numpy array wide 200 values and not initialized
    for i in range(M):
        t1 =  timer() # get timestamp from timer
        t2 = timer() # get timestamp from timer
        while (t2 - t1) < 1e-16: # if zero then we are below clock granularity, retake timing
            t2 = timer() # get timestamp from timer
        t1 = t2 # this is outside the loop
        timesfound[i] = t1 # record the time stamp
    minDelta = 1000000
    Delta = np.diff(timesfound) # it should be cast to int only when needed. it returns an array that calculates the differences btw consecutive elements of an array
    minDelta = Delta.min() #returns the smallest value in the array
    return minDelta

if __name__ == "__main__":
    for i in range(100):
        minDelta = checktick()
        print("Clock granularity: {:e}".format(minDelta))


#time.time_ns()
import numpy as np
import time

def checktick():
    M = 200
    timesfound = np.empty((M,)) #numpy array wide 200 values and not initialized
    for i in range(M):
        t1 =  time.time_ns() # get timestamp from timer
        t2 = time.time_ns() # get timestamp from timer
        while (t2 - t1) < 1e-16: # if zero then we are below clock granularity, retake timing
            t2 = time.time_ns() # get timestamp from timer
        t1 = t2 # this is outside the loop
        timesfound[i] = t1 # record the time stamp
    minDelta = 1000000
    Delta = np.diff(timesfound) # it should be cast to int only when needed. it returns an array that calculates the differences btw consecutive elements of an array
    minDelta = Delta.min() #returns the smallest value in the array
    return minDelta

if __name__ == "__main__":
    for i in range(100):
        minDelta = checktick()*10**(-9)
        print("Clock granularity: {:e}".format(minDelta))
