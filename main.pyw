#https://stackoverflow.com/questions/41967367/pyqt5-using-qtdesigner-how-do-you-connect-a-signal-with-a-slot-callable-define/41968112#41968112


import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from Ui import Ui_Win
from cryptex import cryptor
from pyautogui import alert , confirm

Decrypt_Hidden = True
Encrypt_Hidden = True

class MainW (QMainWindow, Ui_Win):
	def __init__(self):
		QMainWindow.__init__(self)
		self.setupUi(self)
		self.file_to_encrypt , self.file_to_decrypt , self.file_to_save_encrypted , self.file_to_save_decrypted = "" , "" , "" , ""
		self.Browse_E_In.clicked.connect(self.browse_e_in)
		self.Browse_E_Out.clicked.connect(self.browse_e_out)
		self.Browse_D_In.clicked.connect(self.browse_d_in)
		self.Browse_D_Out.clicked.connect(self.browse_d_out)
		self.Visible_E.clicked.connect(self.visible_e)
		self.Visible_D.clicked.connect(self.visible_d)
		self.Encrypt.clicked.connect(self.start_enc)
		self.Decrypt.clicked.connect(self.start_dec)
		self.actionHelp.triggered.connect(self.helping)

	def helping(self):
		alert("This Progran has been made by Mr. Tatva Agarwal\nFor Usage and more info go to:\nhttps://github.com/CoderTatva-2006/SafeCryptex")

	def start_enc(self):
		if self.file_to_encrypt and self.file_to_save_encrypted and str(self.Pass.text()) != "":
			alert("Starting Encryption...\nPlease click Ok and Wait")
			c = cryptor(self.file_to_encrypt , self.file_to_save_encrypted , self.Pass.text())
			val = c.enc()
			if val == "Encrypted":
				alert("Eecryption Complete!")
			elif val == "FileErr":
				alert("Files chosen are not present on  the system!")
			else:
				alert("An Error Occurred , Please try again!")
		else:
			alert("Please Enter Valid Values into all the required fields!")

	def start_dec(self):
		if self.file_to_decrypt and self.file_to_save_decrypted and str(self.Pass_D.text()) != "":
			alert("Starting Decryption...\nPlease click Ok and Wait")
			c = cryptor(self.file_to_decrypt , self.file_to_save_decrypted , self.Pass_D.text())
			val = c.dec()
			if val == "Decrypted":
				alert("Decryption Complete!")
			elif val == "FileErr":
				alert("Files chosen are not present on  the system!")
			elif val == "Err":
				alert("Invalid Password! , Please Try Again.")
			else:
				alert("An Error Occurred , Please try again!")
		else:
			alert("Please Enter Valid Values into all the required fields!")


	def visible_e(self):
		global Encrypt_Hidden
		if Encrypt_Hidden:
			self.Pass.setEchoMode(QLineEdit.Normal)
			Encrypt_Hidden = False
		else:
			self.Pass.setEchoMode(QLineEdit.Password)
			Encrypt_Hidden = True

	def visible_d(self):
		global Decrypt_Hidden
		if Decrypt_Hidden:
			self.Pass_D.setEchoMode(QLineEdit.Normal)
			Decrypt_Hidden = False
		else:
			self.Pass_D.setEchoMode(QLineEdit.Password)
			Decrypt_Hidden = True
		
	def browse_e_in(self):
		self.file_to_encrypt = str(QFileDialog.getOpenFileName(self, 'Open File To Encrypt')[0]) 
		self.Input_E_File.setText(self.file_to_encrypt)

	def browse_e_out(self):
		self.file_to_save_encrypted = str(QFileDialog.getSaveFileName(self,"Save Encrypted File","","Aes Files (*.aes);;All Files (*)")[0])
		self.Output_E_File.setText(self.file_to_save_encrypted)

	def browse_d_in(self):
		self.file_to_decrypt = str(QFileDialog.getOpenFileName(self, 'Open File To Decrypt' , "" , "Aes Files (*.aes);;All Files (*)")[0])
		self.Input_D_File.setText(self.file_to_decrypt)
		
	def browse_d_out(self):
		self.file_to_save_decrypted = str(QFileDialog.getSaveFileName(self,"Save Decrypted File","","All Files (*)")[0])  
		self.Output_D_File.setText(self.file_to_save_decrypted)
	
		
		
if __name__ == '__main__':

	app = QApplication(sys.argv)
	myapp = MainW()
	myapp.show()
	sys.exit(app.exec_())