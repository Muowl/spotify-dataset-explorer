"""Resume as anotações oficiais do Emotify para a página estática.

Uso: baixar data.csv da página oficial para data/emotify.csv e executar
    python scripts/build_emotify.py
"""

import csv
import hashlib
from io import StringIO
import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "data" / "emotify.csv"
DEST = ROOT / "docs" / "assets" / "emotify-data.js"
# Bytes obtidos da fonte oficial em 17/10/2026 UTC; hash da cópia reconferido em 18/10/2026 UTC.
SOURCE_URL = "https://www2.projects.science.uu.nl/memotion/emotifydata/data.csv"
SOURCE_OBSERVED_AT_UTC = "2026-10-17"
EXPECTED_SHA256 = "32229d7329e1245af3f9bd2e7005f51e1c8582ae1e48b9afa5cacb8cdcb65d71"
EMOTIONS = (
    "amazement", "solemnity", "tenderness", "nostalgia", "calmness",
    "power", "joyful_activation", "tension", "sadness",
)
REQUIRED = {"track id", "genre", *EMOTIONS, "mood", "liked", "disliked"}


def main():
    source_bytes = SOURCE.read_bytes()
    source_sha256 = hashlib.sha256(source_bytes).hexdigest()
    if source_sha256 != EXPECTED_SHA256:
        raise ValueError("CSV Emotify diferente da versão observada; confira a origem e refaça a auditoria antes de publicar.")
    print(f"Emotify: SHA-256 {source_sha256}; fonte observada em {SOURCE_OBSERVED_AT_UTC} UTC ({SOURCE_URL})")
    with StringIO(source_bytes.decode("utf-8-sig"), newline="") as f:
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
    # Exemplo real: primeira avaliação que marcou apenas nostalgia e tranquilidade.
    example_index, example = next(
        (i, row) for i, row in enumerate(rows, start=2)
        if {name for name in EMOTIONS if row[name] == "1"} == {"nostalgia", "calmness"}
    )
    summary = {
        "example": {
            "csv_line": example_index,
            "track_id": example["track id"],
            "genre": example["genre"],
            "emotions": {name: int(example[name]) for name in EMOTIONS},
        },
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
