from flask import Flask, render_template
import json
from pathlib import Path

app = Flask(__name__)

notes_file = Path(__file__).parent / "notes.json"

with open(notes_file, "r", encoding="utf-8") as file:
    notes = json.load(file)


def load_topics():
    """Load revision topics from the JSON file."""
    with open(NOTES_FILE, encoding="utf-8") as file:
        return json.load(file)


def get_topic(topic_id):
    """Return a specific topic, or None if it doesn't exist."""
    topics = load_topics()
    return topics.get(topic_id)


def get_topic_titles():
    """Return the ID and title of every available topic."""
    topics = load_topics()
    return [
        (topic_id, topic["title"])
        for topic_id, topic in topics.items()
    ]


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/topics")
def topics():
    return render_template("topics.html", notes=notes)


@app.route("/topics/<topic_id>")
def topic_page(topic_id):
    topic = get_topic(topic_id)

    if topic is None:
        abort(404)

    return render_template(
        "topic.html",
        topic=topic
    )


def main():
    app.run()


if __name__ == "__main__":
    main()
