## Useful scripts

- **minimalist_web_server** -- a really minimalist Web Server
- **cloudfront/aws-cf-sign-url.py** -- a simple python script to sign AWS CloudFront URL's 
- **free_mem_threshold.sh** -- check free mem and execute some troubleshooting action if necessary.
- **hex-string.py** -- A 'stupid' script to print a hexadecimal string.


### Help

##### minimalist_web_server -- a really minimalist Web Server
```
Usage: python2.7 minimalist_web_server.py <PORT>

$ python minimalist_web_server.py 9998
Listening on port 9998 
Ok! I received your post! Data: 'Bla'
127.0.0.1 - - [16/Jul/2014 13:45:38] "POST / HTTP/1.1" 200 -
Ok! I received your post! Data: 'Bla'
127.0.0.1 - - [16/Jul/2014 13:46:03] "POST / HTTP/1.1" 200 -
127.0.0.1 - - [16/Jul/2014 13:46:19] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [16/Jul/2014 13:46:25] "GET /test.txt HTTP/1.1" 200 -

```


##### hex-string.py -- Print a hexadecimal string.


```
Usage: hex-string.py [options]

Print a hexadecimal string.

Options:
  -h, --help            show this help message and exit
  -s STR_SIZE, --size=STR_SIZE
                        string size ( Default: 32 )
                        
Examples:
  $ ./hex-string.py 
  ac0ffbb310e5753acb4bf8dfbd1aad3e
  
  $ ./hex-string.py -s 4
  d92e
```

##### free_mem_threshold.sh -- check free mem and execute some troubleshooting action if necessary.


```
usage: './free_mem_threshold.sh <threshold_percent> [ admin_mail_addr ]'
--------------------------------------------------------
  <threshold_percent> - Threshold percent for free mem
  [ admin_mail_addr ] - sys admin mail address that will receive a feedback when some 
                        throubleshooting action be done. ( 'mutt' must be installed )

Example of usage:
$ sudo ./free_mem_threshold.sh 30 frmaia.br@gmail.com

Critical free mem = 22%! Threshold is 30%. Running troubleshooting_actions.
******************************

#Restarting supervisord ...

Stopping supervisor: supervisord.
Starting supervisor: supervisord.
Checking 'foo' service port
Connection to localhost 3001 port [tcp/*] succeeded!
******************************
Now, free mem = 37%!!!

```
