import requests
import json

url = "https://api.github.com/repos/python/cpython/contributors"

page = 1
per_page = 100
all_contributors = []

while True:
    params = {
        "page": page,
        "per_page": per_page
    }

    r = requests.get(url, params=params)
    r.raise_for_status()

    data = r.json()

    if not data:
        break

    all_contributors.extend(data)
    print(f"Fetched page {page} ({len(data)} contributors)")

    page += 1

print(f"\nTotal contributors: {len(all_contributors)}")

with open("contributors.json", "w") as f:
    json.dump(all_contributors, f, indent=2)

print("Data saved to contributors.json")