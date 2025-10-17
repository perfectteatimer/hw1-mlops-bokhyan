import pandas as pd
from .utils import OUTPUT_DIR


def save_submission(ids, preds, filename="sample_submission.csv"):
    sub = pd.DataFrame({"id": ids, "target": preds})
    sub.to_csv(OUTPUT_DIR / filename, index=False)
