"""Project 3: Expectation

Author		Christopher Tang
Date		03/16/2026

This program provides a line demonstration of expected value. It simulates rolling a six-sided die multiple times and calculates the running average of the outcomes. The program plots the running average against the number of rolls, showing how it converges to the expected value of 3.5 as more rolls are added.

AI Usage: 	AI wasn't used for this project.

Sources: 	
https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.PillowWriter.html
"""

import random
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import PillowWriter

fig, ax = plt.subplots()
ax.set_xlim(0, 1000) 
ax.set_ylim(0, 6) 
ax.set_xlabel("Roll number")
ax.set_ylabel("Running average")

"""
scatter
    Generates a random value between 1 and 6 to simulate rolling a six-sided die. It updates the running sum of the rolls and calculates the running average. The function then plots the running average against the number of rolls.

    Args: 
        n: An integer representing the current roll number.
        sum: An integer representing the cumulative sum of the rolls so far.

    Returns: An ordered pair (sum, ratio) representing the sum of the rolls and the running average (ratio) after the current roll.
"""
def scatter(n, sum):
    x = random.randint(1, 6)
    sum += x
    ratio = sum/n
    plt.scatter(n, ratio, color="blue", label="Running Average")
    return sum, ratio

writer = PillowWriter(fps=30)

# Draw the expected value line at 3.5
x = np.linspace(1, 1000, 1000)
y = np.full(1000, 3.5)
plt.plot(x, y, color="orange", label="Expected Value")

with writer.saving(fig, "expected_value.gif", 100):
    sum = 0
    for i in range(1, 1000):
        ratio = scatter(i, sum)
        sum = ratio[0]
        plt.title(f"Expected Value: {ratio[1]}")
        if i == 1:
            ax.legend()
        writer.grab_frame()
