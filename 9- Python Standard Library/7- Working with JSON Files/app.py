import json
from pathlib import Path

# movies = [
#     {"id": 1, "title": "Name 1"},
#     {"id": 2, "title": "Name 2"},
#     {"id": 3, "title": "Name 3"},

# ]

# data = json.dumps(movies)
# Path("movies.json").write_text(data)

data = Path("movies.json").read_text()
movies = json.loads(data)
print(movies)
print(movies[0])
print(movies[0]["title"])
