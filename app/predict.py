import pandas as pd
import numpy as np
from pathlib import Path
from catboost import CatBoostClassifier


def main():
    work = Path("/app/work")
    art = Path("/app/artifacts")
    test = pd.read_parquet(work / "test_proc.parquet")

    model_path = art / "catboost_model.cbm"
    model = CatBoostClassifier()
    model.load_model(str(model_path))

    preds = model.predict(test, prediction_type="Class")
    try:
        proba = model.predict_proba(test)
        if isinstance(proba, list):
            proba = np.array(proba)
    except Exception:
        proba = None

    out = pd.DataFrame({"row_id": np.arange(len(test)), "target": preds})
    out.to_parquet(work / "submission.parquet", index=False)

    if proba is not None:
        np.save(work / "scores.npy", proba)


if __name__ == "__main__":
    main()
