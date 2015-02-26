#!/usr/bin/python2.7

import SimpleHTTPServer
import SocketServer
import sys

class TestHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
	"""The test example handler."""

	def do_GET(self):
		""" Handle a GET request """
		response_message = "Ok! I'm here!\n"
		self.wfile.write(response_message)
		self.send_response(200, response_message)
		self.finish()

	def do_POST(self):
		""" Handle a POST request """

		if not self.headers.getheader('content-length'):
			response_message = "Ok! But no data received!\n"

		else:
			length = int(self.headers.getheader('content-length'))
			data = self.rfile.read(length)
			response_message = "Ok! I received your post! Data: '%s'\n" % data

		print response_message
		self.wfile.write(response_message)
		self.send_response(200,response_message)	
		self.finish()


def start_server(port, server_class=SocketServer.TCPServer, handler_class=TestHandler):
	print "Listening on port %s " % port
	server_address = ('', port)
	httpd = server_class(server_address, handler_class)
	httpd.serve_forever()
	print "Finishing"

if __name__ == "__main__":

	if len(sys.argv) != 2:
		sys.exit("Usage: python2.7 %s <PORT>" % sys.argv[0])

	port = int(sys.argv[1])
	start_server(port)
