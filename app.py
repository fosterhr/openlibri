from flask import Flask, render_template, redirect
from json import load

APP_NAME = "OpenLibri"

app = Flask(__name__)
books = load(open("static/books/manifest.json", "r"))

@app.route("/")
def home():
    return render_template("library.html", app_name=APP_NAME, books=books)

@app.route("/view/")
def _view():
    return redirect("/", code=302)

@app.route("/view/<id>")
def view(id):
    for book in books:
        if book["id"] == id:
            return render_template("view.html", app_name=APP_NAME, book_name=book["title"], file_name=book["file"])
    return "Error 404", 404

app.run(debug=True, port=80)