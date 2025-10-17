from .load_input import load_test
from .preprocess import transform_text, word_vec, char_vec
from .predict import predict_matrix
from .save_output import save_submission


def main():
    test = load_test()
    X = transform_text(test.text)
    preds = predict_matrix(
        X,
        feature_names_word=word_vec.get_feature_names_out(),
        feature_names_char=char_vec.get_feature_names_out(),
    )
    save_submission(test.id, preds)


if __name__ == "__main__":
    main()
