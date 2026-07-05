from sklearn.ensemble import RandomForestClassifier

from app.ml.trainer import Trainer


model = RandomForestClassifier(

    n_estimators=300,

    max_depth=8,

    random_state=42

)

Trainer(
    model,
    "random_forest"
).train()