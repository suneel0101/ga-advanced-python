fav_movies = [
    {
        "name": "Shawshank Redemption",
        "imdb_score": 8.7,
        "fb_fan_count": 900000
    },
    {
        "name": "Never Say Never",
        "imdb_score": 1.2,
        "fb_fan_count": 80000000,
    },
    {
        "name": "Interstellar",
        "imdb_score": 7.7,
        "fb_fan_count": 1200000,
    }
]

def get_best_fb_movie(movies):
    # pick the first one to start
    best_movie = movies[0]
    for movie in movies:
        # if `movie` has a better fb_fan_count
        # make that our best movie so far
        if movie["fb_fan_count"] > best_movie["fb_fan_count"]:
            best_movie = movie
    return best_movie

def get_best_imdb_score(movies):
    best_movie = movies[0]
    for movie in movies:
        if movie["imdb_score"] > best_movie["imdb_score"]:
            best_movie = movie
    return best_movie

print "best imdb score"
print get_best_imdb_score(fav_movies)

print "best fb score"
print get_best_fb_movie(fav_movies)
