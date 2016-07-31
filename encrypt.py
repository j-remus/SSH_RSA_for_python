import subprocess

msg = raw_input('What would you like to encrypt? ')


def encrypt_RSA(public_key_loc, message):
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


f = open('Enc_data', 'w')
f.write(encrypt_RSA('/Users/zachrayburn/.ssh/id_rsa.pub', msg))
f.close()
print "Written to Enc_data"
