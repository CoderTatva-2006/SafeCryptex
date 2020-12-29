# This file gives method for pyAesCrypt
# https://pypi.org/project/pyAesCrypt/

import pyAesCrypt
import hashlib
BUF = 64 * 1024 #64 Kb buffer size
class cryptor():
	def __init__(self , infile : str, outfile : str , password : str , buf : int = BUF):
		self.infile = infile
		self.outfile = outfile
		self.password = password
		self.passhashed = hashlib.sha256(self.password.encode()).hexdigest()
		self.buf = buf
	def enc(self):
		try:
			pyAesCrypt.encryptFile(self.infile , self.outfile , self.passhashed , self.buf)
			return "Encrypted"
		
		except IOError:
			return "FileErr"
		except:
			return "Err"
	def dec(self):
		try:
			pyAesCrypt.decryptFile(self.infile , self.outfile , self.passhashed , self.buf)
			return "Decrypted"
		except ValueError:
			return "Err"
		except IOError:
			return "FileErr"


