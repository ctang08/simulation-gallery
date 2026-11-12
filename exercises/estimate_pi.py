"""Project 2: Approximating pi

Author		Christopher Tang
Date		03/02/2026

This program provides a line demonstration of the Monte Carlo method for approximating pi. It generates random points in a unit square and counts how many fall within a quarter circle inscribed within that square. The ratio of points inside the quarter circle to the total number of points is used to approximate pi.

AI Usage: 	AI wasn't used for this project.

Sources: 	
https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.PillowWriter.html
https://www.youtube.com/watch?v=bNbN9yoEOdU
"""

import random
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import PillowWriter

fig, ax = plt.subplots()
ax.set_xlim(0, 1) 
ax.set_ylim(0, 1) 
plt.legend()

"""
point
    Generates a random point (x, y) where x and y are uniformly distributed between 0 and 1.

    Args: None.

    Returns: An ordered pair (x, y) representing the coordinates of the random point.
"""
def point():
    x = random.random()
    y = random.random()
    return x, y

"""
scatter(red, blue)
    Plots a random point (x, y) on the graph. If the point is inside the quarter circle, it is plotted in red; otherwise, it is plotted in blue.

    Args: 
        red: An integer representing the number of points that have fallen inside the quarter circle so far.
        blue: An integer representing the number of points that have fallen outside the quarter circle so far.
    
    Returns: 
        A boolean that is True if the point is inside the quarter circle and False if it is outside.
"""
def scatter(red, blue):
    x, y = point()
    if x**2 + y**2 < 1:
        plt.scatter(x, y, color="red", label="Inside Circle")
        return True
    else:
        plt.scatter(x, y, color="blue", label="Outside Circle")
        return False

writer = PillowWriter(fps=15)

# Draw the quarter circle boundary
theta = np.linspace(0, np.pi/2, 100)
x_circle = np.cos(theta)
y_circle = np.sin(theta)
plt.plot(x_circle, y_circle, color="black") 

with writer.saving(fig, "pi_approximation.gif", 100):
    red = 0
    blue = 0

    for i in range(1, 1000):

        #Update the counts of red and blue points
        for j in range(10):
            if scatter(red, blue):
                red += 1
            else:
                blue += 1
        
        #Calculate the approximation of pi as 4 * the ratio of red points to total points
        ratio = 4*red/(red + blue)
        plt.title(f"Approximation of pi: {ratio}")
        writer.grab_frame()
