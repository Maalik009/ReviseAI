import json

with open("notes.json", encoding="utf-8") as file:
    topics = json.load(file)

print(topics["Business"]["title"])

print(
    topics["Economics"]["sections"][0]["content"]
)