import json
from pathlib import Path

value = int(input("Enter a number: "))

config_path = Path("config.json")

with config_path.open("r", encoding="utf-8") as file:
    config = json.load(file)

config["threshold"] = value

with config_path.open("w", encoding="utf-8") as file:
    json.dump(config, file, indent=2)

try:
    with config_path.open("r", encoding="utf-8") as file:
        json.load(file)
    print("✅ config.json was updated successfully and contains valid JSON.")
except json.JSONDecodeError as e:
    print(f"❌ Invalid JSON: {e}")