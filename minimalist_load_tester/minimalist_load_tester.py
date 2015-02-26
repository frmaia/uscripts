from multiprocessing import Pool, Process, Queue
import urllib2
import sys
import random

class Worker(Process):
	def __init__(self, queue, worker_name):
		super(Worker, self).__init__()
		self.queue = queue
		self.name  = worker_name

	def run(self):
		print 'Worker started'
		print 'Computing!'
		for data in iter( self.queue.get, None ):
			#print "'%s' consuming '%s'" % (self.name, data)
			# Do request
			try:
				code = urllib2.urlopen(data).getcode()
				if not code  < 300:
					print "ERROR: received status_code = '%s'" % code
			except urllib2.URLError, e:
				print "ERROR on connecting to '%s': Reason: %s " % (data, e.reason)


if __name__ == '__main__':

	if len(sys.argv) < 4:
		print "Use: time python2.7 %s <number_of_requests> <number_of_workers> <url1> [url2] [url3] [...] " % sys.argv[0]
		sys.exit("Example: time python %s 100 8 'http://localhost/api/endpoint1' 'http://localhost/api/endpoint2' 'http://localhost/api/status' " % sys.argv[0])

	number_of_requests = int(sys.argv[1])
	number_of_workers = int(sys.argv[2])
	url_referencia = sys.argv[3]
	
	urls = [] 
	for i in sys.argv[3:]:
		urls.append(i)
	
	
	request_queue = Queue()

	for i in range(number_of_workers):
		worker_name = "worker_%s" % i
		Worker( request_queue , worker_name ).start()
		#workers.append(Worker( request_queue , worker_name ).start())

	print "putting data on queue"
	for data in range(1,number_of_requests):
		request_queue.put( random.choice(urls) )
		

	# Sentinel objects to allow clean shutdown: 1 per worker.
	for i in range(number_of_workers):
		request_queue.put( None ) 
		
