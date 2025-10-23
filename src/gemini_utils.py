import os, re, json, time, random
import pandas as pd
from tqdm import tqdm
import google.generativeai as genai

def setup_gemini(api_key: str, model_name: str = "gemini-2.5-flash"):
    """Configura la API de Gemini."""
    genai.configure(api_key=api_key)
    return genai.GenerativeModel(model_name)


def classify_batch_with_gemini(model, batch_df: pd.DataFrame, retries: int = 2):
    """
    Analiza un batch pequeño (20 filas aprox) con Gemini.
    Devuelve una lista de diccionarios con: category, subtopic, format, keywords.
    """
    pairs = [
        f"{i+1}. {row.video_title} — {row.channel_title}"
        for i, row in batch_df.iterrows()
    ]

    prompt = f"""
    Analiza los siguientes {len(batch_df)} videos de YouTube.
    Devuelve únicamente una lista JSON válida donde cada elemento corresponde a un video,
    con las claves: "category", "subtopic", "format", "keywords" (lista corta).
    No incluyas texto adicional ni explicaciones.
    Videos:
    {chr(10).join(pairs)}
    """

    for attempt in range(retries):
        try:
            response = model.generate_content(prompt, request_options={"timeout": 45})
            text = response.text.strip()

            # A veces Gemini agrega texto extra → extraemos solo el JSON
            json_match = re.search(r'\[.*\]', text, re.DOTALL)
            if json_match:
                text = json_match.group(0)

            results = json.loads(text)

            # Validamos tamaño
            if len(results) != len(batch_df):
                print(f"Tamaño inconsistente: esperados {len(batch_df)}, recibidos {len(results)}")
                results = [results[0]] * len(batch_df)

            return results

        except Exception as e:
            wait = (2 ** attempt) + random.uniform(0, 1)
            print(f"Error intento {attempt+1}: {e} → Reintentando en {wait:.1f}s...")
            time.sleep(wait)

    # Fallo total → devolvemos valores por defecto
    print("Falló el batch, devolviendo valores por defecto.")
    return [
        {"category": "otros", "subtopic": "otros", "format": "desconocido", "keywords": []}
        for _ in range(len(batch_df))
    ]


def enrich_videos_with_gemini(df_part: pd.DataFrame, model, output_path: str, batch_size: int = 20):
    """
    Procesa un DataFrame completo en lotes usando Gemini.
    Guarda el CSV enriquecido con las columnas nuevas.
    """
    results = []
    for start in tqdm(range(0, len(df_part), batch_size)):
        end = start + batch_size
        batch = df_part.iloc[start:end]
        batch_results = classify_batch_with_gemini(model, batch)
        results.extend(batch_results)
        time.sleep(1)

    df_enrich = pd.concat([df_part.reset_index(drop=True), pd.json_normalize(results)], axis=1)
    df_enrich.to_c
