from lib.io import *
from lib.file import *
from lib.hue import *
from requests import post, get
from html.parser import HTMLParser
from html.entities import name2codepoint
endl = "\n"

'''
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start tag:", tag)
        for attr in attrs:
            print("     attr:", attr)

    def handle_endtag(self, tag):
        print("End tag  :", tag)

    def handle_data(self, data):
        print("Data     :", data)
        if data[0:7] == "http://" or data[0:8] == "https://":
        	print(data)

    def handle_comment(self, data):
        print("Comment  :", data)

    def handle_entityref(self, name):
        c = chr(name2codepoint[name])
        print("Named ent:", c)

    def handle_charref(self, name):
        if name.startswith('x'):
            c = chr(int(name[1:], 16))
        else:
            c = chr(int(name))
        print("Num ent  :", c)

    def handle_decl(self, data):
        print("Decl     :", data)
'''

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        for attr in attrs:
            dork._buffr.append(attr)
    def handle_data(self, data):
        dork._buffr.append(data)
        
class dork:
	_buffr = []
	google = "http://google.com/search"
	page = 0

	def help():
		io.nextline(1)
		io.row(30, ["dork -h", "List help information for this command."])
		io.row(30, ["dork -f", "List all available dork files."])
		io.row(30, ["dork -r [FILE]", "List all dorks within a file."])
		io.row(30, ["dork -u [FILE] [ID] [PAGE]", "Use dork within a file starting from given page."])
		io.row(30, ["dork -u [FILE] [ID] *", "Use dork within a file starting from last page."])
		io.row(30, ["dork -c [ID]", "Use a customized dork."])
		io.nextline(1)
		print("You can replace the short flags with the following words.")
		io.nextline(1)
		io.row(5, ["-h", "help"])
		io.row(5, ["-f", "files"])
		io.row(5, ["-r", "read"])
		io.row(5, ["-u", "use"])
		io.row(5, ["-c", "custom"])
		io.nextline(1)
		print("There's an empty file within dorks folder where you can add your own dorks." + endl)

	def files():
		temp = file.list("dorks")
		if temp == None:
			return ":no-files"
		else:
			if len(temp) == 1: msg = " file was found."
			else: msg = " files were found."
			io.info(str(len(temp)) + msg)
			for f in temp:
				print(f[0:-4])
			print("")

	def read(f):
		temp = file.readfile("dorks/" + f + ".txt")
		if temp == False:
			return ":invalid-file"
		else:
			if len(temp) == 0: return ":no-dorks"
			else: return temp

	def use(f, n, p="*"):
		temp = file.readfile("dorks/" + f + ".txt")
		if temp == False:
			return ":no-file"
		else:
			i = 1
			for _dork in temp:
				_dork = _dork.replace("\n", "")
				if i == n:
					try:
						if p != "*":
							dork.page = (int(p)-1)*10
						io.quote("Dork: " + _dork)
						io.prevline(2)
						io.quote("Page: " + str(int((dork.page/10)+1)))
						temp = get(dork.google, data={"q":_dork, "start":str(dork.page)}, headers={"User-Agent":"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:57.0) Gecko/20100101 Firefox/57.0"}).text
						dork.page += 10
						return temp
					except: return ":dork-error"
				else: i += 1
			return ":no-dork"

	def analize(results):
		parser = MyHTMLParser()
		parser.feed(results)
		warn = "Your client has issued a malformed or illegal request."
		err = 0
		for warn in dork._buffr: err = 1
		if err == 0:
			for temp in dork._buffr:
				print(temp)
		else:
			io.prevline(2)
			io.error("Google is detecting this dork.")