from sys import stdout
from lib.hue import *
endl = "\n"

class io:

	def stdin(prompt=""):
		return input(prompt)

	def clear():
		stdout.write("\x1b[2J\x1b[0H")

	def prevline(n):
		stdout.write("\x1b[" + str(n) + "A")

	def nextline(n):
		stdout.write("\x1b[" + str(n) + "B\x1b[1000D")

	def row(size=20, cols=[]):
		if len(cols) > 0:
			i = 0
			for col in cols:
				stdout.write("\x1b[1000D")
				if i > 0:
					stdout.write("\x1b[" + str(i) + "C")
				stdout.write(col)
				i += size
			stdout.write(endl)

	def question():
		io.prevline(1)
		return input(fore.white + "[?] ")

	def quote(msg, mode=0):
		print(endl + fore.black + "[!] " + msg + fore.reset + endl)

	def info(msg):
		print(endl + fore.blue + "[!] " + msg + fore.reset + endl)

	def success(msg):
		print(endl + fore.green + "[!] " + msg + fore.reset + endl)

	def warning(msg):
		print(endl + fore.yellow + "[!] " + msg + fore.reset + endl)

	def error(msg):
		print(endl + fore.red + "[x] " + msg + fore.reset + endl)
