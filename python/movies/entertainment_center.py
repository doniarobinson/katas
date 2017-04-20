import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
  "A story of a boy and his toys that come to life",
  "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
  "https://www.youtube.com/watch?v=vwyZH85NQC4")

avatar = media.Movie("Avater",
  "A marine on an alien planet",
  "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
  "https://www.youtube.com/watch?v=-9ceBgWV8io")

oceans11 = media.Movie("Ocean's 11",
  "Ocean's Eleven is a 2001 American comedy heist film and a remake of the 1960 Rat Pack film of the same name.",
  "https://upload.wikimedia.org/wikipedia/en/6/68/Ocean%27s_Eleven_2001_Poster.jpg",
  "https://www.youtube.com/watch?v=u7VTkceSsEw")

#oceans11.show_trailer()

movies = [toy_story, avatar, oceans11]

fresh_tomatoes.open_movies_page(movies)

#print(media.Movie.VALID_RATINGS)

#print(media.Movie.__doc__)