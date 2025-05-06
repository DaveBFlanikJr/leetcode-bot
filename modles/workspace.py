from sqlalchemy import Column, Integer, String, DateTime
from modles.db import Base
from datetime import datetime, timezone


class Workspace(Base):
    __tablename__ = "workspaces"
    id = Column(Integer, primary_key=True)
    workspace_id = Column(String, unique=True, nullable=False)
    workspace_name = Column(String)
    bot_token = Column(String, nullable=False)
    installed_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))

    # add a workspace
    @staticmethod
    def add_workspace(session, workspace_id, workspace_name, token):
        workspace = Workspace (
            workspace_id = workspace_id,
            workspace_name = workspace_name,
            bot_token = token
        )
        session.add(workspace)
        session.commit()

    # fetch a workspace
    @staticmethod
    def get_workspace(session, workspace_id):
        return session.query(Workspace).filter_by(workspace_id = workspace_id).first()

    # update a workspace
    @staticmethod
    def update_workspace(session, workspace_id, workspace_name=None, token=None):
        # fetch the workspace
        workspace = session.query(Workspace).filter_by(workspace_id=workspace_id).first()

        if not workspace:
            raise ValueError(f"Workspace with id: {workspace_id} not found.")

        # update the name
        if workspace_name:
            workspace.workspace_name = workspace_name
        # update the token
        if token:
            workspace.bot_token = token

        session.commit()
        return workspace


    # remove a workspace
    @staticmethod
    def remove_workspace(session, workspace_id):
        workspace = session.query(Workspace).filter_by(workspace_id=workspace_id).first()
        # if we have the workspace passed in
        if workspace:
            session.delete(workspace)
            session.commit()
        else:
            raise ValueError(f"Workspace {workspace_id} not found")
