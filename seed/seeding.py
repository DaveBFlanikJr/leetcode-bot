from modles.workspace_service import create_workspace, WorkspaceCreateRequest

def seed_workspace():
    data = WorkspaceCreateRequest(
        workspace_id="abc1234",
        workspace_name="Seeded Workspace2",
        token="xoxb-12345"
    )
    create_workspace(data)
    print("Seeded workspace.")

if __name__ == "__main__":
    seed_workspace()
