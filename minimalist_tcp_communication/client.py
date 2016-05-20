#!/usr/bin/python2.7

import socket
import sys
import time

BUFFER_SIZE = 1024

class Client:
	"""
	A simple tcp client that keeps a connection open with the server, sending it's client_id and client_name information
	"""
	def __init__(self, server_port,  client_id, client_name):

		self.id = client_id
		self.name = client_name

		self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

		self.socket.connect(('localhost', server_port))
		self.socket.send('connect %s %s' % (self.id, self.name))
		data = self.socket.recv(BUFFER_SIZE)
		print "Received data: ", data

		try:
			# This "stupid" loop will keep the client connected to the server.
			while True:
				time.sleep(60)
				pass
		except KeyboardInterrupt:
			self.disconnect()

	def disconnect(self):
		self.socket.send('disconnect %s %s' % (self.id, self.name))
		self.socket.close()
		print "\n Client disconnected"


if __name__ == "__main__":
	server_address, server_port = sys.argv[1].split(':')
	server_address = str(server_address) 
	server_port = int(server_port) 

	client_id = str(sys.argv[2])
	client_name = str(sys.argv[3])
	client = Client(server_port, client_id, client_name)

