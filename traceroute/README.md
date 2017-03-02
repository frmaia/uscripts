
## Description

- [traceroute.py](./traceroute.py) is a simple python implementation of the `traceroute` command. As a bonus, this script will print the slowest 'stopping point' in the route to your destination;
- [traceroute_test.py](./traceroute_test.py) contains unittest implementations to test the [traceroute](./traceroute.py) functions.

### How to run it:
```bash
$ sudo python traceroute.py --help
usage: traceroute.py [-h] [-m MAX_HOPS] [-n] net_address

Check for the slowest hop in a network route.

positional arguments:
  net_address           Network target/destination address.

optional arguments:
  -h, --help            show this help message and exit
  -m MAX_HOPS, --max_hops MAX_HOPS
                        max number of hops (default=30).
  -n                    print primarily IP addresses numerically.
```

#### Examples of usage:

```
$ sudo python traceroute.py --max_hops 15 www.google.com -n
 1:  192.168.0.1                                           1.140 ms
 2:  10.48.128.1                                           8.775 ms
 3:  201.17.128.254                                       16.693 ms
 4:  201.17.128.252                                        9.882 ms
 5:  200.178.127.33                                       21.839 ms
 6:  200.244.212.147                                      18.590 ms
 7:  200.244.212.126                                      21.463 ms
 8:  200.244.212.26                                       23.815 ms
 9:  200.244.213.176                                      17.601 ms
10:  no reply
11:  no reply
12:  no reply
13:  no reply
14:  no reply
15:  no reply
     Too many hops!
******************************
The slowest hop is: {'ip': '200.244.212.26', 'hop': 8, 'latency': 0.023815155029296875}

$ sudo python traceroute.py www.google.com

 1:  192.168.0.1                                           1.081 ms
 2:  10.48.128.1                                          18.645 ms
 3:  c91180fe.virtua.com.br                               11.017 ms
 4:  c91180fd.virtua.com.br                               11.846 ms
 5:  embratel-T0-2-0-0-tacc01.bhe.embratel.net.br         10.890 ms
 6:  ebt-H0-10-0-0-tcore01.bhe.embratel.net.br            18.997 ms
 7:  ebt-B10831-tcore01.spoph.embratel.net.br             18.834 ms
 8:  ebt-B1081-tcore01.spomb.embratel.net.br              18.600 ms
 9:  ebt-B11711-puacc01.spolp.embratel.net.br             18.980 ms
10:  no reply
11:  no reply
12:  no reply
13:  no reply
14:  no reply
15:  no reply
16:  no reply
17:  no reply
18:  no reply
19:  no reply
20:  no reply
21:  no reply
22:  no reply
23:  no reply
24:  no reply
25:  no reply
26:  no reply
27:  no reply
28:  no reply
29:  no reply
30:  no reply
     Too many hops!
******************************
The slowest hop is: {'ip': 'ebt-H0-10-0-0-tcore01.bhe.embratel.net.br', 'hop': 6, 'latency': 0.0189969539642334}

```

### Run Unit tests
Just execute:
```bash
$ sudo python traceroute_test.py
......
----------------------------------------------------------------------
Ran 6 tests in 0.279s

OK
```
