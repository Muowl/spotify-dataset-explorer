"""Build the popular-music page data from the original CSV and reviewed selection.

Run: python scripts/build_global_hits.py
No network calls; YouTube observations stay frozen in data/youtube-selection.json.
"""
import csv
import hashlib
import json
from pathlib import Path
from statistics import median

ROOT = Path(__file__).resolve().parents[1]
FEATURES = ('danceability', 'energy', 'valence', 'acousticness', 'instrumentalness', 'speechiness', 'liveness', 'tempo', 'loudness', 'duration_ms')


def build():
    source = ROOT / 'data/dataset.csv'
    selection = json.loads((ROOT / 'data/youtube-selection.json').read_text())
    if hashlib.sha256(source.read_bytes()).hexdigest() != selection['dataset_sha256']:
        raise ValueError('CSV diferente da versão revisada; refaça a auditoria antes de publicar.')
    tracks = {}
    with source.open(encoding='utf-8-sig', newline='') as f:
        for row in csv.DictReader(f):
            tracks.setdefault(row['track_id'], row)
    videos = []
    seen = set()
    for entry in selection['videos']:
        entry = dict(entry)
        if entry['youtube_id'] in seen:
            raise ValueError('Vídeo duplicado na seleção')
        seen.add(entry['youtube_id'])
        if entry['match_status'] not in ('catalogue', 'uncertain', 'missing'):
            raise ValueError('Status inválido')
        if not isinstance(entry['views'], int) or entry['views'] < 0:
            raise ValueError('Visualizações inválidas')
        row = tracks.get(entry['track_id'])
        entry['features'] = None
        entry['popularity'] = None
        entry['album'] = None
        if entry['track_id']:
            if row is None or row['track_name'] != entry['expected_track_name'] or row['artists'] != entry['expected_artists']:
                raise ValueError(f"Correspondência alterada: {entry['track_id']}")
            entry['album'] = row['album_name']
            entry['popularity'] = int(row['popularity'])
            if entry['match_status'] == 'catalogue':
                entry['features'] = {f: float(row[f]) for f in FEATURES}
        elif entry['match_status'] != 'missing':
            raise ValueError('Faixa ausente sem status missing')
        videos.append(entry)
    groups = []
    for spec in selection['groups']:
        items = sorted([v for v in videos if v['group'] == spec['id']], key=lambda v: -v['views'])
        if len(items) != 10:
            raise ValueError('Cada grupo deve manter os dez casos documentados')
        included = [v for v in items if v['features'] is not None]
        groups.append({**spec, 'items': items, 'n': len(included), 'median': {f: median(v['features'][f] for v in included) for f in FEATURES} if included else None})
    result = {'groups': groups, 'unique_tracks': len(tracks), 'dataset_sha256': selection['dataset_sha256'], 'corpus_median': {f: median(float(r[f]) for r in tracks.values()) for f in FEATURES}}
    output = ROOT / 'docs/assets/hits-data.js'
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text('window.HITS_DATA = ' + json.dumps(result, ensure_ascii=False, separators=(',', ':')) + ';\n')
    print('Gerado:', ', '.join(f"{g['label']}: {g['n']}/10 com áudio associado" for g in groups))


if __name__ == '__main__':
    build()
