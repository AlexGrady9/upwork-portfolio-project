"""Main application entry point."""

import logging
from contextlib import asynccontextmanager
from pathlib import Path

from fastapi import FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from project_name.config.settings import get_settings
from project_name.api.v1 import router as api_v1_router

settings = get_settings()

# Set up logging for the whole app (so you always know what's going on)
logging.basicConfig(
    level=getattr(logging, settings.LOG_LEVEL),
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)

logger = logging.getLogger(__name__)

# Path to static files (images, CSS, etc.)
STATIC_DIR = Path(__file__).parent / "static"


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifespan events."""
    logger.info(f"Starting Upwork Portfolio Project v{app.version}...")
    logger.info(f"Debug mode: {settings.DEBUG}")
    logger.info(f"Log level: {settings.LOG_LEVEL}")
    logger.info(
        f"Environment: {'development' if settings.DEBUG else 'production'}")

    try:
        yield
    finally:
        logger.info("Shutting down application...")


def create_app() -> FastAPI:
    """Create FastAPI application with all configurations."""
    app = FastAPI(
        title="Upwork Portfolio Project",
        description="Professional Python API showcasing best practices",
        version="1.0.0",
        lifespan=lifespan,
    )

    # Serve static files if the folder exists (handy for docs, images, etc.)
    if STATIC_DIR.exists():
        app.mount("/static", StaticFiles(directory=str(STATIC_DIR)), name="static")

    # Allow cross-origin requests (CORS) for local dev or production
    allowed_origins = (
        ["*"] if settings.DEBUG
        else ["https://yourdomain.com", "http://localhost:3000"]
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=allowed_origins,
        allow_credentials=True,
        allow_methods=["GET", "POST", "PUT", "DELETE", "PATCH"],
        allow_headers=["*"],
    )

    # Register all API routes (keeps things modular)
    app.include_router(api_v1_router, prefix="/api/v1", tags=["API v1"])

    return app


# Actually create the FastAPI app instance (so uvicorn can find it)
app = create_app()


@app.get("/favicon.ico", include_in_schema=False)
async def favicon():
    """Handle favicon requests."""
    return Response(status_code=204)  # No Content (browsers love to ask for this)


@app.get("/health", tags=["Health"])
async def health_check():
    """Health check endpoint."""
    return {
        "status": "healthy",
        "version": "1.0.0",
        "debug": settings.DEBUG,
        "log_level": settings.LOG_LEVEL,
    }


@app.get("/", tags=["Root"])
async def root():
    """Root endpoint with API information."""
    return {
        "message": "Welcome to Upwork Portfolio Project API",
        "version": "1.0.0",
        "endpoints": {
            "health": "/health",
            "docs": "/docs",
            "api": "/api/v1",
        },
        "features": [
            "FastAPI with async support",
            "SQLAlchemy ORM integration",
            "JWT Authentication",
            "Comprehensive testing",
            "Docker support",
            "Professional code structure"
        ]
    }


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8000,
        reload=settings.DEBUG,
        log_level=settings.LOG_LEVEL.lower(),
    )
