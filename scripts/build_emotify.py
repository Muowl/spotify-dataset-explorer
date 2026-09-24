"""Resume as anotações oficiais do Emotify para a página estática.

Uso: baixar data.csv da página oficial para data/emotify.csv e executar
    python scripts/build_emotify.py
"""

import csv
import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "data" / "emotify.csv"
DEST = ROOT / "docs" / "assets" / "emotify-data.js"
EMOTIONS = (
    "amazement", "solemnity", "tenderness", "nostalgia", "calmness",
    "power", "joyful_activation", "tension", "sadness",
)
REQUIRED = {"track id", "genre", *EMOTIONS, "mood", "liked", "disliked"}


def main():
    with SOURCE.open(encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f, skipinitialspace=True)
        if not reader.fieldnames or not REQUIRED.issubset(reader.fieldnames):
            raise ValueError("Colunas ausentes no CSV oficial do Emotify")
        rows = list(reader)
    if not rows:
        raise ValueError("CSV vazio")
    emotion_counts = Counter()
    genre_counts = Counter()
    mood_counts = Counter()
    track_ids = set()
    liked = disliked = both = over_three = 0
    for row in rows:
        values = [row[name] for name in EMOTIONS]
        if any(value not in {"0", "1"} for value in values + [row["liked"], row["disliked"]]):
            raise ValueError("Indicador não binário encontrado")
        emotion_counts.update(name for name in EMOTIONS if row[name] == "1")
        genre_counts[row["genre"]] += 1
        mood_counts[row["mood"]] += 1
        track_ids.add(row["track id"])
        liked += row["liked"] == "1"
        disliked += row["disliked"] == "1"
        both += row["liked"] == row["disliked"] == "1"
        over_three += sum(value == "1" for value in values) > 3
    summary = {
        "annotations": len(rows),
        "excerpts": len(track_ids),
        "genres": dict(sorted(genre_counts.items())),
        "emotions": {name: emotion_counts[name] for name in EMOTIONS},
        "mood_codes": dict(sorted(mood_counts.items())),
        "liked": liked,
        "disliked": disliked,
        "both": both,
        "over_three": over_three,
    }
    DEST.write_text("window.emotifySummary = " + json.dumps(summary, ensure_ascii=False, indent=2) + ";\n", encoding="utf-8")
    print(f"{len(rows)} avaliações, {len(track_ids)} trechos; salvo em {DEST.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
