import os
from dotenv import load_dotenv
import asyncio
import aiohttp


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
    print(f"API URL: {api_url}")

    async with aiohttp.ClientSession() as session:
        async with session.get(api_url) as r:
            if r.status != 200:
                print(f"Error: Received status code {r.status}")
                return "Failed to fetch file list."

            files = await r.json()
            # print(files)

            for file in files:
                if file["name"].startswith(problem) and file["name"].endswith(".rb"):
                    filename = file["name"]

                    raw_url = f"https://raw.githubusercontent.com/{OWNER}/{REPO}/{BRANCH}/{FOLDER}/{filename}"
                    print(f"RAW_URL: {raw_url}")

                    async with session.get(raw_url) as raw_r:
                        if raw_r.status == 200:
                            return await raw_r.text()
                        else:
                            return "Failed to fetch file content."
            # fallback
            return "File not found."

print(asyncio.run(fetch_file(1)))
