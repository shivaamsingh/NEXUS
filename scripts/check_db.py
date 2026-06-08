import duckdb

conn = duckdb.connect("data/nexus.duckdb")

count = conn.execute(
    """
    SELECT COUNT(*)
    FROM repositories
    """
).fetchone()[0]

print(f"Repositories: {count}")

print()

rows = conn.execute(
    """
    SELECT *
    FROM repositories
    LIMIT 5
    """
).fetchall()

for row in rows:
    print(row)