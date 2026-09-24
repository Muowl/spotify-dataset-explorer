"""Recria os dados da página de hits a partir do CSV original.

Uso: python scripts/build_global_hits.py
O CSV deve estar em data/dataset.csv (veja data/README.md).
"""

import csv
import json
from pathlib import Path
from statistics import median


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "data" / "dataset.csv"
OUTPUT = ROOT / "docs" / "assets" / "hits-data.js"

# Cinco clipes musicais mais vistos na lista retrospectiva do YouTube (2022).
# O ID fixa a gravação usada; nomes iguais, covers e remixes não entram.
HITS = [
    ("Despacito", "Luis Fonsi;Daddy Yankee", "6habFhsOp2NvshLv26DqMb"),
    ("Shape of You", "Ed Sheeran", "7qiZfU4dY1lWllzX7mPBI3"),
    ("See You Again", "Wiz Khalifa;Charlie Puth", "2JzZzZUQj3Qff7wapcbKjc"),
    ("Uptown Funk", "Mark Ronson;Bruno Mars", "32OlwWuMpZ6b0aN2RZOeMS"),
    ("Gangnam Style", "PSY", "03UrZgTINDqvnUMbbIMhql"),
]
# Rótulos específicos escolhidos para contrastar perfis sonoros.
# Em cada rótulo, o ID é uma das faixas com maior popularity no CSV.
NICHES = [
    ("heavy-metal", "Heavy metal", "2TZtQt10Ajm3wB4MoqluZj"),
    ("bluegrass", "Bluegrass", "11TmWrHkxwtVcCtEdAXjJA"),
    ("classical", "Clássica", "1BncfTJAWxrsxyT9culBrj"),
    ("drum-and-bass", "Drum and bass", "6LW3Z1GqbL78TIjfDyg4zp"),
]
FEATURES = (
    "danceability", "energy", "valence", "tempo", "acousticness",
    "instrumentalness", "speechiness", "liveness", "loudness", "duration_ms",
)


def build():
    if not SOURCE.exists():
        raise SystemExit(f"CSV não encontrado: {SOURCE}. Consulte data/README.md.")

    values = {feature: [] for feature in FEATURES}
    wanted = {hit[2]: hit for hit in HITS}
    niche_ids = {item[2] for item in NICHES}
    niche_genres = {item[0] for item in NICHES}
    genre_popularity = {genre: [] for genre in niche_genres}
    genre_seen = {genre: set() for genre in niche_genres}
    niche_rows = {}
    found = {}
    seen = set()
    original_count = 0
    with SOURCE.open(encoding="utf-8-sig", newline="") as source:
        for row in csv.DictReader(source):
            original_count += 1
            track_id = row["track_id"]
            genre = row["track_genre"]
            if genre in niche_genres and track_id not in genre_seen[genre]:
                genre_seen[genre].add(track_id)
                genre_popularity[genre].append(int(row["popularity"]))
                if track_id in niche_ids:
                    niche_rows[(genre, track_id)] = row
            if track_id in seen:
                continue
            seen.add(track_id)
            for feature in FEATURES:
                if row[feature]:
                    values[feature].append(float(row[feature]))
            if track_id in wanted:
                title, artist, _ = wanted[track_id]
                if row["artists"] != artist:
                    raise ValueError(f"Artista inesperado para {track_id}: {row['artists']}")
                found[track_id] = {
                    "title": title,
                    "artist": artist.replace(";", ", "),
                    "track_id": track_id,
                    "features": {feature: float(row[feature]) for feature in FEATURES},
                }

    missing = set(wanted) - set(found)
    if missing:
        raise ValueError(f"Gravações ausentes: {', '.join(sorted(missing))}")

    hits = [found[track_id] for _, _, track_id in HITS]
    niches = []
    for genre, label, track_id in NICHES:
        row = niche_rows.get((genre, track_id))
        if row is None:
            raise ValueError(f"Faixa {track_id} ausente do gênero {genre}")
        score = int(row["popularity"])
        if score != max(genre_popularity[genre]):
            raise ValueError(f"Faixa {track_id} deixou de liderar {genre}")
        niches.append({
            "title": row["track_name"],
            "artist": row["artists"].replace(";", ", "),
            "genre": label,
            "genre_key": genre,
            "track_id": track_id,
            "popularity": score,
            "genre_median_popularity": median(genre_popularity[genre]),
            "genre_tracks": len(genre_popularity[genre]),
            "features": {feature: float(row[feature]) for feature in FEATURES},
        })
    result = {
        "source_rows": original_count,
        "unique_tracks": len(seen),
        "hits": hits,
        "niches": niches,
        "corpus_median": {feature: median(values[feature]) for feature in FEATURES},
        "hits_median": {
            feature: median(hit["features"][feature] for hit in hits)
            for feature in FEATURES
        },
        "niches_median": {
            feature: median(track["features"][feature] for track in niches)
            for feature in FEATURES
        },
    }
    OUTPUT.write_text(
        "window.HITS_DATA = " + json.dumps(result, ensure_ascii=False, separators=(",", ":")) + ";\n",
        encoding="utf-8",
    )
    print(f"Gerado {OUTPUT.relative_to(ROOT)}: {len(hits)} hits, {len(niches)} nichos, {len(seen)} faixas únicas")


if __name__ == "__main__":
    build()
