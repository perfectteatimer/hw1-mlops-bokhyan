import pandas as pd
from pathlib import Path


def main():
    in_dir = Path("/app/input")
    work = Path("/app/work")
    work.mkdir(parents=True, exist_ok=True)
    p = in_dir / "test.csv"
    if not p.exists():
        raise FileNotFoundError("на нашелся /app/input/test.csv")
    df = pd.read_csv(p)
    df.to_parquet(work / "test.parquet", index=False)


if __name__ == "__main__":
    main()
