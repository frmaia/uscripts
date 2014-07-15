from M2Crypto import EVP
import argparse
import base64
import time
import sys

def aws_url_base64_encode(msg):
    #print "MESSAGE = %s " % msg
    msg_base64 = base64.b64encode(msg)
    #print "MESSAGE_BASE64 = %s " % msg_base64
    msg_base64 = msg_base64.replace('+', '-')
    msg_base64 = msg_base64.replace('=', '_')
    msg_base64 = msg_base64.replace('/', '~')
    return msg_base64

def sign_string(message, priv_key_string):
    key = EVP.load_key_string(priv_key_string)
    key.reset_context(md='sha1')
    key.sign_init()
    key.sign_update(message)
    signature = key.sign_final()
    return signature

def create_url(url, encoded_signature, key_pair_id, expires):
    signed_url = "%(url)s?Expires=%(expires)s&Key-Pair-Id=%(key_pair_id)s&Signature=%(encoded_signature)s" % {
            'url':url,
            'expires':expires,
            'key_pair_id':key_pair_id,
            'encoded_signature':encoded_signature,
            }
    return signed_url

def get_canned_policy_url(url, priv_key_string, key_pair_id, expires):
    #we manually construct this policy string to ensure formatting matches signature
    canned_policy = '{"Statement":[{"Resource":"%(url)s","Condition":{"DateLessThan":{"AWS:EpochTime":%(expires)s}}}]}' % {'url':url, 'expires':expires}

    #sign the non-encoded policy
    signature = sign_string(canned_policy, priv_key_string)
    #now base64 encode the signature (URL safe as well)
    encoded_signature = aws_url_base64_encode(signature)

    #combine these into a full url
    signed_url = create_url(url, encoded_signature, key_pair_id, expires);

    return signed_url

def encode_query_param(resource):
    enc = resource
    enc = enc.replace('?', '%3F')
    enc = enc.replace('=', '%3D')
    enc = enc.replace('&', '%26')
    return enc


def main(args):
    #Set parameters for URL
    parser=argparse.ArgumentParser(description='''Helper for generate and  test CloudFront signed URL's. ''')
    parser.add_argument('-k', '--key-pair-id', required=True, dest='key_pair_id', help='Key pair Id (from the AWS accounts CloudFront tab)')
    parser.add_argument('-p', '--pk', required=True, dest='priv_key_file', help="Private key pair file")
    parser.add_argument('-e', '--expires', required=True, type=int, dest='expires', help="Expires time (in seconds) to sign the resource URL.")
    parser.add_argument('-d', '--distribution-type', required=False, default='download', dest='distribution_type',  help="CloudFront target distribution type ['download', 'streaming']")
    parser.add_argument('resource', metavar='resource-url', type=str, nargs=1, help="Use the FULL URL for download distributions. For streaming distribution, use only")

    args=parser.parse_args()

    if args.distribution_type not in ['download', 'streaming']:
        raise argparse.ArgumentTypeError("Invalid value to 'DISTRIBUTION_TYPE'. Valid values: 'download' or 'streaming'. Check '--help' ..." )

    priv_key_file = args.priv_key_file
    key_pair_id = args.key_pair_id
    expires = int(time.time()) + int(args.expires)

    #Create the signed URL
    priv_key_string = open(args.priv_key_file).read()
    signed_url = get_canned_policy_url(args.resource[0], priv_key_string, key_pair_id, expires)


    #print signed URL
    if args.distribution_type == 'streaming':
        #Flash player doesn't like query params so encode them if you're using a streaming distribution
        enc_url = encode_query_param(signed_url)
        print(enc_url)
    else:
        print(signed_url)



if __name__ == '__main__':
    main(sys.argv[1:])
