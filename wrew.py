import math
import matplotlib.pyplot as plt
import numpy as np

coincidence = """6
key (x): 2
value (y:)3
key (x): 6
value (y:)7
key (x): 4
value (y:)7
key (x): 4
value (y:)8
key (x): 
[[2, 3], [6, 7], [4, 7], [4, 8]]
1.0
2.25
>>> """
print(6)
data = []
while(True):
    key = (input("key (x): " ))
    try:
        key = int(key)
    except:
        break
    value = int(input("value (y:)" ))
    data.append([key,value])
print(data)
global m
global b
global x
global y
def multiply(list1,list2):
    output = []
    for i in range(len(list1)):
        output.append(list1[i]*list2[i])
    return(output)
def mean(liste):
    totalsum = 0
    for i in liste:
        totalsum+=i
    output = totalsum/len(liste)
    return(output)
def factorize(liste):
    newlist = []
    for i in liste:
        newlist.append(i*i)
    return(newlist)

def linearRegression(data):
    global x
    global y
    global m
    global b
    exes = []
    whys = []
    for i in data:
        exes.append(i[0])
        whys.append(i[1])
    
    
    exesto2 = factorize(exes)
    m = (mean(exes)*mean(whys)-(mean(multiply(exes,whys))))/((mean(exes)*mean(exes)-mean(exesto2)))
    print(m)
    b = mean(whys)-m*mean(exes)
    print(b)
    x = np.linspace(-10, 10, 100)
    y = m*x+b
    return(y)
graph = linearRegression(data)
fig = plt.figure(figsize = (10, 5))
# Create the plot
plt.plot(x, y)
 
# Show the plot
plt.show()

mean_y = mean(whys)
def calculateRsquared (m,b,exes,whys,mean_y):
    e_of_mean = 0
    e_of_m =0
    for i in range(len(exes)):
        x_value = exes[i]
        eSquared = (mean_y - y_value)**2
        e_of_mean += eSquared
        sloped_y = m*x_value+b
        e_to_2 = (sloped_y - y_value)**2
        e_of_m+=e_to_2
        return(1 - ( e_of_m / e_of_mean))
r2 = calculateRsquared(m,b,exes,whys,mean_y)
print(r2)
        
                   
        











