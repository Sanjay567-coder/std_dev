import math
 
def mean(values):
    return sum(values)/len(values)
    
def stanDev(values):
    length = len(values)
    m = mean(values)
    total_sum = 0
 
    for i in range(length):
        total_sum += (values[i]-m)**2
 
    return math.sqrt(total_sum/length)
 
x = [60,61,65,63,98,99,90,95,91,96]
 
stan_dev = stanDev(x)
 
print(stan_dev)
 #16.2160414405