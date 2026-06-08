from github_client import github_client
import json
import os

QUERY = "stars:>1000 language:Python"

repos = github_client.search_repositories(
    query=QUERY
)

os.makedirs(
    "../../data/raw/github",
    exist_ok=True
)

for i, repo in enumerate(repos[:100]):

    repo_data = {

        "id": repo.id,
        "name": repo.name,
        "full_name": repo.full_name,
        "description": repo.description,
        "stars": repo.stargazers_count,
        "language": repo.language,
        "topics": repo.get_topics()
    }

    with open(
        f"../../data/raw/github/repo_{i}.json",
        "w"
    ) as f:

        json.dump(
            repo_data,
            f,
            indent=4
        )

print("Done")