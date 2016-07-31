msg = raw_input('What would you like to encrypt? ')
key_path = raw_input('Where is your key file? ')
data_file = raw_input('Where do you want your data to be output? ')


def encrypt_rsa(public_key_loc, message):
    """
    public_key_loc Path to public key
    message String to be encrypted
    return base64 encoded encrypted string
    """
    from Crypto.PublicKey import RSA
    from Crypto.Cipher import PKCS1_OAEP
    key = open(public_key_loc, "r").read()
    rsakey = RSA.importKey(key)
    rsakey = PKCS1_OAEP.new(rsakey)
    encrypted = rsakey.encrypt(message)
    return encrypted.encode('base64')


try:
    f = open(data_file, 'w')
    f.write(encrypt_rsa(key_path, msg))
    f.close()
    print "Written to %s" % data_file
except IOError:
    print ("Write failed check data path...")
