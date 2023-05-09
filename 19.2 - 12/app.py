from flask import Flask, request, render_template
import stories

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html", story = stories.story)


@app.route("/story")
def story():
    story = stories.story.generate(request.args)
    return render_template("story.html", story=story)

