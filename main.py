from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
app = Flask(__name__)

all_books = []
# create the extension
path = "new-books-collection.db"

# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#app.config['SQLALCHEMY_QUERY_CACHE_SIZE'] = 0
#app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
# initialize the app with the extension

db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String, unique=True, nullable=False)
    author = db.Column(db.String)
    rating = db.Column(db.String)

    def __repr__(self):
        return f'<Book{self.id}>'
#db = sqlite3.connect("books-collection.db")
#cursor = db.cursor()

another_book = Book(
    title="Harry Potter",
    author="J.K. Rowling",
    rating="9.7"
)

with app.app_context():

    db.create_all()



new_book = Book(
                title="Harry Potter",
                author="J.K. Rowling",
                rating="9.7"
            )

with app.app_context():

    db.session.add(new_book)
    db.session.commit()

#---->

@app.route('/')
def home():
    return render_template("index.html", all_books=all_books, len_all_books=len(all_books))


@app.route("/add", methods=["POST","GET"])
def add():
    if request.method == "POST":
        print(type(request.form))
        move_dict = request.form.to_dict()
        all_books.append(move_dict)

    return render_template("add.html")


if __name__ == "__main__":
    app.run(debug=True)

