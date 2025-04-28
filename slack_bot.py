import os
from dotenv import load_dotenv

# slackbolt imports
from slack_bolt.async_app import AsyncApp
# from the leetcode
from leetcode import fetch_file


# Load required secrets
load_dotenv()
SLACK_BOT_TOKEN = os.getenv("slack_bot_token")
SLACK_SIGNING_SECRET = os.getenv("slack_signing_secret")

# create app
app = AsyncApp(token=SLACK_BOT_TOKEN, signing_secret=SLACK_SIGNING_SECRET)

@app.command("/leetcode")
async def handle_leetcode_command(ack, respond, command):
    await ack()

    # get the requested problem number
    text = command.get('text')

    if not text or not text.isdigit():
        await respond("Please provide a valid problem number (example: `/leetcode 1`).")
        return

    # convert
    problem_number = int(text)

    # fetch the solution
    solution = await fetch_file(problem_number)

    # wait for response
    await respond(f"```{solution}```")
