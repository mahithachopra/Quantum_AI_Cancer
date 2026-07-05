from sklearn.linear_model import LogisticRegression

from app.ml.trainer import Trainer


model = LogisticRegression(

    max_iter=1000,

    random_state=42

)

Trainer(
    model,
    "logistic"
).train()