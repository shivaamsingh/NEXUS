from dataclasses import dataclass

@dataclass
class Repository:
    repo_id: int
    name: str
    description: str
    stars: int
    language: str
    topics: list[str]