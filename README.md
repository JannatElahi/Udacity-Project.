# Udacity-Project.
README FILE

Fresh tomatoes is a website that shows movie trailers for children. It is a great way to look at movie trailers from youtube. There is a combination of few movies for children along with movie title, poster image and some description of the movie(story line) and the actual youtube trailer. 

There are in total of three files included to make this website. 
          1) media.py
          2)test_entertainment.py
          3)test_freshtomatoes.py

Lets start off with the first file that is media.py

media.py combines a list of movies with some of the data related to the movie. This file "media.py" calls a class Movie. The class "Movie" stores all the data in a constructor. The type of data stored in this contrcutor is movie title, poster image, story line and youtube trailer. 

This class Movie calls a method that is show trailer which will actually open the movie trailer through webbrowser.

The second file is test_entertainment.py. 

This file imports media.py to store information in the contructor called in media.py.
Then, all the information related to each movie is stored seperately in a list.

Then comes the test_freshtomatoes.py

This file is written in html.There are couple of tags used such as head, body,paragraph.
Head tag was used to make the title and the body tag was used for making paragraphs. Attaching links and it does all the formatting of the website. 
This is also responsible for the body of the website as to what content 
will be on the websites. Tags are assigned on this file such as H1, H2. There is a method open movies page which is actually going to open up the website in the webbrowser.

In order to make the website work, run the test_entertainment file and this will open up the website in your webbrowser.You will be able to watch trailers of movies easily.
