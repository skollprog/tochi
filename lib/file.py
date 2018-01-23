from os import path, listdir, getcwd

class file:

	def readfile(file):
		if path.isfile(file):
			with open(file) as file:
				return file.readlines()
		else: return False

	def list(folder):
		temp = []
		i = 0
		for file in listdir(getcwd() + "/" + folder):
			if file != "." or file != "..":
				temp.append(file)
				i += 1
		if i == 0: return None
		else: return temp