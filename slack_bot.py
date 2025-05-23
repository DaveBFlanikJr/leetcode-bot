import os
from dotenv import load_dotenv
import logging
from logging_config import setup_logging

# slackbolt imports
from slack_bolt.async_app import AsyncApp
# from the leetcode
from leetcode import fetch_file

setup_logging()
# Load required secrets
load_dotenv()
SLACK_BOT_TOKEN = os.getenv("slack_bot_token")
SLACK_SIGNING_SECRET = os.getenv("slack_signing_secret")

# create app
app = AsyncApp(token=SLACK_BOT_TOKEN, signing_secret=SLACK_SIGNING_SECRET)

@app.middleware
async def handle_url_verification(logger, body, next):
    logger.info(f"BODY: {body}")
    if body.get("type") == "url_verification":
        logger.info("Handling URL verification...")
        return {"challenge": body["challenge"]}
    return await next()

@app.middleware
async def log_all_requests(logger, body, next):
    logger.info(f"[SLACK MIDDLEWARE] Received: {body}")
    return await next()

@app.command("/leetcode")
async def handle_leetcode_command(ack, respond, command):
    await ack()
    await respond("Slash command received")
    logging.info(command)
    # get the requested problem number
    text = command.get("text", " ")
    print(text)
    await respond(f"Received raw input: `{text}`")
    logging.info(f"RAW TEXT: '{text}'")
    parts = text.strip().split()
    logging.info(f"PARTS: {parts}")
    # print(text)
    logging.info(f"command text: '{text}', parts: {parts}")

    # convert
    lang = parts[0].lower()
    problem_str = parts[1]

    if not problem_str.isdigit():
        await respond("Please provide a valid problem number (example: `/leetcode 1`).")
        return

    try:
        problem_number = int(problem_str)
    except ValueError as e:
        logging.error(f"Failed to convert problem number: {e}")
        await respond("There was an error converting the problem number.")
        return

    # fetch the solution
    solution = await fetch_file(lang, problem_number)

    # wait for response
    await respond(f"```{solution}```")
