#!/usr/bin/python2.7
import traceroute
import unittest

class TestTraceroute(unittest.TestCase):
    def test_find_slowest_hop(self):

        hops_dict = {1: {'ip': '192.168.0.1', 'hop': 1, 'latency': 0.0009160041809082031},
                     2: {'ip': '10.48.128.1', 'hop': 2, 'latency': 0.010013103485107422},
                     3: {'ip': '201.17.128.254', 'hop': 3, 'latency': 0.010753870010375977},
                     4: {'ip': '201.17.128.253', 'hop': 4, 'latency': 0.02326202392578125},
                     5: {'ip': '201.39.21.5', 'hop': 5, 'latency': 0.010139942169189453},
                     6: {'ip': '200.244.213.205', 'hop': 6, 'latency': 0.015893936157226562},
                     7: {'ip': '200.230.251.222', 'hop': 7, 'latency': 0.13425302505493164},
                     8: {'ip': '129.250.202.185', 'hop': 8, 'latency': 0.14442086219787598},
                     9: {'ip': '129.250.6.208', 'hop': 9, 'latency': 0.1418318748474121},
                     10: {'ip': '129.250.2.166', 'hop': 10, 'latency': 0.1575021743774414},
                     11: {'ip': '129.250.2.190', 'hop': 11, 'latency': 0.17141485214233398},
                     12: {'ip': '157.238.64.42', 'hop': 12, 'latency': 0.16363096237182617},
                     14: {'ip': '173.203.0.131', 'hop': 14, 'latency': 0.1461181640625},
                     15: {'ip': '184.106.126.129', 'hop': 15, 'latency': 0.156052827835083},
                     16: {'ip': '23.253.15.53', 'hop': 16, 'latency': 0.15351510047912598}}


        result = traceroute.find_slowest_hop(hops_dict)

        self.assertEqual(result, hops_dict[11])

        self.assertNotEquals(result, hops_dict[10])
        self.assertNotEquals(result, hops_dict[12])


    def test_find_slowest_hop_with_same_values(self):
        # hops_dict --> Note that items '2' and '4' are equivalents in terms of latency.
        hops_dict = {1: {'ip': '192.168.0.1', 'hop': 1, 'latency': 0.0009160041809082031},
                     2: {'ip': '10.48.128.1', 'hop': 2, 'latency': 0.02326202392578125},
                     3: {'ip': '201.17.128.254', 'hop': 3, 'latency': 0.010753870010375977},
                     4: {'ip': '201.17.128.253', 'hop': 4, 'latency': 0.02326202392578125}}

        result = traceroute.find_slowest_hop(hops_dict)
        self.assertEqual(result, hops_dict[2])

    def test_find_slowest_hop_with_empty_dict(self):
        hops_dict = {}
        result = traceroute.find_slowest_hop(hops_dict)
        self.assertIsNone(result)

    def test_traceroute_with_invalid_address(self):
        self.assertRaises(SystemExit, traceroute.traceroute, 'sajhdkjsaodsfhk.com')
        self.assertRaisesRegexp(SystemExit, 'Name or service not known', traceroute.traceroute, 'sajhdkjsaodsfhk.com')

    def test_traceroute_with_None_address(self):
        self.assertRaises(SystemExit, traceroute.traceroute, None)

    def test_traceroute_with_max_hops_args(self):
        result = traceroute.traceroute('google.com', max_hops=2)
        self.assertEqual(len(result), 2)

        result = traceroute.traceroute('google.com', max_hops=3)
        self.assertEqual(len(result), 3)



if __name__ == '__main__':
    unittest.main()
