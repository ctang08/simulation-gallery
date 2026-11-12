"""Project 3: Emergence

Author		Christopher Tang
Date		03/25/2026

This program simulates Langton's Ant. The ant moves on a grid of black and white cells, following simple rules based on the color of the cell it is currently on. The program visualizes the ant's movement and the resulting pattern on the grid.

AI Usage: 	AI wasn't used for this project.

Sources:    
https://en.wikipedia.org/wiki/Langton%27s_ant
https://langtonant.com/

"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import PillowWriter


fig, ax = plt.subplots()

# Create a 200x200 grid of white cells
grid = np.ones((200, 200))
x = 100
y = 100
direction = 0

"""
turn
    Determines the new direction of the ant based on the current color of the cell it is on. If the cell is black (color = 1), the ant turns counterclockwise. If the cell is white, the ant turns clockwise.

    Args: 
        direction: An integer representing the current direction of the ant (0: up, 1: right, 2: down, 3: left).
        color: An integer representing the color of the cell (0: white, 1: black).

    Returns: An integer representing the new direction of the ant.
"""
def turn(direction, color):
    if color == 1:
        return (direction - 1) % 4
    elif color == 0:
        return (direction + 1) % 4

"""
move
    Determines the new position of the ant based on its current direction.

    Args: 
        x: An integer representing the current x-coordinate of the ant.
        y: An integer representing the current y-coordinate of the ant.
        direction: An integer representing the current direction of the ant (0: up, 1: right, 2: down, 3: left).

    Returns: An ordered pair (x, y) representing the new position of the ant.
"""
def move(x, y, direction):
    if direction == 0:
        return x, y + 1
    elif direction == 1:
        return x + 1, y
    elif direction == 2:
        return x, y - 1
    elif direction == 3:
        return x - 1, y

# Simulate the ant's movement for 13,000 steps
for i in range(13000):
    color = grid[x, y]
    direction = turn(direction, color)
    grid[x, y] = 1 - color
    x, y = move(x, y, direction)

    x %= 200
    y %= 200

ax.imshow(grid, cmap='gray')
ax.set_title("Langton's Ant (13,000 steps)")
plt.show()