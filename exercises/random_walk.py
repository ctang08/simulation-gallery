import random
import numpy as np
import matplotlib.pyplot as plt

def flip(p):
   return random.random() < p

def random_walk(n, p):
    position = 0
    for i in range(n):
        if flip(p):
            position += 1
        else:
            position -= 1
    return position

fig1 = plt.figure(1)

x = []
y = []
for i in range(1000):
    x.append(i)
    sum = 0
    for j in range(100):
        sum += abs(random_walk(i, 0.5))
    y.append(sum/100)
plt.scatter(x, y, label="Random")

x = np.linspace(0, 1000, 1000)
y = np.sqrt(x)
plt.plot(x, y, label=f"sqrt(x)")

plt.title("Random Walk Simulation")
plt.xlabel("n")
plt.ylabel("pos")
plt.legend() 

fig2 = plt.figure(2)

x = []
y = []
for i in range(1000):
    x.append(i)
    sum = 0
    for j in range(100):
        sum += abs(random_walk(i, 0.9))
    y.append(sum/100)
plt.scatter(x, y, label="Biased walk (p = 0.9)")

m, b = np.polyfit(x, y, 1)
x = np.linspace(0, 1000, 1000)
y = m*x+b
plt.plot(x, y, label=f"{m:.2f}x + {b:.2f}")

plt.title("Random Walk Simulation")
plt.xlabel("n")
plt.ylabel("pos")
plt.legend() 
plt.show()