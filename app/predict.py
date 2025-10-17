import joblib
import numpy as np
import json
from pathlib import Path
import matplotlib.pyplot as plt
from .utils import OUTPUT_DIR

model = joblib.load("/app/artifacts/model.joblib")


def predict_matrix(X, feature_names_word, feature_names_char):
    y = model.predict(X)

    if hasattr(model, "decision_function"):
        scores = model.decision_function(X)
        plt.figure()
        plt.hist(scores, bins=50, density=True)
        plt.title("Density of decision scores")
        plt.xlabel("score")
        plt.ylabel("density")
        plt.tight_layout()
        plt.savefig(OUTPUT_DIR / "scores_density.png", dpi=150)

    names = list(feature_names_word) + list(feature_names_char)
    if hasattr(model, "coef_"):
        coefs = model.coef_
        if coefs.ndim == 1:
            imp = np.abs(coefs)
        else:
            imp = np.max(np.abs(coefs), axis=0)

        n = min(len(names), imp.shape[-1])
        imp = imp[:n]
        names = names[:n]

        top = np.argsort(imp)[::-1][:5]
        imps = {names[i]: float(imp[i]) for i in top}

        OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
        with open(OUTPUT_DIR / "importances.json", "w", encoding="utf-8") as f:
            json.dump(imps, f, ensure_ascii=False, indent=2)
    return y
