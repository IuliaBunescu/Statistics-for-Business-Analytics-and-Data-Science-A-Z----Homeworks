import math

def normal_distribution(mean, std_dev, x):
    
    y = 1/(std_dev * math.sqrt(2*math.pi))*math.e**(-1/2*((x-mean)/std_dev)**2)
   
    return y