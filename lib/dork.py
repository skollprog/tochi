from lib.io import *
from lib.file import *
from lib.hue import *
endl = "\n"

class dork:

	def help():
		print("")
		io.row(25, ["dork -h", "Attributes list for this command."])
		io.row(25, ["dork -l", "List all available dork files."])
		io.row(25, ["dork -r [FILE]", "List all dorks within a file."])
		io.row(25, ["dork -u [FILE] [ID]", "Use dork within a file."])
		print("")