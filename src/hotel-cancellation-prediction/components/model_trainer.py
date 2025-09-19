import os
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

class ModelTrainer:
    def __init__(self):
        self.model = RandomForestClassifier(
            n_estimators=200,
            max_depth=15,
            min_samples_split=5,
            min_samples_leaf=2,
            max_features="sqrt",
            n_jobs=-1,
            random_state=42
        )
        self.artifact_dir = "artifacts"
        os.makedirs(self.artifact_dir, exist_ok=True)

    def initiate_model_training(self, X, y, transformer=None):
        """
        Train the RandomForest model, evaluate, and save artifacts.
        """
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )

        # Fit model
        self.model.fit(X_train, y_train)

        # Evaluate
        train_acc = accuracy_score(y_train, self.model.predict(X_train))
        test_acc = accuracy_score(y_test, self.model.predict(X_test))

        # Save model
        joblib.dump(self.model, os.path.join(self.artifact_dir, "model.pkl"))

        # Save transformer with feature_columns
        if transformer:
            if getattr(transformer, "feature_columns", None) is None:
                raise ValueError(
                    "Transformer.feature_columns is None — did you call initiate_data_transformation(df, training=True)?"
                )
            joblib.dump(transformer, os.path.join(self.artifact_dir, "transformer.pkl"))

        return {"train_acc": train_acc, "test_acc": test_acc}
