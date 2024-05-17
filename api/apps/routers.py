from fastapi import APIRouter
from api.apps.endpoints.library import library_endpoint

# Initialize the main application router
apps_router = APIRouter()
# Include the library endpoint router in the main application router
# with no prefix and tagging it as "library"
apps_router.include_router(library_endpoint, prefix="", tags=["library"])
