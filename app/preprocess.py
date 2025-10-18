import pandas as pd
from pathlib import Path


def preprocess(df):
    df["transaction_time"] = pd.to_datetime(df["transaction_time"], errors="coerce")
    df["hour"] = df["transaction_time"].dt.hour
    df["dayofweek"] = df["transaction_time"].dt.dayofweek
    df["month"] = df["transaction_time"].dt.month
    df = df.drop(columns=["transaction_time"])
    return df


def main():
    work = Path("/app/work")
    test = pd.read_parquet(work / "test.parquet")
    test_proc = preprocess(test)
    test_proc.to_parquet(work / "test_proc.parquet", index=False)


if __name__ == "__main__":
    main()
