
### Description

write a script. there are 5 devices, i1, i2, i3,  i4, i5 and each have a unique id 111,222,333,444 and 555. 
If all devices are on, the response looks like (111,222,333,444,555) if one of the device is turned off say i4, 
then that unique id is not populated in the string, so response looks like (111,222,333,555). 

Write a script to print out the device thats turned off. In this case the output of script should say "i4 is turned off”


### Components:

##### monitor.py 
- Description: 
The monitor,py is the script implements the algorithm described above

It works in an active mode, asking the server for the connected devices list, and compare it with the last state to bring the expected informations about the inventary of connected devices.
The monitor basically contains two functions:
- **def active_mode:**
  - Implements the algorithm, actively asking the server for the get_connected_devices

**def get_connected_devices:**
- get_connected_devices
  - The helper function that send the request 'get_connected_clients' to the server.


##### client.py
A helper class that implements a simple and minimalist TCP client that will keep a TCP connection open with the server.

##### server.py 
A helper class that implements a simple and minimalist TCP server which allows its connected clients to send some simple commands, keeping track from its client connections.

Compatible commands that can be received by this server:
- connect <client_id> <client_name>
- disconnect <client_id> <client_name>
- get_connected_clients



### Test the script

1. Start the Server:
```bash
# Use: python server.py <port>
# Example:
python server.py 9999
```

2. Start the Monitor script, and keep the eyes on it:
```bash
# Use: python monitor.py <server_host>:<port>
# Example:

python monitor.py localhost:9999
```

3. Start and stop so many Clients you want, and check the simple algorithm behavior throught the Monitor script.
```bash
# Use: python client.py <server_host>:<port> <client_unique_id> <client_name>
# Example:

python client.py localhost:9999 333 i3
```

**Press ctrl+C to stop the components.**
