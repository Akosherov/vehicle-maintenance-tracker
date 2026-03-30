from fastapi import FastAPI
from fastapi.responses import JSONResponse

from routers.users import users_router
from common.exceptions import AppException


app = FastAPI(title="Vehicle Maintenance Tracker")


@app.exception_handler(AppException)
async def app_exception_handler(request, exc: AppException):
    return JSONResponse(status_code=exc.status_code, content={"detail": exc.message})


app.include_router(users_router)
