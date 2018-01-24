from lib.app import *
from lib.io import *
from lib.hue import *
from lib.host import *
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

	# Host command
	if argv[0] == "host" and args == 2:
		if argv[1] == "help" or argv[1] == "-h":
			host.help()
	elif argv[0] == "host" and args == 3:
		if argv[1] == "address" or argv[1] == "-a":
			host.address(argv[2])
		elif argv[1] == "status" or argv[1] == "-s":
			host.status(argv[2])

	# Google dorking
	if argv[0] == "dork" and args == 2:
		if argv[1] == "help" or argv[1] == "-h":
			dork.help()
		if argv[1] == "list" or argv[1] == "-l":
			dork.list()
	elif argv[0] == "dork" and args == 3:
		if argv[1] == "read" or argv[1] == "-r":
			dork.read(argv[2])
	elif argv[0] == "dork" and args == 4:
		if argv[1] == "use" or argv[1] == "-u":
			if argv[3] == "*":
				dork.all(argv[2])
			else:
				dork.use(argv[2], int(argv[3]))
