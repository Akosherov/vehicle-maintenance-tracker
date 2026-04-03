from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

from common.exceptions import AppException
from routers.users import users_router
from routers.clients import clients_router


app = FastAPI(title="Vehicle Maintenance Tracker")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.exception_handler(AppException)
async def app_exception_handler(request, exc: AppException):
    return JSONResponse(status_code=exc.status_code, content={"detail": exc.message})


app.include_router(users_router)
app.include_router(clients_router)
