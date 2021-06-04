from fastapi import APIRouter

from producer_consumer_txt.routes.v1 import process


rota_v1 = APIRouter()
rota_v1.include_router(process.route, prefix="/process", tags=["Process"])
