from modles.workspace_service import create_workspace, WorkspaceCreateRequest

def seed_workspace():
    data = WorkspaceCreateRequest(
        workspace_id="abc123",
        workspace_name="Seeded Workspace",
        token="xoxb-1234"
    )
    create_workspace(data)
    print("Seeded workspace.")

if __name__ == "__main__":
    seed_workspace()
