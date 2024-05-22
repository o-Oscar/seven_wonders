import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import json


def extract_names(parties):
    names = set()
    for partie in parties:
        for n in partie.keys():
            names.add(n)
    return names


def fraction_points(partie, name):
    if name not in partie:
        return None
    total = sum(partie.values())
    points = partie[name]
    return points / total


def avg_fraction_points(parties, name):
    all_pts = []
    for partie in parties:
        pt = fraction_points(partie, name)
        if pt is not None:
            all_pts.append(pt)
    return np.mean(all_pts)


def ranking_pt_part(parties):
    names = extract_names(parties)
    ranking = {}
    for name in names:
        ranking[name] = avg_fraction_points(parties, name)
    return sorted(ranking.items(), key=lambda x: x[1], reverse=True)


def plot_ranking_pt_part(parties):
    ranking = ranking_pt_part(parties)
    plt.bar([name for name, frac in ranking], [frac for name, frac in ranking])
    plt.ylabel("points percentage per game")
    plt.xticks(rotation="vertical")
    plt.title("Avg points percentage per game")
    plt.savefig("results/avg_points_percentage_per_game.png")
    plt.show()


if __name__ == "__main__":
    with open("data.json") as f:
        parties = json.load(f)

    plot_ranking_pt_part(parties)
