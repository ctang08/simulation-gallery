"""
R-Project 0: Monty Hall Simulations

Author		Christopher Tang
Date		02/09/2026

This module contains the simulation code that facilitates runs of the Monty Hall Problem.  The program will generate a matplotlib file illustrating the results of the simulations.  The program may be run through pyCharm directly.

AI Usage: 	Copilot autocompleted one print statement [print("The player lost. The car was behind door " + str(winner + 1) + ".")]
Sources: 	
https://numpy.org/devdocs/reference/index.html
https://matplotlib.org/stable/users/explain/quick_start.html#quick-start
"""

import matplotlib.pyplot as plt
import numpy as np

"""
Monty hall simulation
    Runs one monty hall simulation with randomly generated door choices. Prints the players choices and results of the simulation (win or lose).

    Args:
        switch: An integer that is either 0 or 1. If switch is 1, then the player will switch to the other door after Monty reveals a goat. If switch is 0, then the player will stay with their original choice.

    Returns:
        A boolean that is True if the player wins the car and False if the player loses.
"""

def monty_hall_simulation(switch):

    rng = np.random.default_rng()
    winner = rng.integers(0, 3)
    choices = [0, 1, 2]
    choice = rng.integers(0, 3)
    reveal = rng.integers(0, 3)

    while reveal == choice or reveal == winner:
        reveal = rng.integers(0, 3)
    choices.remove(reveal)
    print("The player originally chose door " + str(choice + 1) + ". Door " + str(reveal + 1) + " was revealed to have goat.")
    if switch == 1:
        choices.remove(choice)
        choice = choices[0]
        print("The player chose to switch to door " + str(choice + 1) + ".")
    else:
        print("The player chose to stay with door " + str(choice + 1) + ".")
    if choice == winner:
        print("The player won the car!")
        print("")
        return True
    else:
        print("The player lost. The car was behind door " + str(winner + 1) + ".")
        print("")
        return False

plt.title("Monty Hall Simulation Results")
plt.xlabel("Number of Simulations")
plt.ylabel("Number of Wins")

for i in range(2):
    wins = 0
    x = np.array([])
    y = np.array([])
    for j in range(100):
        x = np.append(x, j+1)
        if monty_hall_simulation(i):
            wins += 1
        y = np.append(y, wins)
    plt.scatter(x, y, label="Switching" if i == 1 else "Staying")

plt.legend()

plt.show()