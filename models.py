from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Resource(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(80))
    topic = db.Column(db.String(80))
    name = db.Column(db.String(80))
    link = db.Column(db.String(200))
    instructor = db.Column(db.String(80))
    college = db.Column(db.String(80))
    lecture_notes = db.Column(db.Boolean)
    videos = db.Column(db.Boolean)
    assignments = db.Column(db.Boolean)
    book = db.Column(db.Boolean)

    def __init__(self, subject, topic, name, link, instructor, college,
                 lecture_notes, videos, assignments, book):
        self.subject = subject
        self.topic = topic
        self.name = name
        self.link = link
        self.instructor = instructor
        self.college = college
        self.lecture_notes = lecture_notes
        self.videos = videos
        self.assignments = assignments
        self.book = book

# get all of the subjects in the database
def get_subjects():
    subjects = []
    for entry in Resource.query.with_entities(Resource.subject).distinct():
        subjects.append(entry[0])
    return subjects

# for a given subject, get all of the topics
def get_topics(subject):
    topics = []
    for entry in Resource.query.filter_by(subject=subject).with_entities(Resource.topic).distinct():
        topics.append(entry[0])
    return topics

def get_resources(topic):
    resources = []
    for resource in Resource.query.filter_by(topic=topic):
        resources.append(resource)
    return resources
