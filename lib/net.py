from requests import post, get

class net:

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