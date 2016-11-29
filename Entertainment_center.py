import media
import fresh_tomatoes

# toy story
toy_story=media.Movies("Toy Story","A story of boy and his toys",
                       "https://upload.wikimedia.org/wikipedia/en"
                       "/1/13/Toy_Story.jpg",
                       "https://www.youtube.com/watch?v=KYz2wyBy3kc")
# ratatouille
ratatouille=media.Movies("Ratatouille","American computeranimated comedy film",
                       "https://upload.wikimedia.org/wikipedia/en/5/50/Ratatou"
                       "illePoster.jpg",
                       "https://www.youtube.com/watch?v=c3sBBRxDAqk")
# midnight_in_Paris
midnight_in_Paris=media.Movies("Midnight In Paris","American-French romantic "
                               "comedy film ",
                       "https://upload.wikimedia.org/wikipedia/en/9/9f/Midnig"
                       "ht_in_Paris_Poster.jpg",
                       "https://www.youtube.com/watch?v=BYRWfS2s2v4")

movies=[toy_story,ratatouille,midnight_in_Paris]
fresh_tomatoes.open_movies_page(movies)

# print(toy_story.story_line)
# print(media.Movies.VALID_RATINGS)
# toy_story.show_trailer()
# print(media.Movies.__doc__)
# print(media.Movies.__name__)
# print(media.Movies.__module__)

