def mergesort(t):
    
    ### Error checking
    if type(t)!= type([]):
        raise TypeError('This function only takes a list of numbers as input.')
    if not all((isinstance(i, float) | isinstance(i, int))for i in t):
        raise TypeError('All the elements in the input list must be ints and/or floats.')
    
    ### Implementation
    if len(t) <=1: 
        return t
    
    left, right, result = [],[],[]
    
    for i in range(len(t)):
        if i < len(t)/2:
            left.append(t[i])
        else:
            right.append(t[i])
    left,right = mergesort(left),mergesort(right)

    while (len(left)!=0) & (len(right)!=0):
        if left[0] <= right[0]:
            result.append(left[0])
            left = left[1:]
        else:
            result.append(right[0])
            right = right[1:]
    while len(left) != 0:
        result.append(left[0])
        left = left[1:]
    while len(right) != 0:
        result.append(right[0])
        right = right[1:]
        
    return result
    
    
def quicksort(t):
    ### Error checking
    if type(t)!= type([]):
        raise TypeError('This function only takes a list of numbers as input.')
    if not all((isinstance(i, float) | isinstance(i, int))for i in t):
        raise TypeError('All the elements in the input list must be ints and/or floats.')
    
    ### Implementation
    if len(t) <= 1:
        return t
    (less,mid,more) = (list(),list(),list())
    pivot = t[-1]
    mid.append(pivot)
    for i in range(len(t)-1):
        if t[i] == pivot:
            mid.append(t[i])
        elif t[i] < pivot:
            less.append(t[i])
        else: # t[i] > pivot
            more.append(t[i])
    return quicksort(less) + mid + quicksort(more)
    

def bubblesort(t):
    ### Error checking
    if type(t)!= type([]):
        raise TypeError('This function only takes a list of numbers as input.')
    if not all((isinstance(i, float) | isinstance(i, int))for i in t):
        raise TypeError('All the elements in the input list must be ints and/or floats.')
    
    ### Implementation
    x = t[:]
    n = len(x)
    while True:
        swapped = False
        for i in range(1,n):
            if x[i-1] > x[i]:
                x[i-1], x[i] = x[i],x[i-1]
                swapped = True
        n = n-1
        if swapped == False:
            break
    return x
    
    
def run_timing_expt(t):
    
    import time
    start_time = time.time()
    mergesort(t)
    t_merge = time.time() - start_time
    
    start_time2 = time.time()
    quicksort(t)
    t_quick = time.time() - start_time2
    
    start_time3 = time.time()
    bubblesort(t)
    t_bubble = time.time() - start_time3
    
    return (t_merge, t_quick, t_bubble)
    
    
import numpy as np
n_list = [500,1000,1500,2000,2500]
ntrials = 20
merge_asc = np.zeros((len(n_list), ntrials))
quick_asc = np.zeros((len(n_list), ntrials))
bubble_asc = np.zeros((len(n_list), ntrials))

for i in range(len(n_list)):
    for j in range(ntrials):
        time_trial = run_timing_expt(list(range(n_list[i])))
        merge_asc[i,j], quick_asc[i,j], bubble_asc[i,j] = time_trial[0], time_trial[1], time_trial[2]
        
        
        
import matplotlib.pyplot as plt
%matplotlib inline

f = plt.figure(figsize=(8,8)) 

plt.errorbar(n_list, np.mean(merge_asc,axis=1), yerr=2*np.std(merge_asc, axis =1)/(ntrials**0.5), 
             fmt = "g-",label = 'Merge sort')
plt.errorbar(n_list, np.mean(quick_asc,axis=1), yerr=2*np.std(quick_asc, axis =1)/(ntrials**0.5), 
             fmt = "b-", label = 'Quick sort')
plt.errorbar(n_list, np.mean(bubble_asc,axis=1), yerr=2*np.std(bubble_asc, axis =1)/(ntrials**0.5), 
             fmt = 'r-', label = 'Bubble sort')

plt.title('Average runtime (20 trials) as a function of the input size n (with already-sorted lists)')
plt.xlabel('Input size')
plt.xticks(n_list)
plt.ylabel('Runtime (seconds)')
plt.legend(loc = 'upper left')
f.savefig("ascending.pdf")
