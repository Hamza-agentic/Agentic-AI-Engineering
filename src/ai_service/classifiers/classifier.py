from typing import Protocol


class Classifier(Protocol):
    """Interface for text classification components."""

    def classify(
        self,
        text: str,
    ) -> str:
        """Classify text and return its category."""
        ...