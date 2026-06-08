from nexus.storage.duckdb_manager import DuckDBManager
from nexus.ingestion.github.github_client import github_client
from nexus.ingestion.github.models import Repository

db = DuckDBManager()

db.create_tables()

repos = github_client.search_repositories(
    query="stars:>1000 language:Python"
)

count = 0

for repo in repos:

    repository = Repository(
        repo_id=repo.id,
        name=repo.full_name,
        description=repo.description or "",
        stars=repo.stargazers_count,
        language=repo.language or "Unknown",
        topics=[]
    )

    db.insert_repository(repository)

    count += 1

    print(
        f"[{count}] {repository.name}"
    )

    if count >= 100:
        break

print("Done")