"""Project 4: Emergence

Author		Christopher Tang
Date		4/10/2026

This project simulates a multi-color extension of Langton's Ant. The ant moves on a grid of cells that can be in one of seven colors, following specific rules based on the color of the cell it is currently on. The program visualizes the ant's movement and the resulting pattern on the grid.

AI Usage: 	AI wasn't used for this project.

Sources:    
https://matplotlib.org/3.1.3/api/_as_gen/matplotlib.patches.RegularPolygon.html
https://en.wikipedia.org/wiki/Langton%27s_ant#Extension_to_multiple_colors
https://homepages.inf.ed.ac.uk/rbf/CVonline/LOCAL_COPIES/AV0405/MARTIN/Hex.pdf

"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import RegularPolygon
from matplotlib.collections import PatchCollection


fig, ax = plt.subplots(figsize=(6,6))

grid = {}
a, b = 0, 0
direction = 0
directions = [(1, 0), (0, 1), (-1, 1), (-1, 0), (0, -1), (1, -1)]

'''
turn
    Determines the new direction of the ant based on the current color of the cell it is on.

    Args: 
        direction: An integer representing the current direction of the ant.
        color: An integer representing the color of the cell.

    Returns: An integer representing the new direction of the ant.
'''
def turn(direction, color):
    if color == 0: #L1
        return (direction - 1) % 6
    elif color == 1: #L2
        return (direction - 2) % 6
    elif color == 2: #N
        return direction
    elif color == 3: #U
        return (direction + 3) % 6
    elif color == 4: #L2
        return (direction - 2) % 6
    elif color == 5: #L1
        return (direction - 1) % 6
    elif color == 6: #R2
        return (direction + 2) % 6

for i in range(50000):
    color = grid.get((a, b), 0)
    direction = turn(direction, color)
    grid[(a, b)] = (color + 1) % 7
    da, db = directions[direction]
    a, b = a + da, b + db

patches = []
colors = []

'''
axial_to_pixel
    Converts axial coordinates (a, b) to pixel coordinates (x, y) for plotting.

    Args: 
        a: An integer representing the axial coordinate a.
        b: An integer representing the axial coordinate b.
        size: A float representing the size of the hexagon (default is 1).

    Returns: An ordered pair (x, y) representing the pixel coordinates for plotting.
'''
def axial_to_pixel(a, b, size=1):
    x = size * (3/2 * a)
    y = size * (np.sqrt(3) * (b + a/2))
    return x, y

for (a, b), color in grid.items():
    x, y = axial_to_pixel(a, b, size=0.5)
    hexagon = RegularPolygon((x, y), numVertices=6, radius=0.5, orientation=np.radians(30))
    patches.append(hexagon)
    colors.append(color)

collection = PatchCollection(patches, cmap='viridis')
collection.set_array(np.array(colors))

ax.add_collection(collection)
ax.set_aspect('equal')
ax.autoscale_view()
ax.set_title("Langton's Ant (multi-color extension)")
plt.show()