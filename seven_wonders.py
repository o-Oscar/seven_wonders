import numpy as np
import matplotlib.pyplot as plt

# import random
# import math
# import time
# import pandas as pd

parties = [
    {
        "oscar": 42,
        "gab_buffet": 77,
        "romain": 66,
        "clem": 44,
        "JLB": 71,
    },
    {
        "adrien": 44,
        "romain": 59,
        "JLB": 66,
        "gab_buffet": 64,
        "Benoit": 63,
    },
    {
        "dimier": 67,
        "rieutord": 51,
        "romain": 64,
        "bodet": 33,
        "vincent": 49,
    },
    {
        "oscar": 44,
        "neige": 67,
        "gab_buffet": 54,
        "alice": 62,
        "srey": 31,
        "romain": 43,
        "bart": 60,
    },
    {
        "neige": 43,
        "alice": 66,
        "gab_buffet": 51,
        "bart": 46,
        "srey": 42,
        "romain": 62,
    },
    {
        "oscar": 51,
        "clem": 50,
        "adrien": 42,
        "gab_buffet": 51,
        "JLB": 33,
    },
    {
        "gab_letav": 46,
        "simon": 39,
        "dorian": 58,
        "romain": 42,
    },
    {
        "clem": 45,
        "bart": 37,
        "romain": 50,
        "adrien": 39,
        "JLB": 46,
    },
    {
        "oscar": 46,
        "adrien": 39,
        "neige": 61,
        "bart": 55,
        "srey": 41,
        "gab_buffet": 49,
        "romain": 55,
    },
    {
        "neige": 41,
        "romain": 59,
        "alice": 55,
        "bart": 42,
        "srey": 42,
        "gab_buffet": 48,
    },
    {
        "heloise": 39,
        "hortense": 41,
        "alice": 44,
        "JLB": 49,
    },
    {
        "oscar": 47,
        "romain": 62,
        "neige": 54,
        "alice": 36,
        "srey": 41,
        "gab_buffet": 59,
    },
    {
        "JLB": 50,
        "clem": 55,
        "gab_buffet": 59,
        "romain": 50,
        "alex": 60,
    },
    {
        "adrien": 51,
        "romain": 68,
        "rapha": 62,
        "JLB": 56,
        "bart": 50,
        "alex": 75,
    },
    {
        "heloise": 42,
        "alex": 66,
        "JLB": 67,
        "romain": 70,
    },
    {
        "adrien": 41,
        "oscar": 48,
        "gab_buffet": 46,
        "JLB": 54,
    },
    {
        "oscar": 59,
        "gab_buffet": 59,
        "srey": 40,
        "bart": 39,
        "romain": 29,
        "alice": 43,
        "neige": 43,
    },
    {
        "oscar": 68,
        "alice": 76,
        "hortense": 59,
        "romain": 86,
        "clem": 66,
        "JLB": 71,
    },
    {
        "dorian": 67,
        "gab_buffet": 76,
        "romain": 83,
        "clem": 53,
        "JLB": 77,
    },
    {
        "oscar": 56,
        "romain": 82,
        "bart": 64,
        "alex": 84,
        "gab_buffet": 88,
        "JLB": 64,
    },
    {
        "bart": 91,
        "romain": 64,
        "gab_buffet": 50,
        "oscar": 64,
        "alex": 47,
        "JLB": 72,
    },
    {
        "bart": 44,
        "alex": 50,
        "romain": 67,
        "oscar": 68,
        "gab_buffet": 61,
        "JLB": 63,
    },
    {
        "oscar": 75,
        "gab_buffet": 55,
        "alex": 53,
        "romain": 70,
        "JLB": 62,
    },
    {
        "clem": 65,
        "oscar": 108,
        "alex": 80,
        "JLB": 78,
        "romain": 79,
    },
    {
        "dorian": 50,
        "gab_letav": 44,
        "simon": 36,
        "romain": 53,
    },
]


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
    plt.show()


if __name__ == "__main__":
    # print(avg_part(parties, 'bart'))
    # a = ranking_pt_part(parties)
    # print(ranking_pt_part(parties))
    plot_ranking_pt_part(parties)
