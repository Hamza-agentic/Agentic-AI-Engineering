from fastapi import FastAPI

from ai_service.api.routes import router
from ai_service.config.settings import get_settings
from ai_service.utils.logging import get_logger, setup_logging

settings = get_settings()
setup_logging(settings.log_level)
logger = get_logger(__name__)

app = FastAPI(
    title="Week 04 AI Service",
    description="AI service demonstrating interfaces and dependency injection",
    version="1.0.0",
)

app.include_router(router)

logger.info("Starting in '%s' environment", settings.app_env)