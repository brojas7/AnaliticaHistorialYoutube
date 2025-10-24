# Proyecto: Huella YouTube y Recomendador Inteligente

> **Autor:** Bernal Rojas Villalobos
> **Curso:** Fundamentos de analítica de datos
> **Año:** 2025  
> **Repositorio:** [https://github.com/brojas7/AnaliticaHistorialYoutube](#)

---

## Descripción general

Este proyecto analiza mi **huella de consumo en YouTube** (exportada desde [Google Takeout](https://takeout.google.com/)) para construir un **sistema de recomendación** y estudiar el fenómeno de la **burbuja algorítmica**

Se desarrollaron tres enfoques de recomendación:
1. **Popularidad** → Baseline que recomienda los videos más vistos.
2. **Basado en Contenido** → Usa embeddings semánticos de los videos (título, descripción, keywords).
3. **Híbrido (Contenido + Contexto)** → Combina similitud semántica con señales contextuales (hora, día, canal, categoría, suscripción).

El análisis incluye la detección de sesgos, segmentación temática por *clusters*, y la evaluación de métricas como **Precision@10**, **Recall@10**, **Cobertura**, **Diversidad**, y **Bubble Index**.

---

## Objetivos del proyecto

- Analizar mis patrones de visualización y hábitos horarios en YouTube.  
- Evaluar cómo los algoritmos pueden reforzar preferencias o crear burbujas temáticas.  
- Construir y comparar distintos tipos de recomendadores.  
- Medir la relevancia, diversidad y sesgo algorítmico de cada modelo.

---

## Estructura del repositorio

```
├── data/
│   ├── historial-de-búsqueda.json        # Datos crudos exportados de takeout 
│   ├── historial-de-reproducciones.json  # Datos crudos exportados de takeout
│   └── suscripciones.csv                 # Datos crudos exportados de takeout
│   └── df_enrich_enriquecido.csv         # Dataset enriquecido con gemini (Preprocesado para mayor velocidad en replicabilidad)
│
├── notebooks/
│   ├── main.ipynb                        # Cuaderno principal
│
├── src/
│   ├── gemini_utils.py                   # Utiidades de Gemini
│   ├── project_utils.py                  # Utiidades de proyecto
│   └── youtube_utils.py                  # Utilidades de Youtube
│
├── reports/
│   ├── figures/                          # Gráficos importantes
│   └── comparativa_final.png
│
├── README.md                          # Este archivo
└── requirements.txt                   # Librerías necesarias
```

---

## Instalación y ejecución

### Opción 1: Correr en google Colab (Recomendada)
Abrir y ejecutar e siguiente notebook:

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/brojas7/AnaliticaHistorialYoutube/blob/main/notebooks/main.ipynb)

### Opción 2: Correr en local
1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/brojas7/AnaliticaHistorialYoutube.git
   cd AnaliticaHistorialYoutube
   ```

2. **Crear entorno virtual e instalar dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Ejecutar el notebook principal en Colab o localmente:**
   ```bash
   jupyter notebook notebooks/main.ipynb
   ```

---


## Principales resultados

| Modelo | Precision@10 | Recall@10 | Cobertura | Diversidad | BubbleIndex |
|---------|---------------|-----------|------------|-------------|-------------|
| **Popularidad** | 0.008 | 0.003 | 0.0007 | 0.270 | 0.105 |
| **Contenido** | 0.0095 | 0.005 | 0.129 | 0.164 | 0.871 |
| **Híbrido** | 0.0099 | 0.010 | 0.124 | 0.186 | 0.817 |

**Conclusión general:**  
El modelo **híbrido** logra el mejor balance entre relevancia y diversidad, reduciendo parcialmente la burbuja algorítmica respecto al modelo de contenido puro.

---

## Análisis ético y de privacidad

- Los datos personales fueron **anonimizados y transformados** antes del análisis.  
- No se incluyen nombres de usuarios, IDs reales ni contenido sensible.  
- Se evaluó el impacto de los algoritmos sobre la **diversidad de exposición** y el **sesgo de recomendación**.

 *El proyecto busca fomentar la transparencia y la reflexión ética sobre los sistemas de recomendación.*

---

## Tecnologías utilizadas

- **Python** · `pandas`, `numpy`, `scikit-learn`, `plotly`, `sentence-transformers`  
- **Clustering:** `KMeans` para segmentar contenido por tema.  
- **Embeddings:** `Word2Vec` como modelo semántico 
- **Visualización:** `plotly.express`, `seaborn`, `matplotlib`.  
- **Evaluación:** Métricas personalizadas (Precision@K, Recall@K, Cobertura, Diversidad).

---

## Estructura metodológica

1. **Carga, limpieza de datos** (`Takeout → DataFrame`).  
1. **Enriquecimiento de datos con Gemini** (`DataFrame → Gemini → DataFrame`).  
3. **Generación de embeddings** de texto.  
3. **Análisis exploratorio (EDA)** de hábitos y consumo.  
4. **Entrenamiento de recomendadores.**  
5. **Evaluación de métricas de rendimiento y sesgo.**  
6. **Visualización e interpretación.**


---

## 📈 Visualizaciones destacadas

- 📅 **Evolución trimestral de consumo** por cluster temático.  
- 🔥 **Mapa de calor** de actividad por hora y día.  
- 🧩 **Diversidad de clusters** y métricas de burbuja algorítmica.  
- 🎯 **Comparativa de modelos**: Popularidad vs Contenido vs Híbrido.


---

## 📜 Créditos

Este proyecto forma parte del **Reto Ético y Técnico de Recomendación Algorítmica**  
en el curso *Fundamentos de analítica de datos*.  

**Autor:** Bernal Rojas Villalobos
**Contacto:** [brojas@ucenfotec.ac.cr]  

---

## Cita sugerida

> *[Rojas, 2025]*. “Huella YouTube y Recomendador Inteligente: análisis de burbujas algorítmicas y diversidad de exposición.”  
> Proyecto académico, Universidad Cenfotec.

---

