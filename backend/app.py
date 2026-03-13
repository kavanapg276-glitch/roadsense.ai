from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes import upload, potholes, stats

app = FastAPI(title="RoadSense AI Backend")

# CORS (allow frontend to access backend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Root route
@app.get("/")
def read_root():
    return {"message": "RoadSense AI backend running"}

# Health check
@app.get("/health")
def health():
    return {"status": "ok"}

# Include API routes
app.include_router(upload.router, prefix="/api")
app.include_router(potholes.router, prefix="/api")
app.include_router(stats.router, prefix="/api")