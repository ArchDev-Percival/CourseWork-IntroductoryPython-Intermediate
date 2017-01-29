#!/usr/bin/env python
import media
import fresh_tomatoes

the_kings_speech = media.Movie("The King's Speech","The King is able to overcome his speech impediment","http://www.techgadgettalk.com/wp-content/uploads/2016/05/nkFTbA1XjKWo9LCTaV1hV2Lsgr1.jpg","https://www.youtube.com/watch?v=pzI4D6dyp_o")

kingdom_of_heaven = media.Movie("The Kingdom of Heaven","In the twelfth century, blacksmith Balian travels to Jerusalem, a city seething with religious wars. What follows next is his transformation into a defending warrior who saves the city and its people.","https://tenyearsago.files.wordpress.com/2015/05/kingdom1.jpg","https://www.youtube.com/watch?v=YAr6So7e_08")

#print(kingdom_of_heaven.storyline)
#kingdom_of_heaven.show_trailer()

the_pianst = media.Movie("The Pianist","World War II Story","http://i.dailymail.co.uk/i/pix/2015/11/26/10/2ED2997700000578-0-image-a-24_1448534081450.jpg","https://www.youtube.com/watch?v=u_jE7-6Uv7E")

the_godfather_1 = media.Movie("The Godfather,Part I","The rise and fall of Veto Corleone","https://upload.wikimedia.org/wikipedia/en/a/af/The_Godfather,_The_Game.jpg","https://www.youtube.com/watch?v=YYKxj8qiLTg")

shawshank_redemption = media.Movie("The Shawshank Redemption","Follows the life of an accountant wrongly accused of murder, and how he ultimately devastates his captors escaping through a tunnel behind a poster.","http://img01.deviantart.net/2f2f/i/2015/244/7/7/the_shawshank_redemption___movie_poster_by_zungam80-d97zgxc.jpg","https://www.youtube.com/watch?v=6hB3S9bIaco")

the_league_of_extraordinary_gentlemen = media.Movie("The League of Extraodinary Gentlemen","Fantasy movie, about how the league needs to contain itself as one of its members goes rogue.","http://www.impawards.com/2003/posters/league_of_extraordinary_gentlemen_ver2.jpg","https://www.youtube.com/watch?v=QOR9I54dMAY")

movies = [the_kings_speech,kingdom_of_heaven,the_pianst,the_godfather_1,shawshank_redemption,the_league_of_extraordinary_gentlemen]

#print(media.Movie.VALID_RATINGS)
fresh_tomatoes.open_movies_page(movies)
print(media.Movie.__doc__)
print(media.Movie.__name__)
print(media.Movie.__module__)





