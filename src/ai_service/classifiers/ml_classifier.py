class MLClassifier:
    """Example placeholder for a trained ML classifier."""

    def __init__(self, model):
        self.model = model

    def classify(
        self,
        text: str,
    ) -> str:

        prediction = self.model.predict(
            [text]
        )

        return str(
            prediction[0]
        )