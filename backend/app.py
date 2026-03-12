from fastapi import FastAPI
<<<<<<< main
from routes.upload import router as upload_router
=======
from fastapi.middleware.cors import CORSMiddleware
from config import settings
>>>>>>> main

from routes import upload
from routes import potholes
from routes import stats


app = FastAPI(

    title=settings.PROJECT_NAME,

    version=settings.VERSION,

    description=settings.DESCRIPTION

)



# ROUTE REGISTRATION

app.include_router(

    upload.router,

    prefix="/api"

)

app.include_router(

    potholes.router,

    prefix="/api"

)

app.include_router(

    stats.router,

    prefix="/api"

)



# HEALTH CHECK (very important for AWS deployment later)

@app.get("/health")

def health_check():

    return {

        "status":"ok",

        "service":"roadsense-backend"

    }



# ROOT ENDPOINT

app.include_router(upload_router)

@app.get("/")

def home():
<<<<<<< main
    return {"message": "API running"}
=======

    return {

        "project":settings.PROJECT_NAME,

        "version":settings.VERSION,

        "status":"running"

    }
app.add_middleware(

    CORSMiddleware,

    allow_origins=["*"],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"],

)
>>>>>>> main
