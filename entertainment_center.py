# -*- coding: utf-8 -*-
# The utf-8 coding line above supresses errors related to characters in some of the URLs below.

# Luke Sheppard
# lshep.usc{(at)}gmail.com
# For Project 1 of the Udacity Full Stack Nanodegree

# To create a webpage of these movies, run this file. It calls fresh_tomatoes.py.
# Don't run fresh_tomatoes.py all by itself. Your web page won't have these movies.
#
# This file creates class instances of several John le Carre movies,
# puts them in a list, then calls the open_movies() function from the
# fresh_tomatoes.py file which builds an html page and opens it in a browser.
#
# The class is defined in media.py.

import fresh_tomatoes
import media

a_most_wanted_man = media.Movie("A Most Wanted Man",
                                "2014",
                                "A young Chechen Muslim illegally immigrates to Hamburg, where he gets caught up in the international war on terror.",
                                "http://upload.wikimedia.org/wikipedia/en/3/3e/A_Most_Wanted_Man_Poster.jpg",
                                "https://youtu.be/7eAdbmUAxq4",
                                "119")

tinker_tailor_soldier_spy = media.Movie("Tinker Tailor Soldier Spy",
                                        "2011",
                                        "Story is set in the aftermath of the Cold War and involves a spy hunt within the highest echelons of the British Secret Intelligence Service.",
                                        "http://ia.media-imdb.com/images/M/MV5BMTU2OTkwNzMyM15BMl5BanBnXkFtZTcwOTI4ODg2Ng@@._V1_SX640_SY720_.jpg",
                                        "https://www.youtube.com/watch?v=QZL8m7E3lQ0",
                                        "127")

the_constant_gardener = media.Movie("The Constant Gardener",
                                    "2005",
                                    "Story of a British diplomat who is in Kenya investigating the brutal murder of his wife, a human rights advocate who, apparently, had secrets.",
                                    "http://upload.wikimedia.org/wikipedia/en/5/54/Constant_gardener.jpg",
                                    "https://www.youtube.com/watch?v=UYXYzzng3Fo",
                                    "129")

the_tailor_of_panama = media.Movie("The Tailor of Panama",
                                   "2001",
                                   "A British spy in Panama meets a local tailor and his wife who concoct a fantastic fictional tale about an impending coup d'état.",
                                   "http://upload.wikimedia.org/wikipedia/en/b/b0/The_Tailor_of_Panama.jpg",
                                   "https://www.youtube.com/watch?v=i_WA2PHPs_Y",
                                   "109")

a_murder_of_quality = media.Movie("A Murder of Quality",
                                  "1991",
                                  "Smiley investigates the murder of a former colleague’s wife at a boys' school where things are not as they at first appear.",
                                  "http://ia.media-imdb.com/images/M/MV5BMjExMDc0MTQxNF5BMl5BanBnXkFtZTcwMjU1MzcyMQ@@._V1_SX640_SY720_.jpg",
                                  "https://www.youtube.com/watch?v=JQFjh5QuFbE",
                                  "103")

the_russia_house = media.Movie("The Russia House",
                               "1990",
                               "The British secret service enlists a scruffy British publisher in Russia to investigate the origin of three notebooks of leaked British secrets.",
                               "http://upload.wikimedia.org/wikipedia/en/1/16/Russia_house_poster.jpg",
                               "https://www.youtube.com/watch?v=jjc45BEvnHY",
                               "122")

the_little_drummer_girl = media.Movie("The Little Drummer Girl",
                                      "1984",
                                      "Israeli intelligence recruits an American actress to infiltrate a Palestinian terrorist network, but her role is more complicated than she realizes.",
                                      "http://upload.wikimedia.org/wikipedia/en/b/b5/Poster_of_the_movie_The_Little_Drummer_Girl.jpg",
                                      "https://www.youtube.com/watch?v=Qcr-eJHMpio",
                                      "132")

smileys_people = media.Movie("Smiley's People",
                             "1982",
                             "Called out of retirement to settle the affairs of a deceased friend, Smiley finds that the Circus doesn't want to know what happened.",
                             "http://upload.wikimedia.org/wikipedia/en/b/b8/Smileys.jpg",
                             "https://www.youtube.com/watch?v=TCuqgKJDHFE",
                             "360")

the_looking_glass_war = media.Movie("The Looking Glass War",
                                    "1969",
                                    "With a blurry photograph as the only clue to go on, British Intelligence recruits a desperate Polish defector to look for missiles in East Germany.",
                                    "http://upload.wikimedia.org/wikipedia/en/4/4f/Looking_glass_war_movie_poster.jpg",
                                    "https://www.youtube.com/watch?v=D4EwlrpoRxM",
                                    "108")

the_deadly_affair = media.Movie("The Deadly Affair",
                                "1966",
                                "A British security officer tries to find the truth behind the suspicious death of a friend from the Foreign Office but he is pressured to call it a suicide.",
                                "http://upload.wikimedia.org/wikipedia/en/7/7c/Thedeadlyaffairmp.jpg",
                                "https://www.youtube.com/watch?v=4eCUkup14NM",
                                "107")

the_spy_who_came_in_from_the_cold = media.Movie("The Spy Who Came in from the Cold",
                                                "1965",
                                                "A British spy is sent to East Germany to initiate a false defection in order to sow disinformation, but his superiors may not have told him the whole story.",
                                                "http://upload.wikimedia.org/wikipedia/en/5/52/Spy_cold.jpg",
                                                "https://www.youtube.com/watch?v=_khnbwEwNv4",
                                                "112")

# Create the movies list that fresh_tomatoes.py needs
movies = [a_most_wanted_man, tinker_tailor_soldier_spy, the_constant_gardener, the_tailor_of_panama, a_murder_of_quality, the_russia_house, the_little_drummer_girl, smileys_people, the_looking_glass_war, the_deadly_affair, the_spy_who_came_in_from_the_cold]

# Send the movies list as an argument to open_movies() in fresh_tomatoes.py
fresh_tomatoes.open_movies_page(movies)
