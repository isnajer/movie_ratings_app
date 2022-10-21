"""Models for movie ratings app."""

from flask_sqlalchemy import SQLAlchemy
# from datetime import datetime

db = SQLAlchemy()


class User(db.Model):
    """A user."""

    __tablename__ = 'users'

    user_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    # nullable MAY be an error later on....
    
    ratings = db.relationship("Rating", back_populates="user")

    def __repr__(self):
        return f'<User user_id={self.user_id} email={self.email}>'


class Movie(db.Model):
    """Movies."""

    __tablename__ = 'movies'

    movie_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    title = db.Column(db.String)
    overview = db.Column(db.Text)
    release_date = db.Column(db.DateTime)
    poster_path = db.Column(db.String)

    ratings = db.relationship("Rating", back_populates="movie")

    def __repr__(self):
        return f'<Movie movie_id={self.movie_id} title={self.title}>'


class Rating(db.Model):
    """Ratings."""

    __tablename__ = 'ratings'

    rating_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    score = db.Column(db.Integer)
    movie_id = db.Column(db.Integer, db.ForeignKey("movies.movie_id"))
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))

    movie = db.relationship("Movie", back_populates="ratings")
    user = db.relationship("User", back_populates="ratings")

    def __repr__(self):
        return f'<Rating rating_id={self.rating_id} score={self.score}>'


def connect_to_db(flask_app, db_uri="postgresql:///ratings", echo=True):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    # TURNED ECHO OFF BC TERMINAL CONFUSING
    flask_app.config["SQLALCHEMY_ECHO"] = False
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)

    print("Connected to the db!")


if __name__ == "__main__":
    from server import app

    # Call connect_to_db(app, echo=False) if your program output gets
    # too annoying; this will tell SQLAlchemy not to print out every
    # query it executes.

    connect_to_db(app)


# CREATE TABLE: MOVIE RATINGS PART 1
# CREATE A USER CLASS:
# 1 Create Class -> refer to function in line 9
# Check if Class User works in database (psql terminal)
# 2 Create a database called ratings `createdb ratings`
# In case database already exists, you can delete and remake `dropdb ratings` `createdb ratings`
# Run `python3 -i model.py` to go to interactive mode 
# To create tables in the database that are in Python classes:
# 1 `db.create_all()
# CREATE A USER TO ADD TO DATABASE
# 1 `test_user = User(email='test@test.test', password='test')`
# 2 `db.session.add(test_user)` -> add to database
# 3 `db.session.commit()` -> commit to database