from pydantic import BaseModel
from typing import List, Dict, Optional, Union, Any
from modles.workspace import Workspace
from modles.db import SessionLocal, get_db_session


class WorkspaceCreateRequest(BaseModel):
    workspace_id: str
    workspace_name: str
    token: str

class WorkspaceUpdateRequest(BaseModel):
    workspace_id: str
    workspace_name: Optional[str] = None
    token: Optional[str] = None

class WorkspaceKey(BaseModel):
    workspace_id: str

def create_workspace(data: WorkspaceCreateRequest):
    with get_db_session() as session:
        Workspace.add_workspace(
            session,
            workspace_id=data.workspace_id,
            workspace_name=data.workspace_name,
            token=data.token
        )

def get_workspace(data: WorkspaceKey):
    with get_db_session() as session:
        return Workspace.get_workspace(session, workspace_id=data.workspace_id)


def update_workspace(data: WorkspaceUpdateRequest):
    with get_db_session() as session:
        Workspace.update_workspace(
            session,
            workspace_id=data.workspace_id,
            workspace_name=data.workspace_name,
            token=data.token
        )

def delete_workspace(data: WorkspaceKey):
    with get_db_session() as session:
        Workspace.remove_workspace(session, workspace_id=data.workspace_id)
