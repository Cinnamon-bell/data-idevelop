import requests, json
r = requests.get("https://api.github.com/repos/python/cpython")
data = r.json()
print(data["stargazers_count"], "stars")
with open("snapshot.json", "w") as f:
    json.dump(data, f, indent=2)