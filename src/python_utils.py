import ast
import pandas as pd

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