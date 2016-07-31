encrypted_data = raw_input('Where is the encrypted data? ')
priv_key = raw_input("Where your private key? ")
data_file = raw_input("where do you want the decrypted data? ")


def decrypt_rsa(private_key_loc, package):
    """
    public_key_loc = Path to your private key
    package = String to be decrypted
    return decrypted string
    """
    enc = open(str(package), 'r').read()
    from Crypto.PublicKey import RSA
    from Crypto.Cipher import PKCS1_OAEP
    from base64 import b64decode
    key = open(private_key_loc, 'r').read()
    rsakey = RSA.importKey(key)
    rsakey = PKCS1_OAEP.new(rsakey)
    decrypted = rsakey.decrypt(b64decode(enc))
    return decrypted


try:
    f = open(data_file, 'w+')
    f.write(decrypt_rsa(priv_key, encrypted_data))
    f.close()
    print "Written to %s" % data_file
except IOError:
    print ("Write failed check file path...")
