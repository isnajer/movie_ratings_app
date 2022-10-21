"""Server for movie ratings app."""

from flask import (Flask, render_template, request, flash, session,
                   redirect)
from model import connect_to_db, db
import crud
from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined


# Replace this with routes and view functions!
@app.route('/')
def homepage():
    """View homepage"""

    return render_template('homepage.html')


@app.route('/movies')
def all_movies():
    """View all movies."""
    
    # comes from crud.py function called get_movies
    movies = crud.get_movies()

    return render_template('all_movies.html', movies = movies)


@app.route("/movies/<movie_id>")
def show_movie(movie_id):
    """Show details on a particular movie."""

    movie = crud.get_movie_by_id(movie_id)

    return render_template("movie_details.html", movie=movie)


@app.route('/users')
def all_users():
    """"View all users."""

    # comes from crud.py functon called get_users
    users = crud.get_users()
    
    return render_template('all_users.html', users=users)


@app.route("/users/<user_id>")
def show_user(user_id):
    """Show details on a particular user."""
    print(f"User ID is {user_id}") 
    # Test Printing User ID
    user = crud.get_user_by_id(user_id)

    return render_template("user_details.html", user=user)

@app.route("/users", methods=["POST"])
def register_user():
    """Create a new user"""

    email = request.form.get("email")
    password = request.form.get("password")

    user = crud.get_user_by_email(email)
    if user: #if user exists 
        flash("Cannot create an account with that email. Try again.")
    else:
        user = crud.create_user(email, password)
        db.session.add(user)
        db.session.commit()
        flash("Account created! Please log in.")
    
    return redirect("/")


@app.route("/login", methods=["POST"])
def user_login():
    """Logs user in"""

    email = request.form.get("email") #from HTML
    password = request.form.get("password")

    user = crud.get_user_by_email(email) #<- invoking function from crud.py
    if not user or user.password != password:
        flash("Email does not exist / Password is wrong")
    else:
        session['user_email'] = user.email #getting email from object / but has same value as email line 83 (matching)
# ^ dictionary of user_email: email (as value)
        flash("Logged in succesfully!")

#if user does not exist then flash message error
#else user exists check if password is correct
    return redirect("/")

@app.route("/update_rating", methods=["POST"])
def update_rating():
    rating_id = request.json["rating_id"]
    updated_score = request.json["updated_score"]
    crud.update_rating(rating_id, updated_score)
    db.session.commit()

    return "Success"


@app.route("/movies/<movie_id>/ratings", methods=["POST"])
def create_rating(movie_id):
    """Create a new rating for the movie."""

    logged_in_email = session.get("user_email")
    rating_score = request.form.get("rating")

    if logged_in_email is None:
        flash("You must log in to rate a movie.")
    elif not rating_score:
        flash("Error: you didn't select a score for your rating.")
    else:
        user = crud.get_user_by_email(logged_in_email)
        movie = crud.get_movie_by_id(movie_id)

        rating = crud.create_rating(user, movie, int(rating_score))
        db.session.add(rating)
        db.session.commit()

        flash(f"You rated this movie {rating_score} out of 5.")

    # return redirect(f"/movies/{movie_id}")
    return redirect("/movies")
    
    






if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)

# ASK FOR AN EXPLANATION FROM YOUR TASK DOWN. WHAT HAPPENS, THE CONNECTIONS, ETC.