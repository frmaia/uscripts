#!/usr/bin/python2.7

import json
import socket
import sys
import time

from thread import *

BUFFER_SIZE = 1024

class Server:
	"""
	A simple tcp server which receives string commands and keeps a simple track from its client connections.

	Compatible string commands that can be received by this server:
	  - connect <client_id> <client_name>
	  - disconnect <client_id> <client_name>
	  - get_connected_clients

	"""

	def __init__(self, tcp_port=9999, max_queued_connections=5):
		self.tcp_port = tcp_port
		self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

		self.socket.bind(('', tcp_port))
		self.socket.listen(max_queued_connections)

		#Just keep track from connections to close them 
		self.connected_clients = {}

	def start(self):
		print "Server started, listening on port '%s'" % self.tcp_port

		while True:		
			conn, addr = self.socket.accept()
			start_new_thread(self.__process_command, (conn,))

	def stop(self):
		self.socket.shutdown(socket.SHUT_RDWR) 
		self.socket.close()
		print "\nServer stopped!"

	def __process_command(self, conn):
		while True:
			data = conn.recv(BUFFER_SIZE)
			if not data:
				break

			print "DEBUG: Received data: %s" % data
			
			if data == 'get_connected_clients':
				conn.send(json.dumps(self.connected_clients, sort_keys=True))
				return


			command, client_id, client_name = data.split()
			
			if command == 'connect' and client_id not in self.connected_clients:
				self.connected_clients[client_id] = client_name
				conn.send("%s is turned on!" % client_name)

			elif command == 'disconnect' and client_id in self.connected_clients:
				del self.connected_clients[client_id]
				conn.send("%s is turned off!" % client_name)

			print "Current connected clients = %s" % self.connected_clients.keys()


if __name__ == "__main__":
	server_port = int(sys.argv[1])
	
	try:
		server = Server(server_port)
		start_new_thread(server.start())
	except KeyboardInterrupt:
		server.stop()
