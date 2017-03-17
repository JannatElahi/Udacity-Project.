import webbrowser


class Movie():
    """This class provides a way to store movie related information"""
    """The name init is esentially reserved in python,"""
    """it is a special function or method"""
    """init initializes or creates space in memory to remember"""
    """details"""
    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube_url):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube_url

    def show_trailer(self):
        """This instance method opens up the webbrowser"""
        """with the linked url"""
        webbrowser.open(self.trailer_youtube_url)
