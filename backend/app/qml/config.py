from app.core.config import settings

# ----------------------------------------
# Directories
# ----------------------------------------

OUTPUT_DIR = settings.MODEL_DIR

# ----------------------------------------
# Quantum Configuration
# ----------------------------------------

N_QUBITS = 6
N_LAYERS = 2
RANDOM_SEED = 42

# ----------------------------------------
# Model Paths
# ----------------------------------------

SCALER_PATH = settings.SCALER_MODEL

PCA_PATH = settings.PCA_MODEL

QSVC_PATH = settings.QSVC_MODEL

QNN_PATH = settings.QNN_MODEL