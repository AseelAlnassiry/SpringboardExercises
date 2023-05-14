from flask import Flask, request, redirect, render_template, flash
from flask_debugtoolbar import DebugToolbarExtension
from surveys import surveys

app = Flask(__name__)
app.secret_key = 'hahahahah'
survery_responses = []
survey = surveys["satisfaction"]


@app.route("/")
def index():
    return render_template("index.html", survey=survey)


@app.route("/questions/<int:question_id>")
def render_question(question_id):
    if question_id == len(survery_responses):
        question_data = survey.questions[question_id]
        return render_template(
            "question.html", question_data=question_data, question_id=question_id
        )
    elif len(survery_responses) == len(survey.questions):
        flash("You have already completed the survey!")
        return redirect("/thankyou")
    else:
        flash(
            "You are trying to access a question that has alread been answered or doesnt exist"
        )
        return redirect(f"/questions/{len(survery_responses)}")


@app.route("/answer", methods=["POST"])
def collect_answer():
    res = request.form["question"]
    survery_responses.append(res)
    print(survery_responses)
    if len(survery_responses) < len(survey.questions):
        return redirect(f"/questions/{len(survery_responses)}")
    else:
        return redirect("/thankyou")


@app.route("/thankyou")
def thank_you():
    return render_template("thankyou.html")
