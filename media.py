import webbrowser

# Luke Sheppard
# lshep.usc{(at)}gmail.com
# For Project 1 of the Udacity Full Stack Nanodegree

# This file only defines the class and method.
# Class instances are created in entertainment_center.py, which in turn
# relies on fresh_tomatoes.py to create the html/css/js and open it in
# a browser.
# So don't run this file by itself

class Movie():
    """This class provides a way to store movie related information.
       One method call is available: show_trailer()
    """

    # define the class
    def __init__(self, movie_name, movie_year, movie_storyline, movie_poster_url, movie_trailer_url, movie_length):
        self.title               = movie_name
        self.year                = movie_year
        self.storyline           = movie_storyline
        self.poster_image_url    = movie_poster_url
        self.trailer_youtube_url = movie_trailer_url
        self.length              = movie_length

    # define the method that plays the trailer
    def show_trailer(self):
        """Open the movie trailer in a modal window containing
           an iframe with an html5 video player.
        """
        webbrowser.open(self.trailer_youtube_url)
