import media
import test_freshtomatoes

"""Note: I have designed a couple of instances of the class Movie"""
"""namely Cindrella, Frozen, Charlie, Teletubbies and Pinocchio"""
"""As we run the code below, the init funtion gets called"""
"""Self is the instance being created that is Cindrella"""
Cindrella = media.Movie("Cindrella", "In a far away, long ago kingdom,"
                        " Cinderella is living happily with her parents"
                        "until her mother dies.Keen to support her father,"
                        "Ella welcomes her stepmother and her daughters."
                        "into the family home",
                        "http://www.impawards.com/2015/posters/"
                        "cinderella_ver2.jpg",
                        "http://www.impawards.com/2015/posters/"
                        "cinderella_ver2.jpg")
Frozen = media.Movie("Frozen",
                     "Fearless Anna sets off on a journey with rugged mountain"
                     "man Kristoff and his loyal reindeer Sven-to find her"
                     "sister Elsa, whose icy powers have trapped the"
                     "Kingdom of Arendelle in eternal winter",
                     "http://www.tammileetips.com/wp-content/uploads/2013/09/"
                     "Disney-Frozen-Movie-Poster.png",
                     "https://www.youtube.com/watch?v=TbQm5doF_Uc")
Charlie = media.Movie("Charlie and the Chocolate Factory",
                      "When Willy Wonka decides to let five children"
                      "into his chocolate factory, he decides to release"
                      "five golden tickets in five seperate chocolate"
                      "bars, causing complete mayhem..",
                      "http://image.tmdb.org/t/p//original/"
                      "oGPsPAYwmj41tbvbdJhGZkvsGqZ.jpg",
                      "https://www.youtube.com/watch?v=OFVGCUIXJls")
Teletubbies = media.Movie("Teletubbies",
                          " This tv show is for babies, the four"
                          "colourful Teletubbies play in idyllic"
                          "Teletubbyland.They repear fun activities"
                          "such as rolling on the ground,laughing,"
                          "running and rolling on their bellies.",
                          "http://mvpo.us/img/P4955",
                          "https://www.youtube.com/watch?v=YdtED4bmR0k")
Pinocchio = media.Movie("Pinocchio",
                        "an old wood-carver Geppetto carves a wooden"
                        "puppet named Pinocchio. The puppet is"
                        "brought to life by a fairy,who says that"
                        "he can become a real boy if he proves to"
                        "be brave,truthful,and unselfish.",
                        "https://fanart.tv/api/download.php?type="
                        "download&image=137560&section=3",
                        "https://www.youtube.com/watch?v=pEDCcOXkc4o")
Kung = media.Movie("Kung Fu Panda",
                   "Enthusiastic, big and a little clumsy, Po is"
                   "the biggest fan of kung fu around--which"
                   "doesn't exactly come in handy while working"
                   "every day in his family's noodle shop.",
                   "https://www.cinematerial.com/media/posters/"
                   "md/hx/hxqubpsv.jpg?v=1456270602",
                   "https://www.youtube.com/watch?v=PXi3Mv6KMzY")
media_list = [Cindrella, Frozen, Charlie, Teletubbies, Pinocchio, Kung]

test_freshtomatoes.open_movies_page(media_list)


