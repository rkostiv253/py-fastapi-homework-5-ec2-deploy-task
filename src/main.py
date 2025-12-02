from fastapi import FastAPI

from src.routes.movies import movie_router
from src.routes.profiles import profile_router
from src.routes.accounts import account_router
app = FastAPI(
    title="Movies homework",
    description="Description of project"
)

api_version_prefix = "/api/v1"

app.include_router(account_router, prefix=f"{api_version_prefix}/accounts", tags=["accounts"])
app.include_router(profile_router, prefix=f"{api_version_prefix}/profiles", tags=["profiles"])
app.include_router(movie_router, prefix=f"{api_version_prefix}/theater", tags=["theater"])
