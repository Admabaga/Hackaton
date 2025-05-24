from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import RedirectResponse
from app.Api.Routes.Routes import routes
from app.DBConfig.DbConfig import Base
from app.DBConfig.DbConfig import engine

Base.metadata.create_all(bind = engine)
app=FastAPI()
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def main():
    return RedirectResponse(url="/docs")
app.include_router(routes)