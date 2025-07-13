import joblib
from sklearn.metrics import f1_score, classification_report

def evaluate_model(model_path, X_test, y_test, verbose=True):
    model = joblib.load(model_path)
    y_pred = model.predict(X_test)

    if verbose:
        print(classification_report(y_test, y_pred))

    score = f1_score(y_test, y_pred)
    return score
