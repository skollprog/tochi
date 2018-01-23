from lib.app import *
from lib.io import *
from lib.hue import *
from lib.net import *
from lib.dork import *
endl = "\n"
last = ""

io.clear()
app.about()

while True:

	# User input
	_input = io.stdin(fore.green + app.prompt + " " + fore.white)
	if _input == "": _input = _last
	else: _last = _input
	if _input == "exit": app.close()
	if _input == "clear": io.clear()
	argv = _input.split(" ")
	args = len(argv)

	# GOOGLE DORKING
	if argv[0] == "dork" and args == 2:
		if argv[1] == "help" or argv[1] == "-h":
			dork.help()
		elif argv[1] == "files" or argv[1] == "-f":
			temp = dork.files()
			if temp == ":no-files":
				io.error("No file was not found.")
		else: io.error("Invalid argument given.")
	elif argv[0] == "dork" and args == 3:
		if argv[1] == "read" or argv[1] == "-r":
			temp = dork.read(argv[2])
			if temp == ":invalid-file":
				io.error("File doesn't exist.")
			elif temp == ":no-dorks":
				io.error("File hasn't dorks to show.")
			else:
				while True:
					io.warning(str(len(temp)) + " dorks were found. Do you want to list them all? (yes/no)")
					_input = io.question().lower()
					if _input == "yes" or _input == "y":
						i = 1
						print("")
						io.row(10, [fore.blue + "ID", "DORK"])
						for data in temp:
							io.row(10, [fore.yellow + str(i), fore.white + data])
							io.prevline(1)
							i += 1
						print(endl)
						break
					elif _input == "no" or _input == "n":
						print("")
						break
		elif argv[1] == "custom" or argv[1] == "-c":
			temp = dork.use("custom", int(argv[2]), "*")
			if temp == ":no-file": io.error("File doesn't exists.")
			elif temp == ":no-dork": io.error("No dork was found.")
			elif temp == ":dork-error":
				io.prevline(2)
				io.error("There was an error, try again.")
			else:
				dork.analize(temp)
		else: io.error("Invalid argument given.")
	elif argv[0] == "dork" and args == 5:
		if argv[1] == "use" or argv[1] == "-u":
			temp = dork.use(argv[2], int(argv[3]), argv[4])
			if temp == ":no-file": io.error("File doesn't exists.")
			elif temp == ":no-dork": io.error("No dork was found.")
			elif temp == ":dork-error":
				io.prevline(2)
				io.error("There was an error, try again.")
			else:
				dork.analize(temp)
		else: io.error("Invalid argument given.")

	# NET COMMANDS
	if argv[0] == "net" and args == 2:
		if argv[1] == "help" or argv[1] == "-h":
			net.help()
	if argv[0] == "net" and args == 3:
		if argv[1] == "check" or argv[1] == "-c":
			io.quote("Checking host status...")
			temp = net.check(argv[2])
			io.prevline(2)
			if temp == True:
				io.info("Host is online.")
			elif temp == ":no-http":
				io.error("Invalid url format, HTTP/S or WWW was not declared.")
			else:
				io.error("Host is not responding.")