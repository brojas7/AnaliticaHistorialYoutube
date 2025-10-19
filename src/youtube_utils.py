# src/youtube_utils.py
import json
import gzip
import pandas as pd
import dateparser


def load_watch_history(path):
    """
    Carga el archivo 'watch-history.json' exportado desde Google Takeout.
    Devuelve un DataFrame con las columnas:
    ['timestamp', 'title', 'channel', 'channel_id', 'video_id', 'url'].
    """
    # Admite .json o .json.gz
    if path.endswith(".gz"):
        with gzip.open(path, "rt", encoding="utf-8") as f:
            data = json.load(f)
    else:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)

    rows = []
    for e in data:
        # Campos posibles en distintos formatos de Takeout
        time_str = e.get('time') or e.get('timestamp') or e.get('creationTime')
        ts = None
        if time_str:
            try:
                ts = dateparser.parse(time_str)
            except Exception:
                ts = None

        title = e.get('title') or e.get('header') or e.get('titleUrl') or ""
        channel = None
        url = None

        # Canal y URL pueden estar anidados en 'subtitles'
        if 'titleUrl' in e:
            url = e['titleUrl']
        if 'subtitles' in e and isinstance(e['subtitles'], list) and e['subtitles']:
            channel = e['subtitles'][0].get('name')

        # Extraer video_id desde la URL
        video_id = None
        if url and "watch?v=" in url:
            video_id = url.split("watch?v=")[-1].split("&")[0]

        rows.append({
            "timestamp": ts,
            "title": title,
            "channel": channel,
            "channel_id": None,
            "video_id": video_id,
            "url": url
        })

    df = pd.DataFrame(rows)
    df = df.dropna(subset=["timestamp"]).sort_values("timestamp").reset_index(drop=True)
    return df


def anonymize_df(df, cols_to_hash=("video_id", "channel", "url", "title")):
    """
    Anonimiza columnas sensibles mediante hashing no reversible.
    """
    def _hash(x):
        if pd.isna(x):
            return x
        return str(abs(hash(str(x))) % (10**12))

    df = df.copy()
    for c in cols_to_hash:
        if c in df.columns:
            df[c] = df[c].apply(_hash)
    return df


def sessionize(df, gap_minutes=30):
    """
    Crea sesiones a partir de eventos ordenados por tiempo.
    gap_minutes: nuevo id de sesión cuando hay un gap > gap_minutes.
    """
    df = df.sort_values("timestamp").reset_index(drop=True).copy()
    session_ids = []
    current_sid = 0
    prev_ts = None

    for _, row in df.iterrows():
        ts = row['timestamp']
        if prev_ts is None or (ts - prev_ts).total_seconds() > gap_minutes * 60:
            current_sid += 1
        session_ids.append(current_sid)
        prev_ts = ts

    df['session_id'] = session_ids
    df['session_idx'] = df.groupby('session_id').cumcount()
    return df
