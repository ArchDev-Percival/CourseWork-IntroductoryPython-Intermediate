#!/usr/bin/env python
#Google StyleGuide for Python
class Movie():
	#Constructor, always takes self as a parameter
	def __init__(self,movie_title,movie_storyline,poster_image,trailer_youtube):
		self.title = movie_title
		self.storyline = movie_storyline
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube
