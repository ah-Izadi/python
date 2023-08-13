import json
from pathlib import Path

movies = [
    {"id": 1, "title": "Terminator", "year": 1984},
    {"id": 2, "title": "Kindergarten Cop", "year": 1990},
]

data = json.dumps(movies)
print(data)
print(type(data))

Path("C:/Users/Dell/Desktop/movies.json").write_text(data)


#reading
data = Path('C:/Users/Dell/Desktop/movies.json').read_text()
movies = json.loads(data)
print(movies)
print(movies[0]['title'])