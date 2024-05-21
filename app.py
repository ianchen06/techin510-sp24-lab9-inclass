from flask import Flask, request, render_template

app = Flask(__name__)

db = [
    {"id": 1, "name": "photo1"},
    {"id": 2, "name": "photo2"},
    {"id": 3, "name": "photo3"},
]


@app.route("/")
def index():
    return render_template("index.html", photos=db)


@app.route("/photos", methods=["GET", "POST"])
def photos():
    if request.method == "POST":
        # save the photo
        # redirect to the photos page
        return "create photos"

    # show the list of photos
    return "list photos"


@app.route("/photos/new", methods=["GET"])
def new_photos():
    return "new photo"


@app.route("/photos/<int:id>", methods=["GET", "PUT", "DELETE"])
def show_photo(id):
    return "photo details for id: %s" % id


@app.route("/photos/<int:id>/edit", methods=["GET"])
def edit_photo(id):
    return "edit photo for id: %s" % id
