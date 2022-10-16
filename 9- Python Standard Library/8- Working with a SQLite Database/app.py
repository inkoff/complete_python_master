import sqlite3
import json
from pathlib import Path


movies = json.loads(Path("movies.json").read_text())
# print(movies)

# with sqlite3.connect("db.sqlite") as db:
#     com = "INSERT INTO movies VALUES(?, ?)"
#     for m in movies:
#         db.execute(com, tuple(m.values()))
#     db.commit()
with sqlite3.connect("db.sqlite") as db:
    com = "SELECT * FROM `movies`"
    cursor = db.execute(com)
    # for row in cursor:
    #     print(row)
    movies = cursor.fetchall()
    print(movies)
