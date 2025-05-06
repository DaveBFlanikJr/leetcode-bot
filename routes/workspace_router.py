from fastapi import APIRouter, status, HTTPException
from modles.workspace_service import (
    create_workspace,
    update_workspace,
    delete_workspace,
    get_workspace,
    WorkspaceCreateRequest,
    WorkspaceUpdateRequest,
    WorkspaceKey
)
router = APIRouter()

@router.post("/create", status_code=status.HTTP_201_CREATED)
async def create_workspace_route(data: WorkspaceCreateRequest):
    create_workspace(data)
    return {"status": "created"}

@router.post("/get")
async def get_workspace_route(data: WorkspaceKey):
    workspace = get_workspace(data)
    if workspace:
        return workspace
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Workspace not found")

@router.post("/update")
async def update_workspace_route(data: WorkspaceUpdateRequest):
    update_workspace(data)
    return {"status": "updated"}

@router.post("/delete")
async def delete_workspace_route(data: WorkspaceKey):
    delete_workspace(data)
    return {"status": "deleted"}
