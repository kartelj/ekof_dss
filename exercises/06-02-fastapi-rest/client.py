"""
A client of the service (the bonus): prints every film with the name of its genre.

Start the service first (python main.py), then, in a second terminal:   python client.py
"""

import httpx2

URL = "http://localhost:8001/api"

response = httpx2.get(URL + "/genres")
response.raise_for_status()

# a dictionary: the id of a genre -> its name
genres = {}
for genre in response.json():
    genres[genre["genre_id"]] = genre["name"]

response = httpx2.get(URL + "/movies")
response.raise_for_status()
for movie in response.json():
    print(f"{movie['title']:28} {movie['year']}  {genres[movie['genre_id']]}")
