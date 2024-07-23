from Crypto.Cipher import DES


key = 'spam'
cipher = DES.new(key, DES.MODE_OFB)  # https://rules.sonarsource.com/python/type/Vulnerability/RSPEC-5547/
