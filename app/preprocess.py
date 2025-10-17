import joblib
from scipy.sparse import hstack

word_vec = joblib.load("/app/artifacts/word_vec.joblib")
char_vec = joblib.load("/app/artifacts/char_vec.joblib")


def transform_text(series):
    xw = word_vec.transform(series.fillna(""))
    xc = char_vec.transform(series.fillna(""))
    return hstack([xw, xc])
