import os
from dotenv import load_dotenv
import asyncio
import aiohttp
import logging
from logging_config import setup_logging

# logging setup
setup_logging()
# env
load_dotenv()
# Get the user input and fetch the file
OWNER = os.getenv("owner")
REPO = os.getenv("repo")
BRANCH = os.getenv("branch")
FOLDER = os.getenv("folder")
BASE_URL = os.getenv("base_url")

async def fetch_file(desired_problem: int) -> str:
    # Ensure number is formated correctly
    problem = str(desired_problem).zfill(4)
    # create the url
    api_url = f"{BASE_URL}/{OWNER}/{REPO}/contents/{FOLDER}"
    logging.info(f"API URL: {api_url}")

    async with aiohttp.ClientSession() as session:
        async with session.get(api_url) as r:
            if r.status != 200:
                logging.error(f"Error: Received status code {r.status}")
                return "Failed to fetch file list."

            files = await r.json()
            logging.info(f"Received files: {files}")

            for file in files:
                if file["name"].startswith(problem) and file["name"].endswith(".rb"):
                    filename = file["name"]

                    raw_url = f"https://raw.githubusercontent.com/{OWNER}/{REPO}/{BRANCH}/{FOLDER}/{filename}"
                    logging.info(f"RAW_URL: {raw_url}")

                    async with session.get(raw_url) as raw_r:
                        if raw_r.status == 200:
                            content = await raw_r.text()
                            logging.info(f"Successfully fetched content for {filename}")
                            return content
                        else:
                            logging.error(f"Failed to fetch file content for {filename}. Status: {raw_r.status}")
                            return "Failed to fetch file content."
            # fallback
            return "File not found."
