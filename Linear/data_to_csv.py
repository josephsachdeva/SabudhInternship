import numpy as np
import pandas as pd
def generateXData(n):
    '''#addition = np.add(randoms1, randoms2)
    #n=1000
    addition = np.zeros(n)
    #nr = 20
    for y in range(nr):
        randoms = [int(random.random()*1000) for i in range(n)] #generating uniform distributions
        for x in range(n):
            addition[x] = addition[x]+randoms[x] #adding two uniform distributions
    plt.hist(addition, bins=100)
    plt.show()'''
    
    #using numpy to generate Gaussian Random numbers
    X = np.random.random(size=n)*10
    return X

def generateEData(n):
    E = np.random.normal(loc=np.random.randint(n), size=n)/10
    
    return E

def calculate_y_from_e(X, E, c, m):
    Y = c + m*X + E
    print(max(X), min(X))
    print(max(E), min(E))
    return Y

def calculatecm():
    c = 5
    seed = 7
    m = np.random.seed()
    return c, m

n=50
X = generateXData(n)
E = generateEData(n)
c, m = calculatecm()
Y = calculate_y_from_e(X, E, c, m)
#data = X.append(Y)

df = pd.DataFrame({"X":X, "Y":Y})
df.to_csv("train.csv")