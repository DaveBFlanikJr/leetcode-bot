from fastapi import FastAPI, Request, Response
from slack_bolt.adapter.fastapi.async_handler import AsyncSlackRequestHandler
from slack_bot import app as slack_bolt_app
from routes.workspace_router import router as workspace_router

api = FastAPI()
api.include_router(workspace_router, prefix="/workspace")
handler = AsyncSlackRequestHandler(slack_bolt_app)

@api.api_route("/slack/events", methods=["POST"])
async def slack_events_proxy(request: Request):
    return await handler.handle(request)

# for testing
@api.get("/")
def root():
    return {"status": "API running"}
