from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from backend.routes import upload, ask, extract


def create_app():
    app = FastAPI(title="Ultra Doc Intelligence")

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(upload.router, prefix="/api")
    app.include_router(ask.router, prefix="/api")
    app.include_router(extract.router, prefix="/api")

    return app


app = create_app()


# ✅ THIS IS THE KEY PART
if __name__ == "__main__":


    uvicorn.run(app, host="127.0.0.1", port=8000)