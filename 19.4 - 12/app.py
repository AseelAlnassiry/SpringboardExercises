from flask import Flask, request, redirect, render_template, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from surveys import surveys

app = Flask(__name__)
app.secret_key = "hahahahah"
survey = surveys["satisfaction"]


@app.route("/")
def index():
    return render_template("index.html", survey=survey)


@app.post("/start")
def start_survey():
    session["responses"] = []
    
    return redirect("/questions/0")


@app.route("/questions/<int:question_id>")
def render_question(question_id):
    print(session["responses"])
    if question_id == len(session["responses"]) and question_id < len(survey.questions):

        question_data = survey.questions[question_id]
        return render_template(
            "question.html", question_data=question_data, question_id=question_id
        )
    elif len(session["responses"]) == len(survey.questions):
        flash("You have already completed the survey!")
        return redirect("/thankyou")
    else:
        flash(
            "You are trying to access a question that has alread been answered or doesnt exist"
        )
        return redirect(f"/questions/{len(session['responses'])}")


@app.route("/answer", methods=["POST"])
def collect_answer():
    res = request.form["question"]
    responses = session["responses"]
    if len(session["responses"]) < len(survey.questions):
        responses.append(res)
        session["responses"] = responses
        return redirect(f"/questions/{len(session['responses'])}")
    else:
        return redirect("/thankyou")


@app.route("/thankyou")
def thank_you():
    print(session['responses'])
    return render_template("thankyou.html")
