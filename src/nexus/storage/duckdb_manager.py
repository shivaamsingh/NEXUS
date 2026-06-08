from pathlib import Path

import duckdb


class DuckDBManager:

    def __init__(self):

        Path("data").mkdir(
            exist_ok=True
        )

        self.conn = duckdb.connect(
            "data/nexus.duckdb"
        )

    def create_tables(self):

        self.conn.execute(
            """
            CREATE TABLE IF NOT EXISTS repositories
            (
                repo_id BIGINT,
                name VARCHAR,
                description VARCHAR,
                stars INTEGER,
                language VARCHAR
            )
            """
        )

    def insert_repository(
        self,
        repo
    ):

        self.conn.execute(
            """
            INSERT INTO repositories
            VALUES (?, ?, ?, ?, ?)
            """,
            (
                repo.repo_id,
                repo.name,
                repo.description,
                repo.stars,
                repo.language
            )
        )