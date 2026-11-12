"""Seeded numerical models. No plotting or file writes on import."""
import numpy as np


def monty_hall(trials=10000, seed=42):
    rng = np.random.default_rng(seed)
    prizes, choices = rng.integers(0, 3, size=(2, trials))
    stay = prizes == choices
    n = np.arange(1, trials + 1)
    return n, np.cumsum(stay) / n, np.cumsum(~stay) / n


def random_walk(steps=500, walkers=1000, p=0.5, seed=42):
    rng = np.random.default_rng(seed)
    paths = np.cumsum(np.where(rng.random((walkers, steps)) < p, 1, -1), axis=1)
    return np.arange(1, steps + 1), np.mean(np.abs(paths), axis=0)


def estimate_pi(samples=10000, seed=42):
    xy = np.random.default_rng(seed).random((samples, 2))
    inside = np.sum(xy ** 2, axis=1) <= 1
    estimates = 4 * np.cumsum(inside) / np.arange(1, samples + 1)
    return xy, inside, estimates


def expected_value(rolls=10000, seed=42):
    values = np.random.default_rng(seed).integers(1, 7, rolls)
    return np.cumsum(values) / np.arange(1, rolls + 1)


def ant(steps=12000, hexagonal=False):
    """Square LR ant or the seven-state axial-grid rule from the exercise."""
    directions = [(1, 0), (0, 1), (-1, 1), (-1, 0), (0, -1), (1, -1)] if hexagonal else [(0, 1), (1, 0), (0, -1), (-1, 0)]
    turns = [-1, -2, 0, 3, -2, -1, 2] if hexagonal else [1, -1]
    grid = {}
    x = y = heading = 0
    for _ in range(steps):
        color = grid.get((x, y), 0)
        heading = (heading + turns[color]) % len(directions)
        grid[x, y] = (color + 1) % len(turns)
        dx, dy = directions[heading]
        x, y = x + dx, y + dy
    return grid
