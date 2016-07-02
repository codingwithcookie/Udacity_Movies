import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4")

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
                     "http://www.youtube.com/watch?v=5PSNL1qE6VY")

inside_man = media.Movie("Inside Man", "More then just a bank robery",
                         "https://upload.wikimedia.org/wikipedia/en/a/a2/Inside_Man_%28film_poster%29.jpg",
                         "https://www.youtube.com/watch?v=44v8NhVEL5A")


movies = [toy_story, avatar, inside_man]
fresh_tomatoes.open_movies_page(movies)
