import pandas as pd

EPS = 1e-7

numeric_feat = [
    "pickup_weekday",
    "pickup_hour",
    'work_hours',
    "pickup_minute",
    "passenger_count",
    'trip_distance',
    'trip_time',
    'trip_speed'
]
categorical_feat = [
    "PULocationID",
    "DOLocationID",
    "RatecodeID",
]

features = numeric_feat + categorical_feat

def preprocess(df: pd.DataFrame, target_col: str = "high_tip") -> pd.DataFrame:
    """
    Limpieza básica, creación de features y de la variable objetivo `high_tip`.
    """
    # Evitar división por cero
    df = df[df["fare_amount"] > 0].reset_index(drop=True)

    # Variable objetivo: tip > 20%
    df["tip_fraction"] = df["tip_amount"] / df["fare_amount"]
    df[target_col] = df["tip_fraction"] > 0.2

    # Features temporales y derivadas
    df["pickup_weekday"] = df["tpep_pickup_datetime"].dt.weekday
    df["pickup_hour"] = df["tpep_pickup_datetime"].dt.hour
    df["pickup_minute"] = df["tpep_pickup_datetime"].dt.minute
    df["work_hours"] = (
        (df["pickup_weekday"] >= 0)
        & (df["pickup_weekday"] <= 4)
        & (df["pickup_hour"] >= 8)
        & (df["pickup_hour"] <= 18)
    )
    df["trip_time"] = (df["tpep_dropoff_datetime"] - df["tpep_pickup_datetime"]).dt.seconds
    df["trip_speed"] = df["trip_distance"] / (df["trip_time"] + EPS)

    # Subset final de columnas
    df = df[["tpep_dropoff_datetime"] + features + [target_col]]

    # Conversión de tipos y nulos
    df[features + [target_col]] = df[features + [target_col]].astype("float32").fillna(-1.0)
    df[target_col] = df[target_col].astype("int32")

    return df.reset_index(drop=True)

def get_feature_names() -> list:
    return features