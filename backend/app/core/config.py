from pathlib import Path

from pydantic_settings import BaseSettings


BASE_DIR = Path(__file__).resolve().parents[2]


class Settings(BaseSettings):

    # ---------------------------------
    # API
    # ---------------------------------

    API_NAME: str = "Quantum AI Cancer Platform"

    API_VERSION: str = "1.0"

    DEBUG: bool = False

    LOG_LEVEL: str = "INFO"

    # ---------------------------------
    # PostgreSQL
    # ---------------------------------

    POSTGRES_HOST: str

    POSTGRES_PORT: int

    POSTGRES_DB: str

    POSTGRES_USER: str

    POSTGRES_PASSWORD: str

    # ---------------------------------
    # Neo4j
    # ---------------------------------

    NEO4J_URI: str

    NEO4J_USER: str

    NEO4J_PASSWORD: str

    # ---------------------------------
    # Directories
    # ---------------------------------

    BASE_DIR: Path = BASE_DIR

    DATASET_DIR: Path = BASE_DIR / "datasets"

    OUTPUT_DIR: Path = BASE_DIR / "outputs"

    LOG_DIR: Path = BASE_DIR / "logs"

    MODEL_DIR: Path = BASE_DIR / "app" / "qml" / "output"

    # ---------------------------------
    # ML Models
    # ---------------------------------

    ML_MODEL_DIR: Path = BASE_DIR / "app" / "ml" / "models"

    RF_MODEL: Path = ML_MODEL_DIR / "random_forest_best.pkl"

    XGB_MODEL: Path = ML_MODEL_DIR / "xgboost_best.pkl"

    LR_MODEL: Path = ML_MODEL_DIR / "logistic.pkl"

    # ---------------------------------
    # Quantum Models
    # ---------------------------------

    QSVC_MODEL: Path = MODEL_DIR / "qsvc.pkl"

    QNN_MODEL: Path = MODEL_DIR / "qnn.pkl"

    SCALER_MODEL: Path = MODEL_DIR / "scaler.pkl"

    PCA_MODEL: Path = MODEL_DIR / "pca.pkl"
    class Config:

        env_file = ".env"


settings = Settings()