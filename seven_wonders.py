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
    plt.tight_layout()
    plt.savefig("results/avg_points_percentage_per_game.png")
    plt.show()


def to_dataframe(parties):
    data = []
    for i, partie in enumerate(parties):
        for name, pts in partie.items():
            data.append((i, name, pts))
    return pd.DataFrame(data, columns=("game_id", "player", "points"))


def plot_normalized_rank(parties):
    parties = to_dataframe(parties)
    parties["rank"] = parties.groupby("game_id")["points"].rank()
    game_player_nb = parties.groupby("game_id")["points"].count()
    parties["player_nb"] = parties["game_id"].map(game_player_nb)
    parties["normalized_rank"] = (parties["rank"] - 0.5) / parties["player_nb"]

    mean_normalized_rank = parties.groupby("player")["normalized_rank"].mean()
    mean_normalized_rank = mean_normalized_rank.sort_values(ascending=False)

    plt.bar(mean_normalized_rank.index, mean_normalized_rank.values)
    plt.ylabel("normalized rank : (rank - 0.5) / player_nb")
    plt.xticks(rotation="vertical")
    plt.title("Normalized rank over all games")
    plt.tight_layout()
    plt.savefig("results/normalized_rank.png")
    plt.show()


if __name__ == "__main__":
    with open("data.json") as f:
        parties = json.load(f)

    plot_ranking_pt_part(parties)
    plot_normalized_rank(parties)
