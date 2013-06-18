## Useful scripts
- hex-string.py -- Print a hexadecimal string.


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

- free_mem_threshold.sh -- check free mem and execute some troubleshooting action if necessary.


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
