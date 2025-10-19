from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello from Cloud Run"}

@app.get("/health")
async def health():
    return {"status": "healthy"}




