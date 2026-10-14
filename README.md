🌍 Procesamiento de Datos

Repositorio correspondiente a la materia Procesamiento de Datos de la Tecnicatura en Inteligencia Artificial y Ciencia de Datos.

📚 Trabajo Práctico N.º 1 – Análisis de Desastres Naturales (1970–2021)

En este trabajo práctico se desarrolló un proceso ETL (Extract, Transform, Load) utilizando Python, con el objetivo de procesar, analizar y visualizar información histórica sobre desastres naturales ocurridos en distintas regiones del mundo entre 1970 y 2021.

Se trabajó con un dataset de la base de datos internacional EM-DAT, compuesto por 14.644 registros y 47 columnas.

🔄 Proceso ETL

El proyecto se desarrolló mediante una estructura modular, separando las distintas etapas del procesamiento de datos.

1. Extracción (Extract)

Lectura del dataset en formato CSV.

Carga de los datos mediante Pandas.

Exploración inicial de la estructura del dataset.

2. Transformación (Transform)

Selección de variables relevantes para el análisis.

Limpieza y normalización de categorías.

Tratamiento de fechas.

Identificación y análisis de valores faltantes.

Agrupación y agregación de datos para obtener indicadores estadísticos.

3. Carga y visualización (Load)

Generación de gráficos para analizar los datos procesados.

Visualización de tendencias temporales y distribuciones geográficas.

Exportación de los gráficos en formato PNG.

📊 Análisis realizados

Se generaron cinco visualizaciones:

Evolución anual de desastres naturales: análisis de la cantidad de eventos registrados entre 1970 y 2021.

Tipos de desastres por continente: comparación de la distribución de los distintos fenómenos naturales.

Distribución mensual de desastres: identificación de los meses con mayor cantidad de eventos.

Evolución de los tipos de desastres (2002–2021): análisis de las tendencias según el tipo de fenómeno.

Personas afectadas por continente: comparación del impacto de los desastres naturales en la población.

📈 Principales resultados

Se observó un incremento en los registros anuales de desastres naturales durante las últimas décadas del siglo XX, con un máximo en el año 2000.

Asia presentó la mayor cantidad de eventos registrados y concentró el mayor número de personas afectadas.

Se identificaron diferencias en la distribución de los tipos de desastres entre continentes.

La distribución mensual permitió observar variaciones en la cantidad de eventos registrados a lo largo del año.

El análisis de valores faltantes permitió reconocer limitaciones del dataset y evitar interpretaciones incorrectas de la información.

🛠️ Tecnologías utilizadas

Python

Jupyter Notebook

Pandas

Matplotlib

Programación modular

Procesamiento ETL

## 📁 Estructura del proyecto

```text
ProcesamientoDeDatos/
│
├── data/
│   └── 1970-2021_DISASTERS.xlsx - emdat data.csv
│
├── extract/
│   └── extract.py
│
├── transform/
│   └── transform.py
│
├── load/
│   └── load.py
│
├── outputs/
│   ├── desastres_por_anio.png
│   ├── desastres_tipo_continente.png
│   ├── desastres_por_mes.png
│   ├── desastres_tipo_anio.png
│   └── afectados_por_continente.png
│
├── TP1_Procesamiento_De_Datos.ipynb
└── README.md
```

💡 Conclusión

Este trabajo permitió aplicar los conceptos fundamentales del procesamiento de datos mediante un flujo ETL, desde la extracción de información hasta su transformación y visualización.

La implementación modular facilitó la organización, reutilización y mantenimiento del código.

Además, el análisis de un dataset real permitió comprender la importancia de la calidad de los datos, el tratamiento de valores faltantes y la utilización de herramientas de visualización para identificar patrones y tendencias que contribuyan a la interpretación de la información.
