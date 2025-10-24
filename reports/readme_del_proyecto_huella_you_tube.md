# 🎬 Proyecto: Huella YouTube y Recomendador Inteligente

> **Autor:** [Tu nombre aquí]  
> **Curso:** Ciencia de Datos / Machine Learning  
> **Año:** 2025  
> **Repositorio:** [github.com/tuusuario/huella-youtube](#)

---

## 🧠 Descripción general

Este proyecto analiza mi **huella de consumo en YouTube** (exportada desde [Google Takeout](https://takeout.google.com/)) para construir un **sistema de recomendación** y estudiar el fenómeno de la **burbuja algorítmica**.

Se desarrollaron tres enfoques de recomendación:
1. **Popularidad** → Baseline que recomienda los videos más vistos.
2. **Basado en Contenido** → Usa embeddings semánticos de los videos (título, descripción, keywords).
3. **Híbrido (Contenido + Contexto)** → Combina similitud semántica con señales contextuales (hora, día, canal, categoría, suscripción).

El análisis incluye la detección de sesgos, segmentación temática por *clusters*, y la evaluación de métricas como **Precision@10**, **Recall@10**, **Cobertura**, **Diversidad**, y **Bubble Index**.

---

## 🚀 Objetivos del proyecto

- Analizar mis patrones de visualización y hábitos horarios en YouTube.  
- Evaluar cómo los algoritmos pueden reforzar preferencias o crear burbujas temáticas.  
- Construir y comparar distintos tipos de recomendadores.  
- Medir la relevancia, diversidad y sesgo algorítmico de cada modelo.

---

## 🧩 Estructura del repositorio

```
├── data/
│   ├── youtube_history_sample.csv     # Datos anonimizados o sintéticos
│   ├── embeddings.parquet             # Embeddings de texto y contenido
│   └── data_dictionary.md             # Diccionario de datos
│
├── notebooks/
│   ├── 01_EDA_youtube.ipynb           # Exploración y limpieza
│   ├── 02_Modelos_Recomendacion.ipynb # Modelos: popularidad, contenido, híbrido
│   └── 03_Analisis_Burbuja.ipynb      # Métricas y visualizaciones finales
│
├── src/
│   ├── recommenders.py                # Funciones de recomendación
│   ├── metrics.py                     # Métricas personalizadas
│   └── utils.py                       # Utilidades generales
│
├── reports/
│   ├── figures/                       # Gráficos (heatmaps, evolución, comparativas)
│   └── comparativa_final.png
│
├── README.md                          # Este archivo
└── requirements.txt                   # Librerías necesarias
```

---

## ⚙️ Instalación y ejecución

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/tuusuario/huella-youtube.git
   cd huella-youtube
   ```

2. **Crear entorno virtual e instalar dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Ejecutar el notebook principal en Colab o localmente:**
   ```bash
   jupyter notebook notebooks/02_Modelos_Recomendacion.ipynb
   ```

---

## 📊 Principales resultados

| Modelo | Precision@10 | Recall@10 | Cobertura | Diversidad | BubbleIndex |
|---------|---------------|-----------|------------|-------------|-------------|
| **Popularidad** | 0.008 | 0.003 | 0.0007 | 0.270 | 0.105 |
| **Contenido** | 0.0095 | 0.005 | 0.129 | 0.164 | 0.871 |
| **Híbrido** | 0.0099 | 0.010 | 0.124 | 0.186 | 0.817 |

🔹 **Conclusión general:**  
El modelo **híbrido** logra el mejor balance entre relevancia y diversidad, reduciendo parcialmente la burbuja algorítmica respecto al modelo de contenido puro.

---

## 🧭 Análisis ético y de privacidad

- Los datos personales fueron **anonimizados y transformados** antes del análisis.  
- No se incluyen nombres de usuarios, IDs reales ni contenido sensible.  
- Se evaluó el impacto de los algoritmos sobre la **diversidad de exposición** y el **sesgo de recomendación**.

📌 *El proyecto busca fomentar la transparencia y la reflexión ética sobre los sistemas de recomendación.*

---

## 📈 Visualizaciones destacadas

- 📅 **Evolución trimestral de consumo** por cluster temático.  
- 🔥 **Mapa de calor** de actividad por hora y día.  
- 🧩 **Diversidad de clusters** y métricas de burbuja algorítmica.  
- 🎯 **Comparativa de modelos**: Popularidad vs Contenido vs Híbrido.

---

## 🧮 Tecnologías utilizadas

- **Python** · `pandas`, `numpy`, `scikit-learn`, `plotly`, `sentence-transformers`  
- **Clustering:** `KMeans` para segmentar contenido por tema.  
- **Embeddings:** Modelos semánticos tipo BERT/SentenceTransformer.  
- **Visualización:** `plotly.express`, `seaborn`, `matplotlib`.  
- **Evaluación:** Métricas personalizadas (Precision@K, Recall@K, Cobertura, Diversidad).

---

## 🧩 Estructura metodológica

1. **Carga y limpieza de datos** (`Takeout → DataFrame`).  
2. **Generación de embeddings** de texto y metadatos.  
3. **Análisis exploratorio (EDA)** de hábitos y consumo.  
4. **Entrenamiento de recomendadores.**  
5. **Evaluación de métricas de rendimiento y sesgo.**  
6. **Visualización e interpretación ética.**

---

## 📜 Créditos

Este proyecto forma parte del **Reto Ético y Técnico de Recomendación Algorítmica**  
en el curso *Data Science y Ética de IA (2025)*.  

**Autor:** [Tu Nombre]  
**Contacto:** [tuemail@dominio.com]  
**Licencia:** MIT License  

---

## 💬 Cita sugerida

> *[Tu Apellido, Año]*. “Huella YouTube y Recomendador Inteligente: análisis de burbujas algorítmicas y diversidad de exposición.”  
> Proyecto académico, [Tu Universidad o institución].

---

