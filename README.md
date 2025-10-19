# FastAPI Demo PoC

Simple FastAPI application for testing Cloud Run deployments.

## Current Status

- Backstage Entity: Configured
- Cloud Run Service: Not deployed
- Deployment Required: Yes

## Structure

- `main.py` - FastAPI application with health check
- `requirements.txt` - Python dependencies
- `Dockerfile` - Container configuration
- `catalog-info.yaml` - Backstage entity definition

## Endpoints

- `GET /` - Returns greeting message
- `GET /health` - Health check endpoint

## Local Run

```bash
pip install -r requirements.txt
uvicorn main:app --reload --port 8080
```

## Docker Build

```bash
docker build -t fastapi-demo-poc .
docker run -p 8080:8080 fastapi-demo-poc
```

## Cloud Run Deploy

```bash
gcloud run deploy fastapi-demo-poc \
  --source . \
  --region us-central1 \
  --allow-unauthenticated
```

## Backstage Integration

Entity visible at:
http://localhost:3000/catalog/default/proofofconcept/fastapi-demo-poc

Current State:
- Entity loaded successfully
- Cloud Run section shows "No Cloud Run service found"
- Deploy service to populate Cloud Run data

After Deployment:
- Cloud Run service status
- Live deployment URL
- Container image info
- Resource allocation
- Auto-refresh every 30s

