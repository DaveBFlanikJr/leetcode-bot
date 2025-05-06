from pydantic import BaseModel
from typing import List, Dict, Optional, Union, Any
from modles.workspace import Workspace
from modles.db import SessionLocal


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
    session = SessionLocal()
    try:
        Workspace.add_workspace(
            session,
            workspace_id=data.workspace_id,
            workspace_name=data.workspace_name,
            token=data.token
        )
    finally:
        session.close()


def get_workspace(data: WorkspaceKey):
    session = SessionLocal()
    try:
        return Workspace.get_workspace(session, workspace_id=data.workspace_id)
    finally:
        session.close()

def update_workspace(data: WorkspaceUpdateRequest):
    session = SessionLocal()
    try:
        Workspace.update_workspace(
            session,
            workspace_id=data.workspace_id,
            workspace_name=data.workspace_name,
            token=data.token
        )
    finally:
        session.close()

def delete_workspace(data: WorkspaceKey):
    session = SessionLocal()
    try:
        Workspace.remove_workspace(session, workspace_id=data.workspace_id)
    finally:
        session.close()
