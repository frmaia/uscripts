#!/usr/bin/python2.7

import socket
import sys
import time
import json

BUFFER_SIZE = 1024

def get_connected_devices(server_host, server_port):
		monitor_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		monitor_socket.connect((server_host, server_port))

		monitor_socket.send('get_connected_clients')
		data = monitor_socket.recv(BUFFER_SIZE)
		monitor_socket.close()

		return data


def active_mode(server_host,server_port, interval_between_rechecks=5):
	"""
	Actively asks the server for the connected devices list, compare with the last state to bring changes informations to screen.
	"""

	INTERVAL_BETWEEN_RECHECKS = 5

	# Check for the already active
	current_connected = json.loads(get_connected_devices(server_host,server_port), parse_int=None)
	for client_id in current_connected:
		print "%s is already active" % current_connected[client_id]

	print "\n----------\n"

	# Loops checking for eventual changes in the get_connected_devices from server
	try:
		while True:
			updated_list = json.loads(get_connected_devices(server_host,server_port), parse_int=None)
			
			# Compare the response from server, checking for added and removed devices(clients):
			turned_off_items = list(set(current_connected) - set(updated_list))
			turned_on_items = list(set(updated_list) - set(current_connected))

			for client_id in turned_off_items:
				print "%s is turned off" % current_connected[client_id]

			for client_id in turned_on_items:
				print "%s is turned on" % updated_list[client_id]

			if turned_off_items or turned_on_items:
				current_connected = updated_list
				print "Current connected devices: %s" % current_connected.keys()

			time.sleep(interval_between_rechecks)		

	except KeyboardInterrupt:
		sys.exit()

			

if __name__ == "__main__":
	server_host, server_port = sys.argv[1].split(':')
	server_host = str(server_host) 
	server_port = int(server_port) 

	active_mode(server_host,server_port)
