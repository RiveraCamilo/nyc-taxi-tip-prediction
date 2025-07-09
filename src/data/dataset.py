import pandas as pd

def load_and_clean_data(filepath: str) -> pd.DataFrame:
    # Cargar archivo Parquet
    df = pd.read_parquet(filepath)

    return df