from sklearn.ensemble import RandomForestClassifier

from app.ml.experiment.hyperparameter_search import HyperparameterSearch

search = HyperparameterSearch()

params = {

    "n_estimators":[
        100,
        200,
        300,
        500
    ],

    "max_depth":[
        None,
        5,
        8,
        10,
        15
    ],

    "min_samples_split":[
        2,
        5,
        10
    ],

    "min_samples_leaf":[
        1,
        2,
        4
    ],

    "max_features":[
        "sqrt",
        "log2",
        None
    ]

}

search.optimize(

    RandomForestClassifier(random_state=42),

    params,

    "random_forest"

)