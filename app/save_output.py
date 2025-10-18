import json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
from catboost import CatBoostClassifier


def save_submission(work, out_dir):
    sub = pd.read_parquet(work / "submission.parquet")
    sub.to_csv(out_dir / "sample_submission.csv", index=False)


def save_feature_importances(out_dir, model, work):
    import pandas as pd
    import numpy as np

    cols = None
    test_proc_path = work / "test_proc.parquet"
    if test_proc_path.exists():
        cols = pd.read_parquet(test_proc_path, columns=None).columns.tolist()

    try:
        imp = model.get_feature_importance(type="FeatureImportance")
        imp = np.asarray(imp).ravel()

        if cols is None or len(cols) != len(imp):
            names = getattr(model, "feature_names_", None)
            if names is not None and len(names) == len(imp):
                cols = list(names)
            else:
                cols = [f"f{i}" for i in range(len(imp))]

        df = pd.DataFrame({"feature": cols, "importance": imp})
        top5 = df.sort_values("importance", ascending=False).head(5)
        data = {str(r["feature"]): float(r["importance"]) for _, r in top5.iterrows()}
        (out_dir / "feature_importances_top5.json").write_text(
            json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8"
        )
    except Exception as e:
        (out_dir / "feature_importances_top5.json").write_text(
            json.dumps({"error": f"feature_importance failed: {e}"}), encoding="utf-8"
        )


def save_density_plot(work, out_dir):
    scores_path = work / "scores.npy"
    if not scores_path.exists():
        return
    proba = np.load(scores_path, allow_pickle=True)
    if proba.ndim == 1 or (proba.ndim == 2 and proba.shape[1] == 1):
        scores = proba.ravel()
    elif proba.ndim == 2 and proba.shape[1] == 2:
        scores = proba[:, 1]
    else:
        scores = proba.max(axis=1)
    plt.figure()
    pd.Series(scores).plot(kind="density", title="Score density")
    plt.xlabel("score")
    plt.tight_layout()
    plt.savefig(out_dir / "score_density.png", dpi=150)
    plt.close()


def main():
    work = Path("/app/work")
    out_dir = Path("/app/output")
    out_dir.mkdir(parents=True, exist_ok=True)

    save_submission(work, out_dir)

    art = Path("/app/artifacts")
    model_path = art / "catboost_model.cbm"
    model = CatBoostClassifier()

    if not model_path.exists():
        (out_dir / "feature_importances_top5.json").write_text(
            json.dumps({"error": f"model not found: {model_path}"}), encoding="utf-8"
        )
    else:
        try:
            model.load_model(str(model_path))
            save_feature_importances(out_dir, model, work)
        except Exception as e:
            (out_dir / "feature_importances_top5.json").write_text(
                json.dumps({"error": f"load_model failed: {e}"}), encoding="utf-8"
            )

    save_density_plot(work, out_dir)


if __name__ == "__main__":
    main()
