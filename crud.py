"""CRUD operations."""

from model import db, User, Movie, Rating, connect_to_db


def create_user(email, password):
    """Create and return a new user.
    Email= string, Password= string"""
    

    user = User(email=email, password=password)

    return user

def get_users():
    """"Return all users"""

    return User.query.all()


def get_user_by_id(user_id):
    """Returns the user with that ID"""

    return User.query.get(user_id)


def create_movie(title, overview, release_date, poster_path):
    """Create and return a new movie."""

    movie = Movie(
        title=title,
        overview=overview, 
        release_date=release_date,
        poster_path=poster_path,
    )
    return movie


# A function that returns all movies. This will be routed to `/movies`
def get_movies():
    """Return all movies."""

    # Can filter by various columns 
    return Movie.query.all()


def get_movie_by_id(movie_id):

    return Movie.query.get(movie_id)


def create_rating(user, movie, score):
    """Create and return a new rating
    User=user object, Movie=movie object"""

    rating = Rating(
        user=user, movie=movie, score=score
    )

    return rating























if __name__ == '__main__':
    from server import app
    connect_to_db(app)





#CREATE USER FUNCTION ON MOVIE RATINGS: PART2
# STEPS TO ADDING USERS (python3 -i crud.py):
# 1 user = create_user('email', 'password')
# 2 db.session.add(user) -> add user to database
# 3 db.session.commit(blank) -> committing user to database
# CHECK IF USER APPEARS IN DATABSE (psql ratings)(in new terminal)
# 4 SELECT * FROM users; -> returns table with all user id, user email, and user password

# CREATE MOVIE FUNCTION ON MOVIE RATING: PART 2
# STEPS TO ADD MOVIE (python3 -i crud.py):
# 1 CALL FUNCITON AND SET EQUAL TO A MOVE NAME -> `happy = create_movie('Happy Feet', 'The best movie', '2022-09-10', 'url')`
# 2 CHECK IF MOVIE IS CREATED -> `happy`

# CREATE RATING FUNCTION ON MOVIE RATING: PART 2
# STEPS TO ADD MOVIE (python3 -i crud.py):
# 1 CALL FUNCITON AND SET EQUAL TO A RATING NAME -> `rating = create_rating(tony, happy, 9)` <- no strings bc we are using the object tony and happy that we created in the user function and the movie function
# 2 CHECK IF RATING IS CREATED -> `rating`