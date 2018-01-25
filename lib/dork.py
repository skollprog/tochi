from lib.io import *
from lib.file import *
from lib.hue import *
from requests import get
from urllib import parse
from json import loads
import time
endl = "\n"

class dork:

	def help():
		print("")
		io.row(25, ["dork -h", "Attributes list for this command."])
		io.row(25, ["dork -l", "List all available dork files."])
		io.row(25, ["dork -r [FILE]", "List all dorks within a file."])
		io.row(25, ["dork -u [FILE] [ID]", "Use dork within a file."])
		print("")

	def list():
		files = file.list("dorks")
		if len(files) != 0:
			print("")
			for f in files:
				print(f[0:-4])
			print("")
		else:
			io.error("There ain't files to show up.")

	def read(f):
		content = file.readfile("dorks/" + f + ".txt")
		if content != False:
			if len(content) != 0:
				print("")
				io.row(5, [fore.blue + "ID", "DORK"])
				i = 1
				for d in content:
					io.row(5, [fore.yellow + str(i), fore.white + d])
					io.prevline(1)
					i += 1
				print(endl)
			else: io.error("There ain't dorks to show up.")
		else: io.error("File doesn't exist.")

	def search(query):
		_google = "https://www.googleapis.com/customsearch/v1"
		_params = {
			"key": "AIzaSyANm8farYg7FBUl49FRSMDURp4a7VDEyEY",
			"cx": "017576662512468239146:omuauf_lfve",
			"q": query
		}
		_data = get(_google, params=_params).text
		_data = loads(_data)
		try:
			for item in _data["items"]:
				print(item["link"])
			print("")
			return True
		except: return False

	def use(f, n):
		content = file.readfile("dorks/" + f + ".txt")
		if content != False:
			if len(content) != 0:
				i = 1
				for _dork in content:
					if n == i:
						io.quote("Dork: " + fore.magenta + _dork + fore.white)
						io.prevline(1)
						if not dork.search(_dork):
							io.prevline(2)
							io.error("No results gathered.")
						i = -1
						break
					else: i += 1
				if i != -1: io.error("Doesn't exist dork with given ID.")
			else: io.error("This file doesn't contain any dorks to use.")
		else: io.error("File doesn't exist.")

	def all(f):
		content = file.readfile("dorks/" + f + ".txt")
		if content != False:
			if len(content) != 0:
				io.quote("Gathering dorks data...")
				i = 0
				for _dork in content:
					if dork.search(_dork): i += 1
					time.sleep(5)
				if i == 0:
					io.prevline(2)
					io.error("No results gathered.")
			else: io.error("This file doesn't contain any dorks to use.")
		else: io.error("File doesn't exist.")