from ai_service.classifiers.classifier import Classifier
from ai_service.utils.logging import get_logger

logger = get_logger(__name__)


class AIService:
    def __init__(self, classifier: Classifier) -> None:
        self.classifier = classifier

    def classify(self, text: str) -> dict[str, str]:
        if not text.strip():
            logger.warning("Rejected empty text")
            raise ValueError("Text cannot be empty.")

        category = self.classifier.classify(text)
        logger.info("Classified text as '%s'", category)

        return {"text": text, "category": category}