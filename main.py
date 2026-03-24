from Crypto.Cipher import AES


key = b'spam_secret_key!'
cipher = AES.new(key, AES.MODE_OFB)
