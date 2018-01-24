from lib.io import *
from requests import get
from json import loads
import socket
endl = "\n"

class host:

	def help():
		print("")
		io.row(20, ["host -h", "Attributes list for this command."])
		io.row(20, ["host -a [URL]", "Get IP address from a given url."])
		io.row(20, ["host -a self", "Get public IP address from current device."])
		io.row(20, ["host -s [HOST]", "Check if a host is online or not."])
		print("")

	def gethost(url):
		url = url.replace("https://", "")
		url = url.replace("http://", "")
		url = url.replace("www.", "")
		url = url.split("/")[0]
		return url

	def address(url):
		try:
			if url != "self":
				io.quote("Getting host IP address...")
				io.prevline(2)
				url = host.gethost(url)
				io.info(socket.gethostbyname(url))
			else:
				io.quote("Getting public IP address...")
				io.prevline(2)
				url = get("http://freegeoip.net/json").text
				url = loads(url)
				io.info(url["ip"])
		except:
			io.error("Unable to detect IP address.")

	def status(url):
		io.quote("Checking host status...")
		io.prevline(2)
		try:
			url = host.gethost(url)
			url = socket.gethostbyname(url)
			io.info("Host is online.")
		except:
			io.error("Host is not responding.")
