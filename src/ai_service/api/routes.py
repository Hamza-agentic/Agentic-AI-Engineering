from fastapi import APIRouter, HTTPException

from ai_service.classifiers.rule_classifier import RuleClassifier
from ai_service.config.settings import get_settings
from ai_service.services.ai_service import AIService

router = APIRouter()

settings = get_settings()
classifier = RuleClassifier()
ai_service = AIService(classifier)


@router.get("/")
def root():
    return {
        "message": "AI Service is running",
        "version": "1.0.0",
        "environment": settings.app_env,
    }


@router.get("/health")
def health():
    return {"status": "ok"}


@router.post("/classify")
def classify(text: str):
    try:
        return ai_service.classify(text)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc))