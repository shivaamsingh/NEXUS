import os
from dotenv import load_dotenv
from github import Github

load_dotenv()

TOKEN = os.getenv("GITHUB_TOKEN")

if not TOKEN:
    raise ValueError(
        "GITHUB_TOKEN not found"
    )

github_client = Github(TOKEN)