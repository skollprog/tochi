from lib.app import *
from lib.io import *
from lib.hue import *
from lib.host import *
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

	if args > 1:

		# Host command
		if argv[0] == "host" and args == 2:
			if argv[1] == "help" or argv[1] == "-h":
				host.help()
		if argv[0] == "host" and args == 3:
			if argv[1] == "address" or argv[1] == "-a":
				host.address(argv[2])
			elif argv[1] == "status" or argv[1] == "-s":
				host.status(argv[2])