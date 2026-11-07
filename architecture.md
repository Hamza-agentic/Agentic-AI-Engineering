# Week 04 AI Service Architecture

## 1. Overview

This project demonstrates how an AI-related Python application can be transformed
into a structured API service and packaged as a Docker container.

The system uses a simple classification capability to demonstrate software
architecture and deployment concepts.

## 2. Architecture

Client
   |
   | HTTP
   v
FastAPI API
   |
   v
AIService
   |
   v
Classification Logic

Configuration and Logging support the application.

## 3. Layers

### API Layer

File:

src/ai_service/api/routes.py

Responsibilities:

- HTTP endpoints
- Request handling
- HTTP error handling
- Response generation

### Service Layer

File:

src/ai_service/services/ai_service.py

Responsibilities:

- Application logic
- Classification
- Service-level validation

### Configuration Layer

File:

src/ai_service/config/settings.py

Responsibilities:

- Environment-based configuration
- Application settings

### Utility Layer

File:

src/ai_service/utils/logging.py

Responsibilities:

- Application logging configuration

## 4. Container Architecture

Host Machine
    |
    v
Docker
    |
    v
AI Service Container
    |
    v
Uvicorn
    |
    v
FastAPI
    |
    v
AIService

## 5. Port Mapping

Host port:

8000

Container port:

8000

Mapping:

8000:8000

## 6. Configuration

Configuration is provided through environment variables.

Example:

APP_NAME=Week 04 AI Service
APP_VERSION=1.0.0
DEBUG=false
HOST=0.0.0.0
PORT=8000

## 7. Health Check

The endpoint:

GET /health

returns:

{
    "status": "healthy"
}

This allows deployment infrastructure to determine whether
the application is responding.

## 8. Future Evolution

The rule-based classification logic can later be replaced with:

- Machine learning model
- LLM service
- External AI API
- Agentic workflow

The API architecture can remain unchanged.

Future architecture:

Client
   |
   v
API
   |
   v
AI Service
   |
   +---- ML Model
   |
   +---- LLM
   |
   +---- External API
   |
   +---- Agent

This demonstrates separation of concerns and replaceable AI components.
