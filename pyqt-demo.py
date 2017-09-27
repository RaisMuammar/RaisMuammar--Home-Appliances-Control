import sys, os, glob
from PyQt4 import QtCore, QtGui, uic
import serial, time

qtCreatorFile = "pyQtEdit.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtGui.QMainWindow, Ui_MainWindow):
	def __init__(self):
		QtGui.QMainWindow.__init__(self)
		Ui_MainWindow.__init__(self)
		self.setupUi(self)
		self.pushButton_OpenSerial.clicked.connect(self.OpenSerial)
		self.pushButton_Exit.clicked.connect(self.AppExit)
		self.pushButton_Lampu_ON.clicked.connect(self.Lampu_ON)
		self.pushButton_Lampu_OFF.clicked.connect(self.Lampu_OFF)
		self.pushButton_Kipas_ON.clicked.connect(self.Kipas_ON)
		self.pushButton_Kipas_OFF.clicked.connect(self.Kipas_OFF)
		self.pushButton_Dispenser_ON.clicked.connect(self.Dispenser_ON)
		self.pushButton_Dispenser_OFF.clicked.connect(self.Dispenser_OFF)
				
		self.textEdit_LogMessage.append("Demo Kontrol Peralatan Rumah Tangga")
		self.pushButton_Lampu_OFF.setEnabled(False)
		self.pushButton_Lampu_ON.setEnabled(False)
		self.pushButton_Kipas_ON.setEnabled(False)
		self.pushButton_Kipas_OFF.setEnabled(False)
		self.pushButton_Dispenser_ON.setEnabled(False)
		self.pushButton_Dispenser_OFF.setEnabled(False)
		
		
	def OpenSerial(self):
		if self.pushButton_OpenSerial.text()=='Open Serial':
			self.ser = serial.Serial("COM3", "9600", timeout=0.1)
			if self.ser.isOpen():
				self.pushButton_OpenSerial.setText('Close Serial')
				self.textEdit_LogMessage.append("Opening serial port... OK")
				self.pushButton_Lampu_ON.setEnabled(True)
				self.pushButton_Lampu_OFF.setEnabled(True)
				self.pushButton_Kipas_ON.setEnabled(True)
				self.pushButton_Kipas_OFF.setEnabled(True)
				self.pushButton_Dispenser_ON.setEnabled(True)
				self.pushButton_Dispenser_OFF.setEnabled(True)

			else:
				self.textEdit_LogMessage.append("can not open serial port")
		else:
			if self.ser.isOpen():
				self.ser.close()
			self.pushButton_OpenSerial.setText('Open Serial')
			self.textEdit_LogMessage.append("Closing serial port... OK")
			self.pushButton_Lampu_OFF.setEnabled(False)
			self.pushButton_Lampu_ON.setEnabled(False)
			self.pushButton_Kipas_ON.setEnabled(False)
			self.pushButton_Kipas_OFF.setEnabled(False)
			self.pushButton_Dispenser_ON.setEnabled(False)
			self.pushButton_Dispenser_OFF.setEnabled(False)


		

	def Lampu_ON(self):
		self.TXdata = bytearray(1)
		self.ser.write(self.TXdata)
		time.sleep(2)
		self.bytesToRead = self.ser.inWaiting()
		self.pushButton_Lampu_ON.setEnabled(False)
		self.textEdit_LogMessage.append("Lampu ON")
	def Lampu_OFF(self):
		self.TXdata = bytearray(2)
		self.ser.write(self.TXdata)
		time.sleep(2)
		self.bytesToRead = self.ser.inWaiting()
		self.pushButton_Lampu_ON.setEnabled(True)
		self.textEdit_LogMessage.append("Lampu OFF")

	def Kipas_ON(self):
		self.TXdata = bytearray(3)
		self.ser.write(self.TXdata)
		time.sleep(2)
		self.bytesToRead = self.ser.inWaiting()
		self.pushButton_Kipas_ON.setEnabled(False)
		self.textEdit_LogMessage.append("Kipas ON")
	def Kipas_OFF(self):
		self.TXdata = bytearray(4)
		self.ser.write(self.TXdata)
		time.sleep(2)
		self.bytesToRead = self.ser.inWaiting()
		self.pushButton_Kipas_ON.setEnabled(True)
		self.textEdit_LogMessage.append("Kipas OFF")

	def Dispenser_ON(self):
		self.TXdata = bytearray(5)
		self.ser.write(self.TXdata)
		time.sleep(2)
		self.bytesToRead = self.ser.inWaiting()
		self.pushButton_Dispenser_ON.setEnabled(False)
		self.textEdit_LogMessage.append("Dispenser ON")
	def Dispenser_OFF(self):
		self.TXdata = bytearray(6)
		self.ser.write(self.TXdata)
		time.sleep(2)
		self.bytesToRead = self.ser.inWaiting()
		self.pushButton_Dispenser_ON.setEnabled(True)
		self.textEdit_LogMessage.append("Dispenser OFF")
		
				
	def AppExit(self):
		self.textEdit_LogMessage.setText("Exit application")
		self.TXdata = bytearray(7)
		self.ser.write(self.TXdata)
		sys.exit()
		
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
