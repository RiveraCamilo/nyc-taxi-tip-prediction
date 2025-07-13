import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

def train_model(df, features, target_col, model_output_path):
    X = df[features]
    y = df[target_col]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, stratify=y, test_size=0.2, random_state=42
    )

    rfc = RandomForestClassifier(random_state=42)
    rfc.fit(X_train, y_train)

    joblib.dump(rfc, model_output_path)

    return rfc, X_test, y_test
