from sys import stdout as io
from lib.hue import *
endl = "\n"

class app:
	name = "Tōchi"
	built = "v1.0"
	author = "SkollProg"
	contact = "dev@skollprog.com"
	copy = "(c) 2018 " + name + " - All rights reserved."
	prompt = "tōchi://"

	def about():
		print(fore.green + app.name + " " + app.built + fore.black)
		print("Author: " + fore.red + app.author + fore.black)
		print("Contact: " + fore.red + app.contact + fore.black)
		print(app.copy + endl)

	def close():
		print()
		exit()