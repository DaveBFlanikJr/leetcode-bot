import os
from dotenv import load_dotenv
# import asyncio
import re
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
# FOLDER = os.getenv("folder")
BASE_URL = os.getenv("base_url")

# GITHUB TOKEN
github_token = os.getenv("GITHUB_TOKEN")

async def fetch_file(desired_lang: str, desired_problem: int) -> str:
    # print(f"\n[DEBUG] fetch_file() args: lang={desired_lang}, problem={desired_problem}\n")
    # Ensure number is formated correctly
    print(f"\n-------LANG {desired_lang}-------------\n")
    problem = str(desired_problem).zfill(4)
    # create the url
    api_url = f"{BASE_URL}/{OWNER}/{REPO}/contents/{desired_lang}"
    logging.info(f"FULL URL: {BASE_URL}/{OWNER}/{REPO}/contents/{desired_lang}")

    async with aiohttp.ClientSession() as session:
        headers = {
                "Authorization": f"token {github_token}"
            }
        async with session.get(api_url, headers=headers) as r:

            logging.info(f"Response status: {r.status}")
            logging.info(f"Response headers: {r.headers}")

            if r.status != 200:
                logging.error(f"Error: Received status code {r.status}")
                return "Failed to fetch file list."

            files = await r.json()
            logging.info(f"Received files: {files}")

            for file in files:
                if file["name"].startswith(problem) and re.search(r"\.\w+$", file["name"]):
                    filename = file["name"]

                    raw_url = f"https://raw.githubusercontent.com/{OWNER}/{REPO}/{BRANCH}/{desired_lang}/{filename}"
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
