from fastapi import FastAPI, Request, Response
from slack_bolt.adapter.fastapi.async_handler import AsyncSlackRequestHandler
from slack_bot import app as slack_bolt_app

api = FastAPI()
handler = AsyncSlackRequestHandler(slack_bolt_app)

@api.api_route("/slack/events", methods=["POST"])
async def slack_events_proxy(request: Request):
    return await handler.handle(request)

# for testing
@api.get("/")
def root():
    return {"status": "API running"}
