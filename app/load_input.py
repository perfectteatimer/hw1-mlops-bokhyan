import pandas as pd
from pathlib import Path
from .utils import INPUT_DIR


def load_test():
    path = INPUT_DIR / "test.csv"
    if not path.exists():
        raise FileNotFoundError("Не найден /app/input/test.csv")
    df = pd.read_csv(path)
    return df
