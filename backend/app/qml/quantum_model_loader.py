import joblib

from app.qml.config import (
    QSVC_PATH,
    QNN_PATH,
)


class QuantumModelLoader:

    def __init__(self):

        self._qsvc = None
        self._qnn = None

    def qsvc(self):

        if self._qsvc is None:

            self._qsvc = joblib.load(
                QSVC_PATH
            )

            print("QSVC loaded.")

        return self._qsvc

    def qnn(self):

        if self._qnn is None:

            self._qnn = joblib.load(
                QNN_PATH
            )

            print("QNN loaded.")

        return self._qnn