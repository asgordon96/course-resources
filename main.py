from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from models import db, Resource, get_subjects, get_topics, get_resources

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root@localhost/courseresources"
app.config['DEBUG'] = True
db.init_app(app)

@app.route('/')
def index():
    subjects = get_subjects()
    return render_template("index.html", subjects=subjects)

# this is only used with AJAX
@app.route("/getTopics", methods=["GET"])
def getTopics():
    subject = request.args.get("subject")
    topics = get_topics(subject)
    return render_template("topicList.html", topics=topics)

@app.route("/resources/<topic>")
def getResources(topic):
    resources = get_resources(topic)
    return render_template("resources.html", resources=resources)


if __name__ == "__main__":
    app.run()
