#!/usr/bin/python

import argparse
import socket
#import ipdb
import sys
import time



def traceroute(dest_addr, max_hops=30, resolve_names=False):
    """
        This function is an implementation for the traceroute command, measuring the latency of ICMP replies from the intermediary network appliances/routers.
    """

    if not dest_addr:
        sys.exit("You have to pass a valid Internet address to this function. '%s' is invalid!" % dest_addr)

    port = 55555

    ttl = 1
    hops = {}

    while True:

        # Break condition
        if ttl > max_hops:
            print "     Too many hops!"
            break

        # Sender (based on protocol UDP)
        sock_sender = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        sock_sender.setsockopt(socket.SOL_IP, socket.IP_TTL, ttl)

        # Receiver for ICMP replies
        sock_receiver = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
        sock_receiver.bind(("", port))
        sock_receiver.settimeout(3)

        router_addr = None
        ### Send packages to end address
        try:
            sock_sender.sendto("", (dest_addr, port))
        except socket.error , e:
            sys.exit("Error trying to send UDP packages the address '%s': %s" % (dest_addr, e.strerror))

        ### Receive and measure the latency for the ICMP replies
        try:
            start = time.time()
            received = sock_receiver.recvfrom(548)
            end = time.time()

            router_addr = received[1][0]
        except socket.error, e:
            # In the case of connection 'timeout'...
            print "%2s:  no reply" % ttl
            ttl +=1
            continue
        except KeyboardInterrupt:
            # In the case of user wants to cancel/interrupt the process
            sys.exit()
        finally:
            # Always close connections
            sock_sender.close()
            sock_receiver.close()

        ### Resolve names if requested
        if resolve_names:
            try:
                router_addr = socket.gethostbyaddr(router_addr)[0]
            except socket.error:
                #ignore... using IP address instead resolving
                pass

        # Insert data into the 'hops' dictionary
        hops[ttl] = {'hop': ttl, 'ip': router_addr, 'latency': (end - start)}

        # Print information about the route point latency
        print "%2s:  %-50s %8.3f ms" % (ttl, router_addr, round(((end - start) *1000),3))
        ttl += 1

        # Break if the network target was already achieved
        if router_addr == socket.gethostbyname(dest_addr):
            break

    return hops

def find_slowest_hop(hops_dict):
    """
        Iterate over the dictionary looking for the hop with the slowest latency.
    """
    slowest = hops_dict.get(1)

    for i in hops_dict:
        if hops_dict[i]['latency'] > slowest['latency']:
            slowest = hops_dict[i]

    return slowest


if __name__ == "__main__":
    # Argparse...
    parser = argparse.ArgumentParser(description='Check for the slowest hop in a network route.')
    parser.add_argument('net_address',type=str, help='Network target/destination address.')
    parser.add_argument('-m', '--max_hops', type=int, help='max number of hops  (default=30).', default=30)
    parser.add_argument('-n', dest='resolve_names', action='store_false', help='print primarily IP addresses numerically.')
    parser.set_defaults(resolve_names=True)
    args = parser.parse_args()

    ### Run!
    hops_dict = traceroute(args.net_address, args.max_hops, args.resolve_names)
    print "*" * 30
    print "The slowest hop is: %s" % find_slowest_hop(hops_dict)
