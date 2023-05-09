from flask import Flask, request, render_template
import stories

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html", story = stories.story)

