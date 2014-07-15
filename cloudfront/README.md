
## aws-cf-sign-url.py

#### Help

```
$ python aws-cf-sign-url.py --help
usage: aws-cf-sign-url.py [-h] -k KEY_PAIR_ID -p PRIV_KEY_FILE -e EXPIRES
                          [-d DISTRIBUTION_TYPE]
                          resource-url

Helper for generate and test CloudFront signed URL's.

positional arguments:
  resource-url          Use the FULL URL for download distributions. For
                        streaming distribution, use only

optional arguments:
  -h, --help            show this help message and exit
  -k KEY_PAIR_ID, --key-pair-id KEY_PAIR_ID
                        Key pair Id (from the AWS accounts CloudFront tab)
  -p PRIV_KEY_FILE, --pk PRIV_KEY_FILE
                        Private key pair file
  -e EXPIRES, --expires EXPIRES
                        Expires time (in seconds) to sign the resource URL.
  -d DISTRIBUTION_TYPE, --distribution-type DISTRIBUTION_TYPE
                        CloudFront target distribution type ['download',
                        'streaming']

```

#### Example of usage: 

```
$ python aws-cf-sign-url.py -k APKAI*KEY_ID -p pk-APKAI*KEY_ID.pem -e 60 http://di5mm7sb8rvyb.cloudfront.net/teste-felipe/HD_1080p_Sample_Test.mp4

http://di5mm7sb8rvyb.cloudfront.net/teste-felipe/HD_1080p_Sample_Test.mp4?Expires=1379690295&Key-Pair-Id=APKAI43KQQ34LRUDRYIA&Signature=BHyuvo5u7rTTWITgVuBbOJ6Ao9FSLfO9CZYy2pgKRVzZ65QDT61V0NQ9qIFdi5uObAAijRQcaU7jU9v55WpmlnEcmccvDTnk-oSRUwL6xzd8k2NoibOudTgltMkIKi-Md5uPyo7VSYl~D6OxsnwExSWeSC3uEX25PQyhWvpt1EgFFBIZmoPX5BHmM6nJsR093pM5y5Z6sJoJJMWWkRcXWE0Z-N85U~Z4o1PIEP4BQXYb6bdlshRetJKbmJMZT0AR3mehZ5EdPGQzXqVAe35zbCFGuWvOEExEadJH3WgGb8t6WLPfsCJYSF6MiCf3psNKi49YmqzQKhTMZp6m1va6hA__
```
