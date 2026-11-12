"""Run with python -m simulations --output docs/assets --seed 42."""
import argparse
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.collections import PatchCollection
from matplotlib.patches import RegularPolygon
from . import models


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=Path("docs/assets"))
    parser.add_argument("--seed", type=int, default=42)
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)
    plt.rcParams.update({"figure.figsize": (8, 5), "axes.spines.top": False, "axes.spines.right": False, "figure.dpi": 140})
    def save(name, title):
        plt.title(title, loc="left", fontweight="bold", pad=18)
        plt.tight_layout()
        plt.savefig(args.output / (name + ".png"))
        plt.close()
    n, stay, switch = models.monty_hall(seed=args.seed)
    plt.plot(n, stay, label="Stay", color="#e08747"); plt.plot(n, switch, label="Switch", color="#136f63")
    plt.axhline(2/3, color="#999999", ls=":"); plt.xlabel("Trials"); plt.ylabel("Win rate"); plt.legend()
    save("monty-hall", "Changing your mind pays off")
    for p in (0.5, 0.9):
        n, displacement = models.random_walk(p=p, seed=args.seed)
        plt.plot(n, displacement, label=f"P(right) = {p}")
    plt.plot(n, np.sqrt(2*n/np.pi), ls=":", label="Unbiased asymptotic mean |position|")
    plt.xlabel("Steps"); plt.ylabel("Mean absolute position"); plt.legend()
    save("random-walk", "A small bias changes the journey")
    xy, inside, estimates = models.estimate_pi(seed=args.seed)
    plt.scatter(xy[:, 0], xy[:, 1], c=np.where(inside, "#136f63", "#e08747"), s=1)
    plt.gca().set_aspect("equal"); plt.xlabel("x"); plt.ylabel("y")
    save("estimate-pi", f"Random points estimate π ≈ {estimates[-1]:.4f}")
    means = models.expected_value(seed=args.seed)
    plt.plot(np.arange(1, len(means)+1), means, color="#136f63")
    plt.axhline(3.5, ls=":", color="#e08747", label="Expected value: 3.5")
    plt.xlabel("Die rolls"); plt.ylabel("Running average"); plt.legend()
    save("expected-value", "The average settles down")
    for hexagonal in (False, True):
        grid = models.ant(50000 if hexagonal else 12000, hexagonal)
        fig, ax = plt.subplots()
        if hexagonal:
            patches = [RegularPolygon((1.5*x, np.sqrt(3)*(y+x/2)), numVertices=6, radius=1, orientation=np.pi/6) for x,y in grid]
            collection = PatchCollection(patches, cmap="viridis", linewidth=0)
            collection.set_array(np.array(list(grid.values()))); ax.add_collection(collection); ax.autoscale_view()
        else:
            points = np.array([p for p, v in grid.items() if v])
            ax.scatter(points[:,0], points[:,1], marker="s", s=3, color="#136f63")
        ax.set_aspect("equal"); ax.axis("off")
        save("hexagonal-ant" if hexagonal else "langtons-ant", "Seven colors, six directions" if hexagonal else "Order emerging from simple rules")
    print(f"Generated six figures in {args.output}")

if __name__ == "__main__":
    main()
