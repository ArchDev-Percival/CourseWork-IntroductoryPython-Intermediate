class Parent():
	def __init__(self,last_name,eye_colour):
		print("Parent Constructor Called")
		self.last_name = last_name
		self.eye_colour = eye_colour
	def print_information(self):
		print("My last name is: "+self.last_name+" and my eyes are "+self.eye_colour+" in colour.")

class Child(Parent):
	def __init__(self,last_name,eye_colour,number_of_toys):
		print("Child Constructor Called")		
		Parent.__init__(self,last_name,eye_colour)
		self.number_of_toys = number_of_toys

	def print_information(self):
		Parent.print_information(self)
		print("Hey, ain't nobody got time for that! I have got "+str(self.number_of_toys)+" toys to play with!")

miley_cyrus = Child("Cyrus","Blue",5)
miley_cyrus.print_information()
