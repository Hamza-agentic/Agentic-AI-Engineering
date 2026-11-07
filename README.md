# Week 04 - Containerized AI Service

Agentic AI Systems Engineering

## Purpose

This project demonstrates software architecture and cloud/container
foundations by converting an AI-related Python application into a
containerized REST API service.

## Technologies

- Python 3.12
- FastAPI
- Uvicorn
- Docker
- Docker Compose
- Pytest

## Project Structure

```text
src/
└── ai_service/
    ├── main.py
    ├── api/
    │   └── routes.py
    ├── services/
    │   └── ai_service.py
    ├── config/
    │   └── settings.py
    └── utils/
        └── logging.py
