from fastapi import APIRouter, Request
from modles.workspace_service import create_workspace  # your logic

router = APIRouter()

@router.post("/create")
async def create_workspace_route(req: Request):
    data = await req.json()
    create_workspace(data)
    return {"status": "workspace created"}
