# add resources from a csv file
# fields are subject, topic, name, link, instructor, college, notes, videos
# assignments, books
import sys
from main import app, db
from models import Resource

def add_from_csv(txt_file):
    f = open(txt_file, 'r')
    content = f.readlines()
    f.close()

    print len(content)

    # read each line in the tab-separated txt file and add the a resource for that line
    for line in content:
        line = line.strip().split('\t')

        if line[10]:
            description = line[10]
        else:
            description = "No description available"

        resource = Resource(subject=line[0], topic=line[1], name=line[2],
                            link=line[3], instructor=line[4], college=line[5],
                            lecture_notes=line[6] == "TRUE",
                            videos=line[7] == "TRUE",
                            assignments=line[8] == "TRUE",
                            book=line[9] == "TRUE", description=description)

        db.session.add(resource)

    db.session.commit()

if __name__ == "__main__":
    # if we run this program standalone, take the filename to be
    # the first argument and use that .csv file to add resources
    if len(sys.argv) == 2:
        filename = sys.argv[1]
        with app.app_context():
            add_from_csv(filename)
