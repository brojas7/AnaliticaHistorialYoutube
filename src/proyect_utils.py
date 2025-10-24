import ast
import pandas as pd
import hashlib
import numpy as np

def reverse_lookup(column, hashed_value):
    """
    Busca en el diccionario 
    """
    reverse_map = {v: k for k, v in hash_maps[column].items()}
    return reverse_map.get(hashed_value, None)

def normalize_value(x):
    """Convierte listas a strings ordenados, mantiene consistencia en hashes."""
    if isinstance(x, list):
        try:
            # ordenar los elementos para que ['a','b'] y ['b','a'] den el mismo hash
            return ", ".join(sorted(map(str, x)))
        except Exception:
            return str(x)
    elif isinstance(x, np.ndarray):
        return ", ".join(map(str, x.tolist()))
    else:
        return x

def str_to_list(column):
    """
    Convierte una columna de strings con formato de lista en listas reales.
    Ejemplo: "['piano', 'easy to learn']" -> ['piano', 'easy to learn']

    Parámetros:
        column (pd.Series): Columna de un DataFrame.

    Retorna:
        pd.Series: Columna convertida a listas reales.
    """
    def safe_eval(x):
        if isinstance(x, str):
            try:
                return ast.literal_eval(x)
            except Exception:
                return []
        elif isinstance(x, list):
            return x
        else:
            return []

    return column.apply(safe_eval)