from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier

from app.ml.experiment.cross_validation import CrossValidator


def main():

    cv = CrossValidator()

    models = {

        "Logistic Regression":
            LogisticRegression(
                max_iter=1000,
                random_state=42
            ),

        "Random Forest":
            RandomForestClassifier(
                n_estimators=300,
                random_state=42
            ),

        "XGBoost":
            XGBClassifier(
                n_estimators=300,
                learning_rate=0.05,
                max_depth=5,
                eval_metric="logloss",
                random_state=42
            )
    }

    print("\n")
    print("=" * 70)
    print("CLASSICAL ML BENCHMARK")
    print("=" * 70)

    results = {}

    for name, model in models.items():

        print(f"\n{name}")
        print("-" * 70)

        results[name] = cv.evaluate(model)

    print("\n")
    print("=" * 70)
    print("SUMMARY")
    print("=" * 70)

    for model_name, metrics in results.items():

        print(f"\n{model_name}")

        for metric, (mean, std) in metrics.items():

            print(
                f"{metric:<12}"
                f"{mean:.4f} ± {std:.4f}"
            )


if __name__ == "__main__":
    main()