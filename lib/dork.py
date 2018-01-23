from lib.io import *
from lib.file import *
from lib.hue import *
from requests import post, get
from xml.dom import minidom
endl = "\n"

class dork:
	google = "https://google.com/search?q="
	page = 0

	def files():
		temp = file.list("dorks")
		if temp == None:
			return ":no-files"
		else:
			if len(temp) == 1: msg = " file was found."
			else: msg = " files were found."
			io.info(str(len(temp)) + msg)
			for f in temp:
				print(f)
			print("")

	def read(f):
		temp = file.readfile("dorks/" + f)
		if temp == False:
			return ":invalid-file"
		else:
			if len(temp) == 0: return ":no-dorks"
			else: return temp

	def use(f, n, p="*"):
		temp = file.readfile("dorks/" + f)
		if temp == False:
			return ":no-file"
		else:
			i = 1
			for d in temp:
				if i == n:
					try:
						if p != "*":
							dork.page = (int(p)-1)*10
						io.quote("Dork: " + d.replace("\n", ""))
						io.prevline(2)
						io.quote("Page: " + str(int((dork.page/10)+1)))
						temp = get(dork.google + d.replace("\n", "") + "&start=" + str(dork.page)).text
						dork.page += 10
						return temp
					except: return ":dork-error"
				else: i += 1
			return ":no-dork"

	def custom(dork):
		try:
			io.prevline(2)
			io.quote("Dork: " + dorking.google + dork.replace("\n", "") + "&start=" + str(dorking.page))
			temp = get(dorking.google + dork.replace("\n", "") + "&start=" + str(dorking.page)).text
			dorking.page += 10
			return temp
		except: return ":dork-error"

	def analize(results):
		print(results)
