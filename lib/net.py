from lib.io import *
from requests import post, get

class net:

	def help():
		io.nextline(1)
		io.row(20, ["dork -h", "List help information for this command."])
		io.row(20, ["net -c [URL]", "Check if the given URL is responding or not."])
		io.nextline(1)
		print("You can replace the short flags with the following words.")
		io.nextline(1)
		io.row(5, ["-h", "help"])
		io.row(5, ["-c", "check"])
		print("")

	def urlfix(url):
		temp = [url.split(".")[0], url.split("://")[0]]
		if temp[0] == "www":
			return "http://" + url.replace("www.", "")
		elif temp[1] == "http" or temp[1] == "https":
			return url.replace("www.", "")
		else:
			return ":no-http"

	def check(url):
		try:
			url = net.urlfix(url)
			if url != ":no-http":
				get(url)
				return True
			return ":no-http"
		except: return False