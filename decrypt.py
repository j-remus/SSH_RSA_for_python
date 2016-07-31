encrypted_data = raw_input('Where is the encrypted data? ')


def decrypt_RSA(private_key_loc, package):
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


f = open('Dec_data', 'w+')
f.write(decrypt_RSA('/Users/zachrayburn/.ssh/id_rsa', encrypted_data))
f.close()
