# NYC Taxi Tip Prediction

Este proyecto busca reproducir y extender un análisis de propinas en viajes en taxi en la ciudad de Nueva York durante el año 2020, utilizando modelos de Machine Learning. El objetivo es estructurar el código del notebook original en un repositorio modular y mantenible, evaluar su rendimiento a lo largo del tiempo y proponer recomendaciones basadas en evidencia.

El análisis se basa en un notebook provisto que explora el uso de características como distancia, duración, tipo de pago y monto total del viaje para predecir si un pasajero dejará propina o no.

## Objetivos

1. Reproducir el análisis original del notebook de predicción de propinas en taxis de NYC (2020), transformando el flujo en un proyecto estructurado y versionado en Git.
2. Modularizar el código en scripts reutilizables y organizados bajo buenas prácticas de ingeniería de software.
3. Evaluar el rendimiento del modelo a lo largo del tiempo, analizando su comportamiento en distintos meses del año.


## Estructura del proyecto

nyc-taxi-tip-prediction/   
├── data/  
│ ├── raw/ # Datos originales (.parquet)  
├── models/ # Modelos entrenados (archivos .pkl)  
├── notebooks/ # Desarrollo y análisis  
│ ├── 01-crivera-exploracion-datos.ipynb  
│ ├── 02-crivera-entrenamiento-modelo.ipynb  
│ ├── 03-crivera-evaluacion-modelo-febrero.ipynb  
│ └── 04-criverav-analisis-mensual-resultados.ipynb  
├── src/ # Código modular del proyecto  
│ ├── data/  
│ ├── features/  
│ └── modeling/  
├── requirements.txt  
└── README.md  


---

## Cómo ejecutar el proyecto

### 1. Clonar el repositorio

git clone https://github.com/RiveraCamilo/nyc-taxi-tip-prediction.git
cd nyc-taxi-tip-prediction

### 2. Crear un entorno virtual (opcional pero recomendado)
python -m venv .venv
.venv\Scripts\activate    # En Windows
source .venv/bin/activate  # En macOS/Linux

### 3. Instalar las dependencias

pip install -r requirements.txt


### 4 Descargar los archivos de datos

Descargar los archivos Parquet manualmente desde:

Enero: https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2020-01.parquet

Febrero: https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2020-02.parquet

Y guardarlos en la carpeta `data/raw/.`

### Requisitos principales
- Python 3.8+
- pandas
- scikit-learn
- matplotlib / seaborn
- joblib
- pyarrow