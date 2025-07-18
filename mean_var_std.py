import numpy as np
a = np.array([1,2,3,4,5,6,7,8,9])

def calculate(a):
    if len(a) != 9:
        raise ValueError("List must contain at least nine numbers.")
    
    ar = np.array(a).reshape(3,3)
    print(ar)

    calculations = {
        
  "mean": [list(np.mean(ar,axis=0)),list(np.mean(ar,axis=1)),float(np.mean(ar))],
  "variance": [list(np.var(ar,axis=0)),list(np.var(ar,axis=1)),float(np.var(ar))],
  "standard deviation": [list(np.std(ar,axis=0)),list(np.std(ar,axis=1)),float(np.std(ar))],
  "max": [list(np.max(ar,axis=0)),list(np.max(ar,axis=1)),int(np.max(ar))],
  "min": [list(np.min(ar,axis=0)),list(np.min(ar,axis=1)),int(np.min(ar))],
  "sum": [list(np.sum(ar,axis=0)),list(np.sum(ar,axis=1)),int(np.sum(ar))]
   }

    return calculations 

    
calculate([1,2,3,4,5,6,7,8,9])
